from enum import Enum


class NotificationActionType(str, Enum):
    ACKNOWLEDGED_ALERT = "acknowledged-alert"
    ADD_NOTE = "add-note"
    ASSIGNED_ALERT = "assigned-alert"
    CLOSED_ALERT = "closed-alert"
    CREATE_ALERT = "create-alert"
    INCOMING_CALL_ROUTING = "incoming-call-routing"
    RENOTIFIED_ALERT = "renotified-alert"
    SCHEDULE_END = "schedule-end"
    SCHEDULE_START = "schedule-start"

    def __str__(self) -> str:
        return str(self.value)
