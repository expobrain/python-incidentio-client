from enum import Enum


class StepProgressSlimV2WebhookDeliveryState(str, Enum):
    AVAILABLE = "available"
    EXPIRED = "expired"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
