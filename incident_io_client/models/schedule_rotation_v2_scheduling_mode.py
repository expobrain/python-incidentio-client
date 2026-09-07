from enum import Enum


class ScheduleRotationV2SchedulingMode(str, Enum):
    FAIR = "fair"
    SEQUENTIAL = "sequential"

    def __str__(self) -> str:
        return str(self.value)
