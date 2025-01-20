from enum import Enum


class ManagedResourcesV2CreateManagedResourceRequestBodyResourceType(str, Enum):
    ESCALATION_PATH = "escalation_path"
    SCHEDULE = "schedule"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
