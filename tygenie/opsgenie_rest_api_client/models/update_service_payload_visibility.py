from enum import Enum


class UpdateServicePayloadVisibility(str, Enum):
    OPSGENIE_USERS = "OPSGENIE-USERS"
    TEAM_MEMBERS = "TEAM_MEMBERS"

    def __str__(self) -> str:
        return str(self.value)
