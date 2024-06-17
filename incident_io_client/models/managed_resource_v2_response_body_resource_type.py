from enum import Enum


class ManagedResourceV2ResponseBodyResourceType(str, Enum):
    SCHEDULE = "schedule"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
