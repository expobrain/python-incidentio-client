from enum import Enum


class ActionsV2ListIncidentMode(str, Enum):
    RETROSPECTIVE = "retrospective"
    STANDARD = "standard"
    STREAM = "stream"
    TEST = "test"
    TUTORIAL = "tutorial"

    def __str__(self) -> str:
        return str(self.value)
