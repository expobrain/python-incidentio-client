from enum import Enum


class StatusPageIncidentComponentImpactV2ComponentStatus(str, Enum):
    DEGRADED_PERFORMANCE = "degraded_performance"
    FULL_OUTAGE = "full_outage"
    PARTIAL_OUTAGE = "partial_outage"

    def __str__(self) -> str:
        return str(self.value)
