from enum import Enum


class DeprecatedAlertPolicyType(str, Enum):
    AUTO_CLOSE = "auto-close"
    AUTO_RESTART_NOTIFICATIONS = "auto-restart-notifications"
    MODIFY = "modify"
    NOTIFICATION_DEDUPLICATION = "notification-deduplication"
    NOTIFICATION_DELAY = "notification-delay"
    NOTIFICATION_RENOTIFY = "notification-renotify"
    NOTIFICATION_SUPPRESS = "notification-suppress"

    def __str__(self) -> str:
        return str(self.value)
