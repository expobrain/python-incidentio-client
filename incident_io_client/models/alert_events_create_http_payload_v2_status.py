from enum import Enum


class AlertEventsCreateHTTPPayloadV2Status(str, Enum):
    FIRING = "firing"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
