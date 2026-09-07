from enum import Enum


class OnCallNotificationRulePublicV2RuleType(str, Enum):
    HIGH_URGENCY = "high_urgency"
    LOW_URGENCY = "low_urgency"

    def __str__(self) -> str:
        return str(self.value)
