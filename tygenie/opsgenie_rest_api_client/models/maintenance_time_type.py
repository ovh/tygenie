from enum import Enum


class MaintenanceTimeType(str, Enum):
    FOR_1_HOUR = "for-1-hour"
    FOR_30_MINUTES = "for-30-minutes"
    FOR_5_MINUTES = "for-5-minutes"
    INDEFINITELY = "indefinitely"
    SCHEDULE = "schedule"

    def __str__(self) -> str:
        return str(self.value)
