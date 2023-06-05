from enum import Enum


class IncidentStatusesV1CreateRequestBodyCategory(str, Enum):
    LIVE = "live"
    LEARNING = "learning"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
