from enum import Enum


class ScheduleRotationWorkingIntervalCreatePayloadV2RequestBodyWeekday(str, Enum):
    FRIDAY = "friday"
    MONDAY = "monday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    THURSDAY = "thursday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"

    def __str__(self) -> str:
        return str(self.value)
