from enum import Enum


class DurationTimeUnit(str, Enum):
    DAYS = "days"
    HOURS = "hours"
    MICROS = "micros"
    MILISECONDS = "miliseconds"
    MINUTES = "minutes"
    NANOS = "nanos"
    SECONDS = "seconds"

    def __str__(self) -> str:
        return str(self.value)
