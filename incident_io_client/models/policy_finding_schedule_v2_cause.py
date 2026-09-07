from enum import Enum


class PolicyFindingScheduleV2Cause(str, Enum):
    NOBODY_SCHEDULED = "nobody_scheduled"
    NO_ON_CALL_SEAT = "no_on_call_seat"
    USER_DEACTIVATED = "user_deactivated"

    def __str__(self) -> str:
        return str(self.value)
