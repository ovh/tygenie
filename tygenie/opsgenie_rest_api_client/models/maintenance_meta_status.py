from enum import Enum


class MaintenanceMetaStatus(str, Enum):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    PAST = "past"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
