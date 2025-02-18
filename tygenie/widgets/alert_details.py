from rich.text import Text
from textual.containers import VerticalScroll
from textual.content import Content
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import (
    ContentSwitcher,
    DataTable,
    Label,
    Markdown,
    Pretty,
    Static,
    TabPane,
)

import tygenie.config as config
import tygenie.opsgenie as opsgenie
from tygenie.widgets.center_middle import CenterMiddle
from tygenie.widgets.tabbed_content import TygenieTabbedContent
from tygenie.widgets.tags import Tags


class AlertDetailsTabbedContent(TygenieTabbedContent):
    pass


class AlertDetailTitle(Static):

    title = reactive(Content(""))

    def watch_title(self):
        self.update(Content.from_markup("$title", title=self.title))


class AlertDetails(Widget):

    DEFAULT_CSS = """\
    RawAlertDetails {
        & #no_alert_details_label {
            height: 1fr;
            hatch: right $surface-lighten-1 70%;
        }

        & #no_alert_description_label {
            height: 1fr;
            hatch: right $surface-lighten-1 70%;
        }

        & #no_alert_tags_label {
            height: 1fr;
            hatch: right $surface-lighten-1 70%;
        }
    }
"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.urls = []

    def compose(self):
        self.border_title = "Alert details"
        yield AlertDetailTitle(id="alert_details_title")
        alert_details_config = config.ty_config.tygenie.get("alert_details", {})
        initial_tab = alert_details_config.get("default_tab", "details")
        with AlertDetailsTabbedContent(
            id="alert_detail_tabbed_content",
            initial=f"tabpane-{str(initial_tab).lower()}",
        ):
            with TabPane("Details", id="tabpane-details"):
                with ContentSwitcher(initial=None, id="alert_details_details_switcher"):
                    yield CenterMiddle(
                        Label("The alert doesn't have detail"),
                        id="no_alert_details_label",
                    )
                    with VerticalScroll(id="alert_detail_pretty_container"):
                        yield DataTable(id="datatable_alert_details")
            with TabPane("Tags", id="tabpane-tags"):
                with ContentSwitcher(initial=None, id="alert_details_tags_switcher"):
                    yield CenterMiddle(
                        Label("The alert doesn't have a tag"), id="no_alert_tags_label"
                    )
                    with VerticalScroll(id="alert_tags_container"):
                        yield Tags(names=[], id="alert_tags_checkboxes")
            with TabPane("Description", id="tabpane-description"):
                with ContentSwitcher(
                    initial=None, id="alert_details_description_switcher"
                ):
                    yield CenterMiddle(
                        Label("The alert doesn't have description"),
                        id="no_alert_description_label",
                    )
                    with VerticalScroll(id="alert_description_md_container"):
                        yield Markdown(None, id="pretty_alert_description")
            with TabPane("RAW", id="tabpane_raw"):
                with VerticalScroll():
                    yield Pretty(None, id="pretty_raw_alert_detail")

    class UpdateAlertDetails(Message):

        def __init__(self, alert) -> None:
            self.alert = alert.data
            super().__init__()

    async def get_alert_detail(self, opsgenie_id: str | None = None):
        if not opsgenie_id:
            return None
        alert = await opsgenie.client.api.get_alert(
            parameters={
                "identifier": opsgenie_id,
                "identifier_type": "id",
            }
        )

        if alert is not None:
            # Update alert_detail_title
            self.post_message(self.UpdateAlertDetails(alert=alert))
        else:
            self.notify(severity="error", message="Unable to get alert detail")
