from enum import Enum


class OnCallNotificationRuleMethodTargetPublicV2Type(str, Enum):
    ALL = "all"
    SPECIFIC = "specific"

    def __str__(self) -> str:
        return str(self.value)
