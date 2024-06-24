from enum import Enum


class EscalationPathNodeLevelV2ResponseBodyTimeToAckIntervalCondition(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
