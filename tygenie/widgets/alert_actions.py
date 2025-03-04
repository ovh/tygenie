import re
import httpx
import semver
from textual import on, work
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button
import tygenie.logger as ty_logger

from tygenie import consts
from tygenie.config import ty_config
from tygenie.widgets.input import TagValueInput


class AlertActionContainer(Widget):

    tag_value: reactive = reactive("", recompose=True)
    version: reactive = reactive(f"v{consts.VERSION}", recompose=True)

    async def watch_tag_value(self):
        input = self.query_one("#tag_alert", Button)
        input.label = f"Tag alert '{self.tag_value}'"
        await self.recompose()

    async def watch_version(self):
        self.border_subtitle = self.version
        await self.recompose()

    def __init__(self, tag_value: str = "", **kwargs) -> None:
        super().__init__(**kwargs)
        if tag_value == "":
            tag_value = ty_config.tygenie.get("default_tag", "")

        self.set_reactive(AlertActionContainer.tag_value, tag_value)

    def compose(self) -> ComposeResult:
        self.border_title = "Actions"
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

    class CheckTygenieNewVersion(Message):
        """A message"""

    async def on_mount(self):
        self.send_check_tygenie_version_message()
        # Check every 6 hours for new version
        self.set_interval(6 * 60 * 60, self.send_check_tygenie_version_message)

    @work(exclusive=True, exit_on_error=True, thread=True)
    def send_check_tygenie_version_message(self):
        self.post_message(self.CheckTygenieNewVersion())

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

    @on(CheckTygenieNewVersion)
    @work(exclusive=True, exit_on_error=True, thread=False)
    async def check_tygenie_new_version(self):
        ty_logger.logger.log("Checking latest Tygenie release...")
        try:
            async with httpx.AsyncClient() as client:
                data = await client.get(
                    url="https://api.github.com/repos/ovh/tygenie/releases/latest"
                )
                latest_version = re.sub("^v", "", data.json()["name"])

            if semver.compare(consts.VERSION, latest_version) < 0:
                ty_logger.logger.log(f"New version found: {latest_version}")
                self.version = (
                    f"v{consts.VERSION} - [$text-error]v{latest_version} available![/]"
                )
        except Exception:
            pass
