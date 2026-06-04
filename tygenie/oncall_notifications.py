"""Pre-shift oncall reminder notifications.

Fires desktop notifications ahead of the user's upcoming Opsgenie oncall
shifts. Triggers are configured under ``tygenie.oncall_notifications`` in
``tygenie.json``. Notifications fire even when ``desktop_notification.enable``
is ``false`` -- this feature has its own ``enable`` toggle.
"""

from __future__ import annotations

import json
import os
import pathlib
import re
from dataclasses import dataclass, field
from typing import Any

import pendulum
from desktop_notifier import Urgency

import tygenie.config as config
import tygenie.logger as ty_logger
import tygenie.opsgenie as opsgenie
from tygenie.opsgenie_rest_api_client.types import Unset

STATE_DIR = pathlib.Path.home() / ".local" / "share" / "tygenie"
STATE_FILE = STATE_DIR / "oncall_notifications_state.json"

LAST_FRIDAY = "last_friday"

DEFAULT_CONFIG: dict[str, Any] = {
    "enable": True,
    "check_interval": 3600,
    "notify_at_hour": 10,
    "timezone": "local",
    "urgency": "Critical",
    # Triggers whose scheduled time has passed by more than this are not
    # delivered -- they're silently marked as fired in the state file so
    # they don't keep being checked. Prevents a burst of stale reminders
    # the first time the feature is activated against an imminent shift.
    "max_catchup_hours": 24,
    "triggers": {
        "one_month": {"enable": True, "months": 1},
        "two_weeks": {"enable": True, "weeks": 2},
        LAST_FRIDAY: {"enable": True},
    },
}


def _resolve_urgency(value: Any) -> Urgency:
    """Map a config string (e.g. ``"Critical"``) to a ``desktop_notifier`` Urgency.

    Falls back to ``Urgency.Critical`` on unknown/empty values.
    """
    name = str(value or "Critical").capitalize()
    return getattr(Urgency, name, Urgency.Critical)


def _resolve_timezone(value: Any) -> str:
    """Validate a config timezone string. Falls back to ``"local"`` on errors.

    Accepts an IANA name (e.g. ``"Europe/Paris"``), the literal ``"local"``,
    or empty/None for the system local zone.
    """
    tz = str(value).strip() if value else "local"
    if not tz:
        tz = "local"
    try:
        pendulum.timezone(tz)
    except Exception as exc:
        ty_logger.logger.log(
            f"oncall_notifications: invalid timezone '{tz}' ({exc}), falling back to local"
        )
        return "local"
    return tz


@dataclass(frozen=True)
class Shift:
    schedule_id: str
    start: pendulum.DateTime
    end: pendulum.DateTime
    schedule_name: str = ""
    rotation_name: str = ""

    @property
    def key(self) -> str:
        return f"{self.schedule_id}:{self.start.to_iso8601_string()}"

    def context_line(self) -> str:
        parts: list[str] = []
        if self.schedule_name:
            parts.append(f"Schedule: {self.schedule_name}")
        if self.rotation_name:
            parts.append(f"Rotation: {self.rotation_name}")
        return " | ".join(parts)


@dataclass
class OncallNotificationsState:
    path: pathlib.Path = STATE_FILE
    data: dict[str, Any] = field(default_factory=lambda: {"version": 1, "fired": {}})

    def load(self) -> None:
        if not self.path.exists():
            return
        try:
            with open(self.path, "r") as fh:
                self.data = json.load(fh)
            self.data.setdefault("version", 1)
            self.data.setdefault("fired", {})
        except (OSError, json.JSONDecodeError) as exc:
            ty_logger.logger.log(
                f"oncall_notifications: cannot read state file ({exc}); starting fresh"
            )
            self.data = {"version": 1, "fired": {}}

    def save(self) -> None:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(self.path.suffix + ".tmp")
        with open(tmp, "w") as fh:
            json.dump(self.data, fh, indent=2)
        os.replace(tmp, self.path)

    def already_fired(self, shift_key: str, trigger: str) -> bool:
        return bool(self.data["fired"].get(shift_key, {}).get(trigger))

    def mark_fired(
        self, shift: Shift, trigger: str, fired_at: pendulum.DateTime
    ) -> None:
        entry = self.data["fired"].setdefault(shift.key, {})
        entry[trigger] = fired_at.to_iso8601_string()
        entry["shift_end"] = shift.end.to_iso8601_string()

    def prune(self, before: pendulum.DateTime) -> None:
        cutoff_iso = before.to_iso8601_string()
        stale = [
            key
            for key, entry in self.data["fired"].items()
            if entry.get("shift_end", "") < cutoff_iso
        ]
        for key in stale:
            del self.data["fired"][key]


