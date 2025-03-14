from enum import Enum


class DeprecatedNotificationDeduplicationAlertPolicyDeduplicationActionType(str, Enum):
    FREQUENCY_BASED = "frequency-based"
    VALUE_BASED = "value-based"

    def __str__(self) -> str:
        return str(self.value)
