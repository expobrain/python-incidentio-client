from enum import Enum


class AuditLogPrivateIncidentAccessAttemptedMetadataV2ResponseBodyOutcome(str, Enum):
    DENIED = "denied"
    GRANTED = "granted"

    def __str__(self) -> str:
        return str(self.value)
