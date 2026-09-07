from enum import Enum


class PolicyDueDateConfigPayloadV2CalculationType(str, Enum):
    SEVEN_DAYS = "seven_days"
    WEEKDAYS = "weekdays"

    def __str__(self) -> str:
        return str(self.value)
