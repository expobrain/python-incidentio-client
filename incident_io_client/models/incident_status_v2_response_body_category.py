from enum import Enum


class IncidentStatusV2ResponseBodyCategory(str, Enum):
    TRIAGE = "triage"
    DECLINED = "declined"
    MERGED = "merged"
    CANCELED = "canceled"
    LIVE = "live"
    LEARNING = "learning"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
