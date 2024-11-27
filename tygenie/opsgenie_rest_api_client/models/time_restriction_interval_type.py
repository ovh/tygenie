from enum import Enum


class TimeRestrictionIntervalType(str, Enum):
    TIME_OF_DAY = "time-of-day"
    WEEKDAY_AND_TIME_OF_DAY = "weekday-and-time-of-day"

    def __str__(self) -> str:
        return str(self.value)
