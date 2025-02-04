from textual import on
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button

from tygenie.config import ty_config
from tygenie.consts import VERSION
from tygenie.widgets.input import TagValueInput


class AlertActionContainer(Widget):

    tag_value: reactive = reactive("", recompose=True)

    async def watch_tag_value(self):
        input = self.query_one("#tag_alert", Button)
        input.label = f"Tag alert '{self.tag_value}'"
        await self.recompose()

    def __init__(self, tag_value: str = "", **kwargs) -> None:
        super().__init__(**kwargs)
        if tag_value == "":
            tag_value = ty_config.tygenie.get("default_tag", "")

        self.set_reactive(AlertActionContainer.tag_value, tag_value)

    def compose(self) -> ComposeResult:
        self.border_title = "Actions"
        self.border_subtitle = f"[orange1]Version:[/orange1] [b]{VERSION}[/b]"
        with Horizontal(id="alert_action_horizontal_container"):
            yield TagValueInput(id="tag_value_container")
            yield Button(
                label=f"Tag alert '{self.tag_value}'", name="tag_alert", id="tag_alert"
            )
            yield Button(
                label="Open in webbrowser",
                name="open_in_webbrowser",
                id="open_in_webbrowser",
            )
            yield Button(label="Add note", name="add_note", id="add_note")

    class OpenInBrowser(Message):
        """A message to indicate that we have to open selected alert in webbrowser"""

    class AddNote(Message):
        """A message to indicate that we have to open selected alert alertmanager link"""

    class AddTag(Message):
        """A message to indicate that we have to open selected alert alertmanager link"""

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.name == "open_in_webbrowser":
            self.post_message(self.OpenInBrowser())
        if event.button.name == "add_note":
            self.post_message(self.AddNote())
        if event.button.name == "tag_alert":
            self.post_message(self.AddTag())

    @on(TagValueInput.TagValueChange)
    def update_tag_value(self, message: TagValueInput.TagValueChange):
        self.tag_value = message.label
