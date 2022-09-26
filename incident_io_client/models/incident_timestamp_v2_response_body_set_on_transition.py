from enum import Enum


class IncidentTimestampV2ResponseBodySetOnTransition(str, Enum):
    VALUE_0 = ""
    ENTER = "enter"
    LEAVE = "leave"

    def __str__(self) -> str:
        return str(self.value)
