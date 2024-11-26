import re

from rich.text import Text

from tygenie.alerts_list.formatter import BaseFormatter
from tygenie.opsgenie_rest_api_client.models.alert_report import AlertReport


class PCI(BaseFormatter):

    displayed_fields = {
        #    'tiny_id': '#ID',
        "created_at": "Created",
        # 'last_occurred_at': 'Last Occured',
        "status": "Status",
        "priority": "Priority",
        "region": "Region",
        "message": "Message",
        "owner": "Owner",
        "closed_by": "Closed by",
    }

    def region(self, value) -> Text:
        m = re.match(r"^\[([^\[]+)\].*$", self.to_format["message"])
        region = ""
        if m and m.groups():
            region = m.group(1)
        return Text(
            region, style=self.app.theme_variables.get("warning", self.colors["white"])
        )

    def host(self, value) -> Text:
        m = re.match(r".+ (.+)\.cloud\.ovh\.net.+", self.to_format["message"])
        host = ""
        if m and m.groups():
            host = m.group(1)
        return Text(
            host,
            style=self.app.theme_variables.get(
                "secondary-lighten-3", self.colors["white"]
            ),
        )

    def light_message(self, value) -> Text:
        value = re.sub(r"(.+) .+\.cloud\.ovh\.net\s:\s+(.+)", r"\g<1> \g<2>", value)
        value = re.sub(r"^\[[A-Z\-]+\d+(\.[A-Z]+)?\] ", "", value)
        return Text(value[0:80])

    def message(self, value) -> Text:
        value = re.sub(r"^\[([^\[]+)\]\s*\:?\s*", "", value)
        if len(value) > 100:
            value = value[0:100] + "..."
        return Text(str(value).rstrip(","))
