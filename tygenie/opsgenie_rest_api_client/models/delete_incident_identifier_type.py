from enum import Enum


class DeleteIncidentIdentifierType(str, Enum):
    ID = "id"
    TINY = "tiny"

    def __str__(self) -> str:
        return str(self.value)
