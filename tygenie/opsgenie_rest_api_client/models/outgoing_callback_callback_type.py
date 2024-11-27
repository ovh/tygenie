from enum import Enum


class OutgoingCallbackCallbackType(str, Enum):
    BIDIRECTIONAL_CALLBACK = "bidirectional-callback"
    CAMPFIRE_CALLBACK = "campfire-callback"
    FLOWDOCK_CALLBACK = "flowdock-callback"
    FLOWDOCK_V2_CALLBACK = "flowdock-v2-callback"
    PLANIO_CALLBACK = "planio-callback"

    def __str__(self) -> str:
        return str(self.value)
