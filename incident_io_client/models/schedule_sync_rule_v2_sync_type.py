from enum import Enum


class ScheduleSyncRuleV2SyncType(str, Enum):
    ALL_USERS = "all_users"
    NEXT_ON_CALL = "next_on_call"
    ON_CALL = "on_call"

    def __str__(self) -> str:
        return str(self.value)
