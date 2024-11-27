from enum import Enum


class GetIncidentIdentifierType(str, Enum):
    ID = "id"
    TINY = "tiny"

    def __str__(self) -> str:
        return str(self.value)
