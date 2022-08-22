from enum import Enum


class IncidentsCreateRequestBodyMode(str, Enum):
    REAL = "real"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