def _trigger_times(
    shift_start: pendulum.DateTime,
    triggers_cfg: dict[str, Any],
    notify_hour: int,
    tz: str = "local",
) -> dict[str, pendulum.DateTime]:
    """Compute the firing time for each enabled trigger.

    Lead-time triggers may specify ``months``, ``weeks`` and/or ``days``;
    all present units are subtracted from ``shift_start``. The
    ``last_friday`` trigger has no duration -- it lands on the Friday
    strictly before ``shift_start``. The configured ``tz`` defines what
    ``notify_hour`` means -- e.g. 10:00 Europe/Paris regardless of the host
    timezone.
    """

    def at_hour(d: pendulum.DateTime) -> pendulum.DateTime:
        return d.in_tz(tz).set(hour=notify_hour, minute=0, second=0, microsecond=0)

    out: dict[str, pendulum.DateTime] = {}
    for name, cfg in triggers_cfg.items():
        if not isinstance(cfg, dict) or not cfg.get("enable", True):
            continue
        if name == LAST_FRIDAY:
            d = shift_start.subtract(days=1)
            while d.day_of_week != pendulum.FRIDAY:
                d = d.subtract(days=1)
            out[name] = at_hour(d)
        else:
            kwargs = {k: cfg[k] for k in ("months", "weeks", "days") if k in cfg}
            if not kwargs:
                ty_logger.logger.log(
                    f"oncall_notifications: trigger '{name}' has no duration, skipping"
                )
                continue
            out[name] = at_hour(shift_start.subtract(**kwargs))
    return out


def _trigger_label(trigger: str, trigger_cfg: dict[str, Any]) -> str:
    if trigger == LAST_FRIDAY:
        return "Friday before"
    for unit, suffix in (("months", "month"), ("weeks", "week"), ("days", "day")):
        n = trigger_cfg.get(unit)
        if isinstance(n, int) and n > 0:
            return f"{n} {suffix}{'s' if n != 1 else ''} before"
    return trigger


def _strip_domain(name: str) -> str:
    return re.sub("@.*$", "", name).lower()


