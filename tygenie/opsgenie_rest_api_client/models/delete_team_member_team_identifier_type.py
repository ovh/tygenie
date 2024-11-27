from enum import Enum


class DeleteTeamMemberTeamIdentifierType(str, Enum):
    ID = "id"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
