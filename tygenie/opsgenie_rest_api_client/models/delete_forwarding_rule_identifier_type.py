from enum import Enum


class DeleteForwardingRuleIdentifierType(str, Enum):
    ALIAS = "alias"
    ID = "id"

    def __str__(self) -> str:
        return str(self.value)
