from enum import Enum


class ListNotesIdentifierType(str, Enum):
    ALIAS = "alias"
    ID = "id"
    TINY = "tiny"

    def __str__(self) -> str:
        return str(self.value)
