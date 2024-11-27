from enum import Enum


class AssignAlertIdentifierType(str, Enum):
    ALIAS = "alias"
    ID = "id"
    TINY = "tiny"

    def __str__(self) -> str:
        return str(self.value)
