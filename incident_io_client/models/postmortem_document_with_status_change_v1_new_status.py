from enum import Enum


class PostmortemDocumentWithStatusChangeV1NewStatus(str, Enum):
    COMPLETE = "complete"
    CREATED = "created"
    NOT_STARTED = "not_started"
    REVIEW = "review"

    def __str__(self) -> str:
        return str(self.value)
