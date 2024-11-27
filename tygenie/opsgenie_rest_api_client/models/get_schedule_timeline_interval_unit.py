from enum import Enum


class GetScheduleTimelineIntervalUnit(str, Enum):
    DAYS = "days"
    MONTHS = "months"
    WEEKS = "weeks"

    def __str__(self) -> str:
        return str(self.value)
