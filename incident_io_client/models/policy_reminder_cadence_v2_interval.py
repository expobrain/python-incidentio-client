from enum import Enum


class PolicyReminderCadenceV2Interval(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
