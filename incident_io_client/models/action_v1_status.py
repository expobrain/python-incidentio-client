from enum import Enum


class ActionV1Status(str, Enum):
    COMPLETED = "completed"
    DELETED = "deleted"
    NOT_DOING = "not_doing"
    OUTSTANDING = "outstanding"

    def __str__(self) -> str:
        return str(self.value)
