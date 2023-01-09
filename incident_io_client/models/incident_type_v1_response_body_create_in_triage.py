from enum import Enum


class IncidentTypeV1ResponseBodyCreateInTriage(str, Enum):
    ALWAYS = "always"
    OPTIONAL = "optional"

    def __str__(self) -> str:
        return str(self.value)
