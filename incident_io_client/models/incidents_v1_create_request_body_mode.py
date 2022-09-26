from enum import Enum


class IncidentsV1CreateRequestBodyMode(str, Enum):
    REAL = "real"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
