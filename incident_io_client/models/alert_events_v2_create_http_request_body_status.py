from enum import Enum


class AlertEventsV2CreateHTTPRequestBodyStatus(str, Enum):
    FIRING = "firing"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
