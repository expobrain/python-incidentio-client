from enum import Enum


class PolicyOnCallReadinessV2Enforcement(str, Enum):
    ADVISORY = "advisory"
    BLOCKING = "blocking"

    def __str__(self) -> str:
        return str(self.value)