class OncallNotifier:
    """Periodic worker that fires pre-shift oncall reminders."""

    def __init__(self, app):
        self.app = app
        self.state = OncallNotificationsState()

    def _settings(self) -> dict[str, Any]:
        cfg = config.ty_config.tygenie.get("oncall_notifications", {})
        # Top-level scalars fall back to defaults; triggers are taken verbatim
        # from user config so removing one from the config disables it.
        merged: dict[str, Any] = {**DEFAULT_CONFIG, **cfg}
        if "triggers" not in cfg:
            merged["triggers"] = DEFAULT_CONFIG["triggers"]
        return merged

    def _urgency(self) -> Urgency:
        return _resolve_urgency(self._settings().get("urgency"))

    def _tz(self) -> str:
        return _resolve_timezone(self._settings().get("timezone"))

    async def check_and_fire(self) -> None:
        settings = self._settings()
        if not settings.get("enable", True):
            return

        username = _strip_domain(config.ty_config.opsgenie.get("username", ""))
        if not username:
            ty_logger.logger.log(
                "oncall_notifications: opsgenie.username is empty, skipping check"
            )
            return

        tz = _resolve_timezone(settings.get("timezone"))
        self.state.load()
        self.state.prune(pendulum.now(tz).subtract(days=7))

        shifts = await self._fetch_upcoming_shifts(username, tz)
        notify_hour = int(settings.get("notify_at_hour", 10))
        triggers_cfg = settings.get("triggers", {})
        urgency = _resolve_urgency(settings.get("urgency"))
        max_catchup_hours = max(
            0, int(settings.get("max_catchup_hours", 24) or 0)
        )
        max_catchup_seconds = max_catchup_hours * 3600
        now = pendulum.now(tz)

        for shift in shifts:
            for trig_name, trig_dt in _trigger_times(
                shift.start, triggers_cfg, notify_hour, tz
            ).items():
                if trig_dt > now or trig_dt >= shift.start:
                    continue
                if self.state.already_fired(shift.key, trig_name):
                    continue
                age_seconds = (now - trig_dt).total_seconds()
                if age_seconds > max_catchup_seconds:
                    ty_logger.logger.log(
                        f"oncall_notifications: skipping stale trigger "
                        f"'{trig_name}' ({age_seconds / 3600:.1f}h late) "
                        f"for shift {shift.key}"
                    )
                    self.state.mark_fired(shift, trig_name, now)
                    self.state.save()
                    continue
                try:
                    await self._fire(
                        shift,
                        trig_name,
                        triggers_cfg.get(trig_name, {}),
                        urgency,
                        tz,
                    )
                except Exception as exc:
                    ty_logger.logger.log(
                        f"oncall_notifications: failed to send notification: {exc}"
                    )
                    continue
                self.state.mark_fired(shift, trig_name, now)
                self.state.save()

    async def _fetch_upcoming_shifts(
        self, username: str, tz: str = "local"
    ) -> list[Shift]:
        schedule_ids = config.ty_config.opsgenie.get("on_call_schedule_ids", [])
        if not schedule_ids:
            return []

        shifts: dict[str, Shift] = {}
        now_local = pendulum.now(tz)
        for sched_id in schedule_ids:
            try:
                resp = await opsgenie.client.api.get_schedule_timeline(
                    identifier=sched_id, interval=3
                )
            except Exception as exc:
                ty_logger.logger.log(
                    f"oncall_notifications: timeline fetch failed for {sched_id}: {exc}"
                )
                continue
            if resp is None or isinstance(getattr(resp, "data", None), Unset):
                continue
            timeline = getattr(resp.data, "final_timeline", None)
            if timeline is None or isinstance(timeline, Unset):
                continue
            parent = getattr(resp.data, "field_parent", None)
            schedule_name = ""
            if parent is not None and not isinstance(parent, Unset):
                name_attr = getattr(parent, "name", None)
                if name_attr and not isinstance(name_attr, Unset):
                    schedule_name = str(name_attr)
            for rotation in timeline.rotations or []:
                rotation_name = ""
                rot_name = getattr(rotation, "name", None)
                if rot_name and not isinstance(rot_name, Unset):
                    rotation_name = str(rot_name)
                for period in rotation.periods or []:
                    shift = self._period_to_shift(
                        sched_id,
                        period,
                        username,
                        now_local,
                        schedule_name=schedule_name,
                        rotation_name=rotation_name,
                        tz=tz,
                    )
                    if shift is None:
                        continue
                    shifts.setdefault(shift.key, shift)
        return sorted(shifts.values(), key=lambda s: s.start)

    @staticmethod
    def _period_to_shift(
        sched_id: str,
        period,
        username: str,
        now_local: pendulum.DateTime,
        schedule_name: str = "",
        rotation_name: str = "",
        tz: str = "local",
    ) -> Shift | None:
        start_raw = getattr(period, "start_date", None)
        end_raw = getattr(period, "end_date", None)
        if not start_raw or isinstance(start_raw, Unset):
            return None
        if not end_raw or isinstance(end_raw, Unset):
            return None

        recipients: list[str] = []
        flat = getattr(period, "flattened_recipients", None)
        if flat and not isinstance(flat, Unset):
            recipients = [r.name for r in flat if getattr(r, "name", None)]
        elif getattr(period, "recipient", None) and not isinstance(
            period.recipient, Unset
        ):
            name = getattr(period.recipient, "name", None)
            if name:
                recipients = [name]
        if not any(_strip_domain(n) == username for n in recipients):
            return None

        start = pendulum.instance(start_raw).in_tz(tz)
        end = pendulum.instance(end_raw).in_tz(tz)
        if start <= now_local:
            return None  # active or past shift, no pre-notification
        return Shift(
            schedule_id=sched_id,
            start=start,
            end=end,
            schedule_name=schedule_name,
            rotation_name=rotation_name,
        )

    async def _fire(
        self,
        shift: Shift,
        trigger: str,
        trigger_cfg: dict[str, Any],
        urgency: Urgency,
        tz: str = "local",
    ) -> None:
        label = _trigger_label(trigger, trigger_cfg)
        title = f"Tygenie: oncall shift reminder ({label})"
        await self.app.notifier.send(
            title=title,
            message=_format_shift_message(shift, tz=tz),
            urgency=urgency,
        )
        ty_logger.logger.log(
            f"oncall_notifications: fired {trigger} for shift {shift.key}"
        )

    async def show_next_shift(self) -> None:
        """User-triggered: send a notification about the next upcoming shift.

        Bypasses both the dedup state and the ``enable`` toggle so the user
        can always pull this information on demand.
        """
        urgency = self._urgency()
        tz = self._tz()
        username = _strip_domain(config.ty_config.opsgenie.get("username", ""))
        if not username:
            await self.app.notifier.send(
                title="Tygenie: next oncall",
                message="opsgenie.username is not set in tygenie.json.",
                urgency=urgency,
            )
            return

        shifts = await self._fetch_upcoming_shifts(username, tz)
        if not shifts:
            await self.app.notifier.send(
                title="Tygenie: next oncall",
                message="No upcoming oncall shift found for you in the next 3 months.",
                urgency=urgency,
            )
            return

        shift = shifts[0]
        await self.app.notifier.send(
            title="Tygenie: your next oncall shift",
            message=_format_shift_message(shift, include_lead_time=True, tz=tz),
            urgency=urgency,
        )
        ty_logger.logger.log(
            f"oncall_notifications: on-demand next shift {shift.key}"
        )


def _format_shift_message(
    shift: Shift, include_lead_time: bool = False, tz: str = "local"
) -> str:
    # Render shift times in the user's configured timezone so the displayed
    # hour matches the one used for trigger computation.
    start_local = shift.start.in_tz(tz)
    end_local = shift.end.in_tz(tz)
    start_fmt = start_local.format("dddd D MMM YYYY HH:mm zz")
    end_fmt = end_local.format("ddd D MMM HH:mm")
    lines = [f"You are on call starting {start_fmt}.", f"Ends {end_fmt}."]
    context = shift.context_line()
    if context:
        lines.append(context)
    if include_lead_time:
        delta_days = (start_local.date() - pendulum.now(tz).date()).days
        if delta_days > 0:
            lines.append(f"Starts in {delta_days} day{'s' if delta_days != 1 else ''}.")
    return "\n".join(lines)
