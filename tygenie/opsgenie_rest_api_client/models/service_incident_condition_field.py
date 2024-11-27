from enum import Enum


class ServiceIncidentConditionField(str, Enum):
    DESCRIPTION = "description"
    EXTRA_PROPERTIES = "extra-properties"
    MESSAGE = "message"
    PRIORITY = "priority"
    RECIPIENTS = "recipients"
    TAGS = "tags"
    TEAMS = "teams"

    def __str__(self) -> str:
        return str(self.value)
