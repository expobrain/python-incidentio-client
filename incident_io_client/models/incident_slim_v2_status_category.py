from enum import Enum


class IncidentSlimV2StatusCategory(str, Enum):
    ACTIVE = "active"
    CANCELED = "canceled"
    CLOSED = "closed"
    DECLINED = "declined"
    MERGED = "merged"
    PAUSED = "paused"
    POST_INCIDENT = "post-incident"
    TRIAGE = "triage"

    def __str__(self) -> str:
        return str(self.value)
