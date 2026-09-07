from enum import Enum


class OnCallNotificationRuleAppDetailsPublicV2PushNotificationCriticality(str, Enum):
    ACTIVE = "active"
    CRITICAL = "critical"

    def __str__(self) -> str:
        return str(self.value)
