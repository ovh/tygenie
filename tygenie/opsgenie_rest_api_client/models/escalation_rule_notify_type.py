from enum import Enum


class EscalationRuleNotifyType(str, Enum):
    ADMINS = "admins"
    ALL = "all"
    DEFAULT = "default"
    NEXT = "next"
    PREVIOUS = "previous"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
