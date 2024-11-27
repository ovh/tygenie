from enum import Enum


class BaseWebhookCallbackBaseWebhookCallbackType(str, Enum):
    FLOCK_CALLBACK = "flock-callback"
    KORE_CALLBACK = "kore-callback"
    MOXTRA_CALLBACK = "moxtra-callback"
    RING_CENTRAL_GLIP_CALLBACK = "ring-central-glip-callback"
    STATUSY_CALLBACK = "statusy-callback"
    WEBHOOK_CALLBACK = "webhook-callback"

    def __str__(self) -> str:
        return str(self.value)
