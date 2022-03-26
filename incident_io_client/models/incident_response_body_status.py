from enum import Enum


class IncidentResponseBodyStatus(str, Enum):
    INVESTIGATING = "investigating"
    FIXING = "fixing"
    MONITORING = "monitoring"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
