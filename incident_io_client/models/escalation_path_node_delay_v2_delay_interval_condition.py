from enum import Enum


class EscalationPathNodeDelayV2DelayIntervalCondition(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
