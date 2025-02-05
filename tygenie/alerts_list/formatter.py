import re
from importlib import import_module

import pendulum
from rich.text import Text
from textual.app import App
from udatetime import from_string as dtfstr

import tygenie.config as config
import tygenie.logger as ty_logger
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
        formatter_fields: dict = {},
        alert: None | Alert = None,
        disabled: bool = False,
        app: App | None = None,
    ) -> None:
        self.to_format: dict = to_format
        self.formatter_fields: dict = formatter_fields
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
        created = pendulum.parse(str(self.formatter_fields["created_at"]), tz="UTC")
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
        self.formatter_fields = getattr(self.module, self.formatter).displayed_fields
        self.displayed_fields = self._get_final_displayed_fields()

    def _get_final_displayed_fields(self):
        displayed_fields = config.ty_config.tygenie.get("displayed_fields", {})
        fields_methods = displayed_fields.keys()
        if not fields_methods:
            displayed_fields = self.formatter_fields
            fields_methods = self.formatter_fields.keys()

        unknown_fields = []
        # Check if all custom fields have a corresponding method
        # 1/ check it exists in all fields
        # 2/ if it does not exists check the corresponding method name
        for method in fields_methods:
            if method in self.formatter_fields.keys():
                continue
            if self.formatter and str(method).lower() in dir(
                getattr(self.module, self.formatter)
            ):
                continue
            unknown_fields.append(method)

        if unknown_fields:
            ty_logger.logger.log(
                f"You defined some unknown fields that could not be displayed, they will be ignored: {unknown_fields}"
            )

        final_fields = [f for f in fields_methods if f not in unknown_fields]
        final_displayed_fields = {
            k: displayed_fields[k] for k in final_fields if k in displayed_fields
        }

        return final_displayed_fields

    def format(self) -> dict:
        to_format = {}
        formatter_fields = {}
        if self.formatter is not None:
            for f in self.formatter_fields.keys():
                if not hasattr(self.alert, f):
                    if f in self.displayed_fields:
                        to_format[f] = ""
                    formatter_fields[f] = ""
                    continue
                if f in self.displayed_fields:
                    to_format[f] = getattr(self.alert, f)
                formatter_fields[f] = getattr(self.alert, f)
            return getattr(self.module, self.formatter)(
                to_format=to_format,
                formatter_fields=formatter_fields,
                alert=self.alert,
                app=self.app,
            ).format()
        else:
            return {}


class DefaultFormatter(BaseFormatter):
    """Default alert list formatter"""
