from enum import Enum


class NotifyTime(str, Enum):
    JUST_BEFORE = "just-before"
    VALUE_1 = "15-minutes-ago"
    VALUE_2 = "1-hour-ago"
    VALUE_3 = "1-day-ago"

    def __str__(self) -> str:
        return str(self.value)
