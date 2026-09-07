from enum import Enum


class PolicyFindingV2State(str, Enum):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    DISMISSED = "dismissed"
    PENDING = "pending"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
