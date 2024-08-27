from enum import Enum


class AlertRouteIncidentTemplateV2PrioritySeverity(str, Enum):
    SEVERITY_FIRST_WINS = "severity-first-wins"
    SEVERITY_MAX = "severity-max"

    def __str__(self) -> str:
        return str(self.value)
