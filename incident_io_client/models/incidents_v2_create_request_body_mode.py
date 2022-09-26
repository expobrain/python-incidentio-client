from enum import Enum


class IncidentsV2CreateRequestBodyMode(str, Enum):
    STANDARD = "standard"
    RETROSPECTIVE = "retrospective"
    TEST = "test"
    TUTORIAL = "tutorial"

    def __str__(self) -> str:
        return str(self.value)
