from enum import Enum


class AuditLogPrivateIncidentAccessAttemptedMetadataV2ResponseBodyOutcome(str, Enum):
    GRANTED = "granted"
    DENIED = "denied"

    def __str__(self) -> str:
        return str(self.value)
