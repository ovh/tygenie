from enum import Enum


class DeprecatedNotificationDelayAlertPolicyDelayOption(str, Enum):
    FOR_DURATION = "for-duration"
    NEXT_FRIDAY = "next-friday"
    NEXT_MONDAY = "next-monday"
    NEXT_SATURDAY = "next-saturday"
    NEXT_SUNDAY = "next-sunday"
    NEXT_THURSDAY = "next-thursday"
    NEXT_TIME = "next-time"
    NEXT_TUESDAY = "next-tuesday"
    NEXT_WEDNESDAY = "next-wednesday"
    NEXT_WEEKDAY = "next-weekday"

    def __str__(self) -> str:
        return str(self.value)
