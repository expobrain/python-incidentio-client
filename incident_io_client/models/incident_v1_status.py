from enum import Enum


class IncidentV1Status(str, Enum):
    CLOSED = "closed"
    DECLINED = "declined"
    FIXING = "fixing"
    INVESTIGATING = "investigating"
    MONITORING = "monitoring"
    TRIAGE = "triage"

    def __str__(self) -> str:
        return str(self.value)
