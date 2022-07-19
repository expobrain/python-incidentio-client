from enum import Enum


class IncidentsCreateRequestBodyStatus(str, Enum):
    TRIAGE = "triage"
    INVESTIGATING = "investigating"
    FIXING = "fixing"
    MONITORING = "monitoring"
    CLOSED = "closed"
    DECLINED = "declined"

    def __str__(self) -> str:
        return str(self.value)
