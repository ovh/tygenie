from enum import Enum


class ContactMetaMethod(str, Enum):
    EMAIL = "email"
    MOBILE = "mobile"
    SMS = "sms"
    VOICE = "voice"

    def __str__(self) -> str:
        return str(self.value)
