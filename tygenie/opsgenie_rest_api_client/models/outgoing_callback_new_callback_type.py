from enum import Enum


class OutgoingCallbackNewCallbackType(str, Enum):
    AMAZON_SNS_CALLBACK = "amazon-sns-callback"
    BASE_WEBHOOK_CALLBACK = "base-webhook-callback"
    BIDIRECTIONAL_CALLBACK_NEW = "bidirectional-callback-new"
    BMC_REMEDY_ON_DEMAND_CALLBACK = "bmc-remedy-on-demand-callback"
    OEC_CALLBACK = "oec-callback"

    def __str__(self) -> str:
        return str(self.value)
