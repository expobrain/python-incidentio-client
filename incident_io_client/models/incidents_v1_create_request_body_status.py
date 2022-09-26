from enum import Enum


class IncidentsV1CreateRequestBodyStatus(str, Enum):
    TRIAGE = "triage"
    INVESTIGATING = "investigating"
    FIXING = "fixing"
    MONITORING = "monitoring"
    CLOSED = "closed"
    DECLINED = "declined"

    def __str__(self) -> str:
        return str(self.value)
