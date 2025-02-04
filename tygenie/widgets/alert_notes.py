from textual.containers import VerticalScroll
from textual.message import Message
from textual.widget import Widget
from textual.widgets import ContentSwitcher, Label, Markdown

import tygenie.opsgenie as opsgenie
from tygenie.widgets.center_middle import CenterMiddle


class AlertNotes(Widget):

    DEFAULT_CSS = """\
    AlertNotes {
        & #no_note_label {
            height: 1fr;
            hatch: right $surface-lighten-1 70%;
        }
    }
"""

    def compose(self):
        self.border_title = "Alert notes"
        content_switcher = ContentSwitcher(initial=None, id="alert_notes_switcher")
        with content_switcher:
            yield CenterMiddle(
                Label("The alert doesn't have a note"), id="no_note_label"
            )
            with VerticalScroll(id="alert_notes_markdown_container"):
                md = Markdown(None, name="Notes", id="md_alert_note")
                yield md

    class UpdateAlertNotes(Message):

        def __init__(self, alert_notes) -> None:
            self.alert_notes = alert_notes.data
            super().__init__()

    async def get_alert_notes(self, opsgenie_id: str | None = None):
        if not opsgenie_id:
            return None
        alert_notes = await opsgenie.client.api.get_alert_notes(
            parameters={
                "identifier": opsgenie_id,
                "identifier_type": "id",
            }
        )

        if alert_notes is not None:
            self.post_message(self.UpdateAlertNotes(alert_notes=alert_notes))
        else:
            self.notify(severity="error", message="Unable to get alert note")
