from enum import Enum


class EscalationPathTargetV2RequestBodyType(str, Enum):
    SCHEDULE = "schedule"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
