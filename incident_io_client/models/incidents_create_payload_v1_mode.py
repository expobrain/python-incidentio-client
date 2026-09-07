from enum import Enum


class IncidentsCreatePayloadV1Mode(str, Enum):
    REAL = "real"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
