from enum import Enum


class IncidentsV1CreateRequestBodyVisibility(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
