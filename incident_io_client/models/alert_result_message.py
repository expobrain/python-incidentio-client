from enum import Enum


class AlertResultMessage(str, Enum):
    EVENT_ACCEPTED_FOR_PROCESSING = "Event accepted for processing"

    def __str__(self) -> str:
        return str(self.value)
