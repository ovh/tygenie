from enum import Enum


class ConditionField(str, Enum):
    ACTIONS = "actions"
    ALIAS = "alias"
    DESCRIPTION = "description"
    DETAILS = "details"
    ENTITY = "entity"
    EXTRA_PROPERTIES = "extra-properties"
    MESSAGE = "message"
    PRIORITY = "priority"
    RECIPIENTS = "recipients"
    SOURCE = "source"
    TAGS = "tags"
    TEAMS = "teams"

    def __str__(self) -> str:
        return str(self.value)
