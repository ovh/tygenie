import json
import os
import pathlib
import shutil
from collections import OrderedDict

CONFIG_DIR = pathlib.Path.home() / ".config" / "tygenie"
CONFIG_FILE = "tygenie.json"
CONFIG_PATH = CONFIG_DIR / CONFIG_FILE
SAMPLE_CONFIG = f"{os.path.dirname(__file__)}/assets/tygenie.json"


class Config:
    def __init__(self, config_path: pathlib.Path | str = CONFIG_PATH):
        self.config_dir: pathlib.Path = CONFIG_DIR
        self.config_file: str = CONFIG_FILE
        self._config_path: pathlib.Path = pathlib.Path(config_path)
        self.config: dict = {}
        self.tygenie: dict = {}
        self.opsgenie: dict = {}
        self.sample_copied: bool = False

        super().__init__()
        self.__init__config()
        self.auto_update()

    @property
    def config_path(self):
        return self._config_path

    @config_path.setter
    def config_path(self, value: pathlib.Path | str = CONFIG_PATH):
        if isinstance(value, str):
            value = pathlib.Path(value)

        self._config_path = value

    def __init__config(self):
        os.makedirs(self.config_dir, exist_ok=True)
        if not os.path.exists(self.config_path):
            shutil.copyfile(SAMPLE_CONFIG, self.config_path)
            self.sample_copied = True

    def _load_config(self):
        self.tygenie = self.config.get("tygenie", {})
        self.opsgenie = self.config.get("opsgenie", {})

    def load(self):
        with open(self.config_path, "r") as conf:
            self.config = json.load(conf, object_pairs_hook=OrderedDict)

        self._load_config()

    def reload(self):
        self.load()

    def save(self, config):
        with open(self.config_path, "w") as conf:
            conf.write(json.dumps(config, indent=2))

        self.config = config
        self._load_config()

    def auto_update(self):
        """This method automatically update deprecated parameters"""

        self.load()

        # Update desktop notification parmeters, was "notify" before "desktop_notification"
        notify = self.config.get("tygenie", {}).get("notify", None)
        dn = self.config.get("tygenie", {}).get("desktop_notification", {})
        dn_urgency = self.config.get("tygenie", {}).get(
            "desktop_notification_urgency", "Critical"
        )
        # In case we have notify but desktop_notification parameter we force dn to
        # be notify value to pass in the next if
        if notify is not None and dn == {}:
            dn = notify

        if type(dn) is bool:  # either we have notify or the depreccated bool value
            new_dn = {
                "enable": dn,
                "urgency": dn_urgency,
                "when_on_call_only": False,
            }
            self.config.get("tygenie", {})["desktop_notification"] = new_dn
            for key in ["notify", "desktop_notification_urgency"]:
                self.config.get("tygenie", {}).pop(key, None)

        # Update deprecated plugins parameters
        plugins = self.config.get("tygenie", {})["plugins"]
        if (
            "alerts_list_formatter" not in plugins
            and "alert_description_formatter" not in plugins
        ):

            new_plugins_config = {
                "alerts_list_formatter": plugins.get("alert_formatter", None),
                "alert_description_formatter": plugins.get("content_transformer", None),
            }
            self.config.get("tygenie", {})["plugins"] = new_plugins_config

        # Add theme parameter config
        self.config.get("tygenie", {})["theme"] = self.config.get("tygenie", {}).get(
            "theme", "flexoki"
        )

        # Add palette keybinding
        self.config.get("tygenie", {}).get("keybindings", {})["palette"] = (
            self.config.get("tygenie", {})
            .get("keybindings", {})
            .get("palette", "ctrl+p")
        )

        # Add displayed_field as a key/value structure
        self.config.get("tygenie", {})["displayed_fields"] = self.config.get(
            "tygenie", {}
        ).get("displayed_fields", {})

        self.save(self.config)


ty_config = Config()
ty_config.load()


def set_config_file(config_file):
    global ty_config
    ty_config = Config(config_path=config_file)
    ty_config.load()
