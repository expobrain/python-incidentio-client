from enum import Enum


class EscalationPathNodePayloadV2RequestBodyType(str, Enum):
    IF_ELSE = "if_else"
    LEVEL = "level"
    NOTIFY_CHANNEL = "notify_channel"
    REPEAT = "repeat"

    def __str__(self) -> str:
        return str(self.value)
