from enum import Enum


class WebhookIncidentV2ResponseBodyVisibility(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
