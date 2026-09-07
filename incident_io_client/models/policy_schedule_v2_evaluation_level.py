from enum import Enum


class PolicyScheduleV2EvaluationLevel(str, Enum):
    ROTATION = "rotation"
    SCHEDULE = "schedule"

    def __str__(self) -> str:
        return str(self.value)
