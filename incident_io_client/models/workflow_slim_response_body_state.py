from enum import Enum


class WorkflowSlimResponseBodyState(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    DISABLED_DRAFT = "disabled_draft"
    DRAFT = "draft"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
