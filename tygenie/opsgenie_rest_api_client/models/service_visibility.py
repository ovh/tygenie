from enum import Enum


class ServiceVisibility(str, Enum):
    OPSGENIE_USERS = "OPSGENIE_USERS"
    TEAM_MEMBERS = "TEAM_MEMBERS"

    def __str__(self) -> str:
        return str(self.value)
