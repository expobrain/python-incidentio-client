from enum import Enum


class IncidentStatusV2ResponseBodyCategory(str, Enum):
    CANCELED = "canceled"
    CLOSED = "closed"
    DECLINED = "declined"
    LEARNING = "learning"
    LIVE = "live"
    MERGED = "merged"
    PAUSED = "paused"
    TRIAGE = "triage"

    def __str__(self) -> str:
        return str(self.value)
