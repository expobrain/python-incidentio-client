from enum import Enum


class IncidentTimestampV2ResponseBodySetOnVisit(str, Enum):
    VALUE_0 = ""
    FIRST = "first"
    LAST = "last"

    def __str__(self) -> str:
        return str(self.value)
