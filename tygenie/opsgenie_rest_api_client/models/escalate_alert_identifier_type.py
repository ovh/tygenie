from enum import Enum


class EscalateAlertIdentifierType(str, Enum):
    ALIAS = "alias"
    ID = "id"
    TINY = "tiny"

    def __str__(self) -> str:
        return str(self.value)
