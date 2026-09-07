from enum import Enum


class EscalationPathNodeLevelV2AckMode(str, Enum):
    ALL = "all"
    FIRST = "first"

    def __str__(self) -> str:
        return str(self.value)
