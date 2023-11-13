from enum import Enum


class AlertEventsV2CreateHTTPResponseBodyStatus(str, Enum):
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
