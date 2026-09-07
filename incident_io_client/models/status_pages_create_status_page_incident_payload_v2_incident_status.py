from enum import Enum


class StatusPagesCreateStatusPageIncidentPayloadV2IncidentStatus(str, Enum):
    IDENTIFIED = "identified"
    INVESTIGATING = "investigating"
    MONITORING = "monitoring"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
