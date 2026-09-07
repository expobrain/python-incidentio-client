from enum import Enum


class WorkflowsUpdateWorkflowPayloadV2RunsOnIncidentModesItem(str, Enum):
    RETROSPECTIVE = "retrospective"
    STANDARD = "standard"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
