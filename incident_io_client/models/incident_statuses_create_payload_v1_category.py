from enum import Enum


class IncidentStatusesCreatePayloadV1Category(str, Enum):
    CLOSED = "closed"
    LEARNING = "learning"
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
