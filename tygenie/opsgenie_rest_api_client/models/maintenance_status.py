from enum import Enum


class MaintenanceStatus(str, Enum):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    PAST = "past"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
