from enum import Enum


class WorkflowSlimRunsOnIncidentModesItem(str, Enum):
    RETROSPECTIVE = "retrospective"
    STANDARD = "standard"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
