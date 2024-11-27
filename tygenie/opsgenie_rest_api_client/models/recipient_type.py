from enum import Enum


class RecipientType(str, Enum):
    ALL = "all"
    ESCALATION = "escalation"
    GROUP = "group"
    NONE = "none"
    SCHEDULE = "schedule"
    TEAM = "team"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
