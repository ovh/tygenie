from enum import Enum


class UpdateHeartbeatPayloadIntervalUnit(str, Enum):
    DAYS = "days"
    HOURS = "hours"
    MINUTES = "minutes"

    def __str__(self) -> str:
        return str(self.value)
