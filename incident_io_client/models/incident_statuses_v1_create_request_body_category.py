from enum import Enum


class IncidentStatusesV1CreateRequestBodyCategory(str, Enum):
    CLOSED = "closed"
    LEARNING = "learning"
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
