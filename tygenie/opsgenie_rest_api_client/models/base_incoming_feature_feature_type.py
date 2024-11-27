from enum import Enum


class BaseIncomingFeatureFeatureType(str, Enum):
    EMAIL_BASED = "email-based"
    TOKEN_BASED = "token-based"

    def __str__(self) -> str:
        return str(self.value)
