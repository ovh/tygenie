from enum import Enum


class MaintenanceEntityType(str, Enum):
    INTEGRATION = "integration"
    POLICY = "policy"

    def __str__(self) -> str:
        return str(self.value)
