from enum import Enum


class IncidentsCreateRequestBodyVisibility(str, Enum):
    PUBLIC = "public"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
