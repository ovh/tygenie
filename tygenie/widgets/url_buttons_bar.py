import json

from textual.app import ComposeResult
from textual.containers import HorizontalScroll
from textual.widget import Widget

from tygenie.widgets.buttons import Buttons


class AlertDetailsUrlButtonsBar(Widget):

    def compose(self) -> ComposeResult:
        self.display = False
        self.border_title = "Related links"
        with HorizontalScroll(id="alert_details_url_buttons_container"):
            yield Buttons(id="alert_details_url_buttons")

    def update(self, names_urls=[]):
        self.query_one("#alert_details_url_buttons", Buttons).update(names_urls)
        if names_urls:
            self.display = True

    def parse_content_and_update(self, content={}):
        def get_values(i):
            if isinstance(i, dict):
                return [
                    value for sub_item in i.values() for value in get_values(sub_item)
                ]
            elif isinstance(i, list):
                return [value for sub_item in i for value in get_values(sub_item)]
            else:
                return [i]

        content_dict = json.loads(content)
        return get_values(content_dict)
