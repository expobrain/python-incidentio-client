from enum import Enum


class ActionsListIncidentMode(str, Enum):
    REAL = "real"
    TEST = "test"
    TUTORIAL = "tutorial"

    def __str__(self) -> str:
        return str(self.value)
