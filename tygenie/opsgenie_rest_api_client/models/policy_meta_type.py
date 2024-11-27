from enum import Enum


class PolicyMetaType(str, Enum):
    ALERT = "alert"
    NOTIFICATION = "notification"

    def __str__(self) -> str:
        return str(self.value)
