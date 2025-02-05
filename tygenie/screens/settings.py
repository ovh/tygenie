import json
from typing import TYPE_CHECKING

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Grid
from textual.message import Message
from textual.widgets import Button, Footer, TextArea

import tygenie.config as config
import tygenie.logger as logger
import tygenie.opsgenie as opsgenie
from tygenie import consts
from tygenie.screen import TyScreen
from tygenie.widgets.textarea import TygenieTextArea

if TYPE_CHECKING:
    from tygenie.app import TygenieApp


class SettingsScreen(TyScreen):

    BINDINGS = [
        Binding(
            key="ctrl+a", action="activate_alerts_screen()", description="Alerts screen"
        ),
        Binding(key="ctrl+s", action="save_config()", description="Save config"),
        Binding(key="ctrl+q", action="quit", description="Quit"),
    ]

    def __init__(self):
        self.original_text = ""
        self.has_changed = True
        super().__init__()
        self.app: "TygenieApp"

    async def on_screen_resume(self):
        await self.recompose()

    class SettingsUpdated(Message):
        """Message to indicate that settings have been updated and that we go back to alert list"""

    def compose(self) -> ComposeResult:
        config.ty_config.load()
        textarea = TygenieTextArea.code_editor(
            json.dumps(config.ty_config.config, indent=2),
            soft_wrap=True,
            language="json",
            id="settings_textarea",
        )
        self.original_text = textarea.text
        yield Grid(
            textarea,
            Button("Save", variant="success", id="save"),
            id="settings_grid",
        )
        yield Footer()

    async def action_save_config(self):
        await self.save_config()

    def action_activate_alerts_screen(self):
        if self.has_changed:
            self.post_message(self.SettingsUpdated())
        self.app.switch_screen(f"{consts.ALERTS_SCREEN_NAME}")

    async def _save_config(self):
        textarea = self.query_one("#settings_textarea", TextArea)
        try:
            original_json = json.loads(self.original_text)
            current_json = json.loads(textarea.text)

            if original_json == current_json:
                self.notify("No change detected")
                self.has_changed = False
            else:
                config.ty_config.save(config=json.loads(textarea.text))
                self.has_changed = True
        except Exception as e:
            self.has_changed = False
            self.notify(severity="error", message=f"Unable to write configuration: {e}")
        else:
            if self.has_changed:
                self.original_text = textarea.text
                self.notify(
                    severity="information", message="Configuration successfully saved"
                )
            try:
                config.ty_config.reload()
                opsgenie.reload()
                logger.reload()

                await self.app.reload()
            except Exception as e:
                self.notify(severity="error", message=f"Failed to relaod app: {e}")

    async def save_config(self):
        await self._save_config()
        if config.ty_config.sample_copied:
            self.notify(f"Sample copied: {config.ty_config.sample_copied}")
            # As it is the first config, go back to alerts list
            self.action_activate_alerts_screen()

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "save":
            await self.save_config()
