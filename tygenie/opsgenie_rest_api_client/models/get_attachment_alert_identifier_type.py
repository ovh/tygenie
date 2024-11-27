from enum import Enum


class GetAttachmentAlertIdentifierType(str, Enum):
    ALIAS = "alias"
    ID = "id"
    TINY = "tiny"

    def __str__(self) -> str:
        return str(self.value)
