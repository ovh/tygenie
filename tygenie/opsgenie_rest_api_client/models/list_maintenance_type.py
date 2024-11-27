from enum import Enum


class ListMaintenanceType(str, Enum):
    ALL = "all"
    NON_EXPIRED = "non-expired"
    PAST = "past"

    def __str__(self) -> str:
        return str(self.value)
