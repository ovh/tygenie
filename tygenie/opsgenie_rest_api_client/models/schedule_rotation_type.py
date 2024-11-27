from enum import Enum


class ScheduleRotationType(str, Enum):
    DAILY = "daily"
    HOURLY = "hourly"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
