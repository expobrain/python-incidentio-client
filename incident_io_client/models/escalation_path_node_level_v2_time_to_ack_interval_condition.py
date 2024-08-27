from enum import Enum


class EscalationPathNodeLevelV2TimeToAckIntervalCondition(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
