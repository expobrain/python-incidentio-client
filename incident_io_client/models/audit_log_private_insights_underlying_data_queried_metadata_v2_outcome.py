from enum import Enum


class AuditLogPrivateInsightsUnderlyingDataQueriedMetadataV2Outcome(str, Enum):
    DENIED = "denied"
    GRANTED = "granted"

    def __str__(self) -> str:
        return str(self.value)
