from enum import Enum


class ActionResponseBodyStatus(str, Enum):
    OUTSTANDING = "outstanding"
    COMPLETED = "completed"
    DELETED = "deleted"
    NOT_DOING = "not_doing"

    def __str__(self) -> str:
        return str(self.value)
