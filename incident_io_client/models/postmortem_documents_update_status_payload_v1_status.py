from enum import Enum


class PostmortemDocumentsUpdateStatusPayloadV1Status(str, Enum):
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    IN_REVIEW = "in_review"

    def __str__(self) -> str:
        return str(self.value)
