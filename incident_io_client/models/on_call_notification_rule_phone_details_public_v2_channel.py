from enum import Enum


class OnCallNotificationRulePhoneDetailsPublicV2Channel(str, Enum):
    SMS = "sms"
    VOICE = "voice"

    def __str__(self) -> str:
        return str(self.value)
