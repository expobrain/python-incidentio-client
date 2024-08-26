from enum import Enum


class EscalationPathTargetV2ScheduleMode(str, Enum):
    ALL_USERS = "all_users"
    ALL_USERS_FOR_ROTA = "all_users_for_rota"
    CURRENTLY_ON_CALL = "currently_on_call"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
