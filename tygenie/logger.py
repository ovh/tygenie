import pendulum
from textual import log
from tygenie.config import ty_config


class Logger:

    def __init__(self):
        self.config = ty_config.tygenie.get(
            "log", {"enable": False, "file": "/tmp/tygenie.log"}
        )
        self.enable = self.config["enable"]
        self.file = self.config["file"]

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
