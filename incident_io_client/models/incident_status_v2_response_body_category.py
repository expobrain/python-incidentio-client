from enum import Enum


class IncidentStatusV2ResponseBodyCategory(str, Enum):
    TRIAGE = "triage"
    DECLINED = "declined"
    MERGED = "merged"
    LIVE = "live"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
