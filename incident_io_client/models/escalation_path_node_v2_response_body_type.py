from enum import Enum


class EscalationPathNodeV2ResponseBodyType(str, Enum):
    IF_ELSE = "if_else"
    LEVEL = "level"
    REPEAT = "repeat"

    def __str__(self) -> str:
        return str(self.value)
