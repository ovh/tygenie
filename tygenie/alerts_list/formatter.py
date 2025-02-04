import re
from importlib import import_module

import pendulum
from rich.text import Text
from textual.app import App
from udatetime import from_string as dtfstr

import tygenie.config as config
from tygenie.opsgenie_rest_api_client.models.alert import Alert
from tygenie.opsgenie_rest_api_client.models.alert_report import AlertReport


class BaseFormatter:

    displayed_fields = {
        "created_at": "Created",
        "duration": "Created since",
        "status": "Status",
        "priority": "Priority",
        "message": "Message",
        "owner": "Owner",
        "closed_by": "Closed By",
    }

    colors = {"white": "#ffffff"}

    def __init__(
        self,
        to_format: dict = {},
        alert: None | Alert = None,
        disabled: bool = False,
        app: App | None = None,
    ) -> None:
        self.to_format: dict = to_format
        self.alert: Alert | None = alert
        self.formatted: dict[Text, Text] = {k: Text("") for k in self.to_format.keys()}
        self.date_format: str = config.ty_config.tygenie.get("alerts", {}).get(
            "date_format", "%d/%m %H:%M"
        )
        self.disabled: bool = disabled
        if isinstance(app, App):
            self.app = app

    def format(self) -> dict:
        for attr, value in self.to_format.items():
            if not hasattr(self, attr) or self.disabled:
                self.formatted[attr] = Text(str(value))
                continue
            self.formatted[attr] = getattr(self, attr)(value)

        return self.formatted

    def _as_date(self, value) -> str:
        if value is None:
            return ""
        # value is a datetime object, so it is safe to call isoformat
        return dtfstr(value.isoformat()).strftime(self.date_format)

    def tiny_id(self, value) -> Text:
        return Text(
            value, style=self.app.theme_variables["secondary"], justify="center"
        )

    def created_at(self, value) -> Text:
        return Text(
            self._as_date(value),
            style=self.app.theme_variables["secondary-lighten-3"],
            justify="center",
        )

    def updated_at(self, value) -> Text:
        return Text(self._as_date(value), style=self.colors["white"], justify="center")

    def last_occurred_at(self, value) -> Text:
        return Text(self._as_date(value), style=self.colors["white"], justify="center")

    def owner(self, value) -> Text:
        return Text(
            re.sub("@.*$", "", value),
            style=self.app.theme_variables["warning"],
            justify="left",
        )

    def light_message(self, value) -> Text:
        return Text(value[0:80])

    def message(self, value) -> Text:
        if len(value) > 100:
            value = value[0:100] + "..."
        return Text(str(value))

    def closed_by(self, value) -> Text:
        value = ""
        if self.alert is not None and isinstance(self.alert.report, AlertReport):
            if self.alert.report.closed_by:
                value = self.alert.report.closed_by

        return Text(
            re.sub("@.*$", "", str(value)),
            style=self.app.theme_variables["warning"],
            justify="left",
        )

    def status(self, value) -> Text:
        if self.alert is None:
            return Text("")

        value = ""

        if self.alert.status == "open":
            value = "open"
            if self.alert.acknowledged:
                value = "acked"
        elif self.alert.status == "closed":
            value = "closed"

        return Text(
            value, style=self.app.theme_variables.get(value, ""), justify="left"
        )

    def priority(self, value) -> Text:
        theme_colors = self.app.theme_variables
        p_colors = [
            theme_colors.get("error", self.colors["white"]),
            theme_colors.get("accent", self.colors["white"]),
            theme_colors.get("warning", self.colors["white"]),
            theme_colors.get("secondary", self.colors["white"]),
            theme_colors.get("primary", self.colors["white"]),
        ]

        match = re.match(r"P(\d+)", value)
        if match is not None:
            return Text(
                value,
                style=p_colors[int(match.groups()[0]) - 1],
                justify="center",
            )
        else:
            return Text("")

    def duration(self, value) -> Text:
        created = pendulum.parse(str(self.to_format["created_at"]), tz="UTC")
        now_utc = pendulum.now(tz="UTC")
        duration = now_utc.diff_for_humans(created, absolute=True)
        return Text(
            duration,
            style=self.app.theme_variables.get("warning", self.colors["white"]),
        )


class AlertFormatter:

    def __init__(
        self,
        alert: Alert | None = None,
        formatter: str | None = None,
        app: App | None = None,
    ) -> None:
        self.alert: Alert | None = alert
        self.formatter: str | None = formatter or None
        self.app = app
        if self.formatter is None:
            self.module = import_module("tygenie.alerts_list.formatter")
            self.formatter = "DefaultFormatter"
        else:
            self.module = import_module(
                f"tygenie.plugins.{self.formatter}.alerts_list_formatter"
            )
        self.displayed_fields = getattr(self.module, self.formatter).displayed_fields

    def format(self) -> dict:
        to_format = {}
        if self.formatter is not None:
            for f in getattr(self.module, self.formatter).displayed_fields.keys():
                if not hasattr(self.alert, f):
                    to_format[f] = ""
                    continue
                to_format[f] = getattr(self.alert, f)
            return getattr(self.module, self.formatter)(
                to_format, alert=self.alert, app=self.app
            ).format()
        else:
            return {}


class DefaultFormatter(BaseFormatter):
    """Default alert list formatter"""
