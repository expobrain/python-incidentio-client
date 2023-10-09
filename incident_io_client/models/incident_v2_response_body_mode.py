from enum import Enum


class IncidentV2ResponseBodyMode(str, Enum):
    RETROSPECTIVE = "retrospective"
    STANDARD = "standard"
    TEST = "test"
    TUTORIAL = "tutorial"

    def __str__(self) -> str:
        return str(self.value)
