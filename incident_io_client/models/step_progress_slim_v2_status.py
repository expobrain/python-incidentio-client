from enum import Enum


class StepProgressSlimV2Status(str, Enum):
    COMPLETE = "complete"
    ERROR = "error"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
