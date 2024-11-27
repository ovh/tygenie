from enum import Enum


class CreateContactPayloadMethod(str, Enum):
    EMAIL = "email"
    MOBILE = "mobile"
    SMS = "sms"
    VOICE = "voice"

    def __str__(self) -> str:
        return str(self.value)
