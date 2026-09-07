from enum import Enum


class WorkflowsCreateWorkflowPayloadV2PrivateIncidentScope(str, Enum):
    ALL = "all"
    NONE = "none"
    OWNING_TEAMS = "owning_teams"

    def __str__(self) -> str:
        return str(self.value)
