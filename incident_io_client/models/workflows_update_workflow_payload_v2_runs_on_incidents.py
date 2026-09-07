from enum import Enum


class WorkflowsUpdateWorkflowPayloadV2RunsOnIncidents(str, Enum):
    NEWLY_CREATED = "newly_created"
    NEWLY_CREATED_AND_ACTIVE = "newly_created_and_active"

    def __str__(self) -> str:
        return str(self.value)
