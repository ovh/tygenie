import argparse
import os

from desktop_notifier import DesktopNotifier
from textual import on
from textual.app import App
from textual.binding import Binding

import tygenie.config as config
import tygenie.logger as logger
import tygenie.opsgenie as opsgenie
import tygenie.screens.add_note
import tygenie.screens.alerts
import tygenie.screens.settings
from tygenie import consts
from tygenie.alert_details.description_formatter import ContentFormatter
from tygenie.alerts_list.formatter import AlertFormatter


class TygenieApp(App):
    """Opsgenie terminal application"""

    CSS_PATH = f'{os.path.join(os.path.dirname(__file__),"tygenie.tcss")}'
    BINDINGS = [
        Binding(
            key="ctrl+s",
            action=f'switch_screen("{consts.SETTINGS_SCREEN_NAME}")',
            description="Settings",
        ),
        Binding(key="ctrl+q", action="quit", description="Quit"),
    ]

    SCREENS = {
        consts.ALERTS_SCREEN_NAME: tygenie.screens.alerts.AlertsScreen,
        consts.SETTINGS_SCREEN_NAME: tygenie.screens.settings.SettingsScreen,
        consts.ADD_NOTE_SCREEN_NAME: tygenie.screens.add_note.AddNoteScreen,
    }

    COMMAND_PALETTE_BINDING = config.ty_config.tygenie.get("keybindings", {}).get(
        "palette", "ctrl+p"
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.notifier = DesktopNotifier(
            app_icon=f"{os.path.dirname(__file__)}/assets/icon.png"
        )
        self.started = False
        self.load_plugins()

    def load_plugins(self):
        plugins = config.ty_config.tygenie.get("plugins", {})
        self.alerts_list_formatter = AlertFormatter(
            formatter=plugins.get("alerts_list_formatter", None), app=self.app
        )
        self.alert_description_formatter = ContentFormatter(
            formatter=plugins.get("alert_description_formatter", None)
        )

    @on(tygenie.screens.settings.SettingsScreen.SettingsUpdated)
    async def reload(self):
        self.load_plugins()
        self.refresh_bindings()
        await self.get_screen(consts.ALERTS_SCREEN_NAME).reload()

    def get_theme_variable_defaults(self) -> dict[str, str]:
        theme_config = self.get_theme(self.theme)
        if theme_config is None:
            return {}

        return {
            "open": theme_config.error or "",
            "acked": theme_config.accent or "",
            "closed": theme_config.success or "",
        }

    async def on_mount(self):
        if config.ty_config.sample_copied:
            self.push_screen(consts.SETTINGS_SCREEN_NAME)
        else:
            self.push_screen(consts.ALERTS_SCREEN_NAME)
        dn_config = config.ty_config.tygenie.get("desktop_notification", {})
        if dn_config.get("enable", True) is True:
            await self.notifier.send(
                title="Tygenie",
                message=f"Starting tygenie {consts.VERSION}",
            )
        self.theme = config.ty_config.tygenie.get("theme", "flexoki")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c", default=None)
    arguments = parser.parse_args()

    if arguments.config is not None:
        config.set_config_file(arguments.config)
        logger.reload()
        opsgenie.reload()

    app = TygenieApp()
    try:
        app.run()
    except Exception:
        pass


if __name__ == "__main__":
    main()
