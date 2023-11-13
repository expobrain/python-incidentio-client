from enum import Enum


class AlertEventsV2CreateHTTPResponseBodyDeduplicationKey(str, Enum):
    UNIQUE_KEY = "unique-key"

    def __str__(self) -> str:
        return str(self.value)
