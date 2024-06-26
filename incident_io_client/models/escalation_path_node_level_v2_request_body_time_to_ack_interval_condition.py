from enum import Enum


class EscalationPathNodeLevelV2RequestBodyTimeToAckIntervalCondition(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
