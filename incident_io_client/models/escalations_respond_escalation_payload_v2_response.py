from enum import Enum


class EscalationsRespondEscalationPayloadV2Response(str, Enum):
    ACK = "ack"
    NACK = "nack"
    SNOOZE = "snooze"

    def __str__(self) -> str:
        return str(self.value)
