from enum import Enum


class ListIncidentsSort(str, Enum):
    CREATEDAT = "createdAt"
    ISSEEN = "isSeen"
    MESSAGE = "message"
    OWNER = "owner"
    STATUS = "status"
    TINYID = "tinyId"

    def __str__(self) -> str:
        return str(self.value)
