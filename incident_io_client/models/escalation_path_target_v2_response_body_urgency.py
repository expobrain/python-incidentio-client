from enum import Enum


class EscalationPathTargetV2ResponseBodyUrgency(str, Enum):
    HIGH = "high"
    LOW = "low"

    def __str__(self) -> str:
        return str(self.value)
