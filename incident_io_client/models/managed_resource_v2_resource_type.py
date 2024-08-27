from enum import Enum


class ManagedResourceV2ResourceType(str, Enum):
    SCHEDULE = "schedule"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
