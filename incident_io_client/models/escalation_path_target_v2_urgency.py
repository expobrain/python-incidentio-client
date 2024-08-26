from enum import Enum


class EscalationPathTargetV2Urgency(str, Enum):
    HIGH = "high"
    LOW = "low"

    def __str__(self) -> str:
        return str(self.value)
