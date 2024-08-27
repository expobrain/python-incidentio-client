from enum import Enum


class ScheduleRotationWorkingIntervalV2Weekday(str, Enum):
    FRIDAY = "friday"
    MONDAY = "monday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    THURSDAY = "thursday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"

    def __str__(self) -> str:
        return str(self.value)
