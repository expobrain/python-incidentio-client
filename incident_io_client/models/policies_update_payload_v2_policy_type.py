from enum import Enum


class PoliciesUpdatePayloadV2PolicyType(str, Enum):
    DEBRIEF = "debrief"
    FOLLOW_UP = "follow_up"
    ON_CALL_READINESS = "on_call_readiness"
    POST_MORTEM = "post_mortem"
    SCHEDULE = "schedule"
    VACATION_CONFLICT = "vacation_conflict"

    def __str__(self) -> str:
        return str(self.value)
