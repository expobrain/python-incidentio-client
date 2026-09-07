from enum import Enum


class OnCallNotificationMethodPublicV2MethodType(str, Enum):
    APP = "app"
    EMAIL = "email"
    MICROSOFT_TEAMS = "microsoft_teams"
    PHONE = "phone"
    SLACK = "slack"
    WHATSAPP_MESSAGE = "whatsapp_message"

    def __str__(self) -> str:
        return str(self.value)
