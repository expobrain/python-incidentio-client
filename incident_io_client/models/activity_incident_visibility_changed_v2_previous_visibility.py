from enum import Enum


class ActivityIncidentVisibilityChangedV2PreviousVisibility(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
