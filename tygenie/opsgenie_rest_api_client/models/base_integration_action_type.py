from enum import Enum


class BaseIntegrationActionType(str, Enum):
    ACKNOWLEDGE = "acknowledge"
    ADDNOTE = "addNote"
    CLOSE = "close"
    CREATE = "create"
    IGNORE = "ignore"

    def __str__(self) -> str:
        return str(self.value)
