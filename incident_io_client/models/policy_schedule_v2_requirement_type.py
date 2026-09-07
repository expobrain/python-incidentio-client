from enum import Enum


class PolicyScheduleV2RequirementType(str, Enum):
    CONTIGUOUS = "contiguous"

    def __str__(self) -> str:
        return str(self.value)
