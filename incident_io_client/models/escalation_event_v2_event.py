from enum import Enum


class EscalationEventV2Event(str, Enum):
    ACKED = "acked"
    CANCELLED = "cancelled"
    ENTERED_GRACE_PERIOD = "entered_grace_period"
    EXPIRED = "expired"
    NOTIFIED_CHANNELS = "notified_channels"
    NOTIFIED_USERS = "notified_users"
    RESOLVED = "resolved"
    TRIGGERED = "triggered"

    def __str__(self) -> str:
        return str(self.value)
