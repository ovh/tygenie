import pendulum
from textual import log

import tygenie.config as config


class Logger:

    def __init__(self):
        self._load_config()

    def _load_config(self):
        self.enable = config.ty_config.tygenie.get("log", {}).get("enable", False)
        self.file = config.ty_config.tygenie.get("log", {}).get(
            "file", "/tmp/tygenie.log"
        )

    def log(self, message: str = ""):
        if not message or not self.enable:
            return

        date = pendulum.now()
        logline = f"[{date}] {message}"
        # Logline visble in textual console: textual console -vvv
        # and run app.py file with textual run app.py --dev
        log(f"{logline}")
        try:
            with open(self.file, "a") as f:
                f.write(logline + "\n")
        except Exception as e:
            log(f"Unable to log in file: {e}")
            pass


logger = Logger()


def reload():
    global logger
    logger = Logger()
