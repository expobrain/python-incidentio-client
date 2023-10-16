from enum import Enum


class IncidentV2ResponseBodyVisibility(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
