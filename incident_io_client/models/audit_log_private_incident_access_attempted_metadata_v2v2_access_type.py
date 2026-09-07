from enum import Enum


class AuditLogPrivateIncidentAccessAttemptedMetadataV2V2AccessType(str, Enum):
    DIRECT_MEMBERSHIP = "direct_membership"
    GLOBAL_ACCESS = "global_access"
    NA = "N/A"
    TEAM_MEMBERSHIP = "team_membership"

    def __str__(self) -> str:
        return str(self.value)
