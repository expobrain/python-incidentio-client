from enum import Enum


class ScheduleRotationHandoverV2RequestBodyIntervalType(str, Enum):
    DAILY = "daily"
    HOURLY = "hourly"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
