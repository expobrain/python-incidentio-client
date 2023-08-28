from enum import Enum


class FollowUpsV2ListIncidentMode(str, Enum):
    STANDARD = "standard"
    RETROSPECTIVE = "retrospective"
    TEST = "test"
    TUTORIAL = "tutorial"

    def __str__(self) -> str:
        return str(self.value)
