from enum import Enum


class AlertV2Status(str, Enum):
    FIRING = "firing"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
