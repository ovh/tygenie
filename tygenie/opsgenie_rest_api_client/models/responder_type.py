from enum import Enum


class ResponderType(str, Enum):
    ESCALATION = "escalation"
    SCHEDULE = "schedule"
    TEAM = "team"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
