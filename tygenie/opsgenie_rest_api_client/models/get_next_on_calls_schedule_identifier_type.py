from enum import Enum


class GetNextOnCallsScheduleIdentifierType(str, Enum):
    ID = "id"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
