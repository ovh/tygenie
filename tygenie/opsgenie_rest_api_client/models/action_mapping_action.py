from enum import Enum


class ActionMappingAction(str, Enum):
    ACKNOWLEDGE = "acknowledge"
    ADD_NOTE = "add-note"
    ADD_RESPONDER = "add-responder"
    ADD_TAGS = "add-tags"
    ASSIGN_OWNERSHIP = "assign-ownership"
    CLOSE = "close"
    CREATE = "create"
    CUSTOM_ACTION = "custom-action"
    DELETE = "delete"
    ESCALATE = "escalate"
    ESCALATE_TO_NEXT = "escalate-to-next"
    REMOVE_TAGS = "remove-tags"
    SNOOZE = "snooze"
    TAKE_OWNERSHIP = "take-ownership"
    UNACKNOWLEDGE = "unacknowledge"
    UPDATE_DESCRIPTION = "update-description"
    UPDATE_MESSAGE = "update-message"
    UPDATE_PRIORITY = "update-priority"

    def __str__(self) -> str:
        return str(self.value)
