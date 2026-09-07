from enum import Enum


class EscalationUserResponseOptionsV2AvailableActionsItem(str, Enum):
    ACK = "ack"
    NACK = "nack"
    SNOOZE = "snooze"

    def __str__(self) -> str:
        return str(self.value)
