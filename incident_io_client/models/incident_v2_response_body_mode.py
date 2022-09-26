from enum import Enum


class IncidentV2ResponseBodyMode(str, Enum):
    STANDARD = "standard"
    RETROSPECTIVE = "retrospective"
    TEST = "test"
    TUTORIAL = "tutorial"

    def __str__(self) -> str:
        return str(self.value)
