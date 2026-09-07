from enum import Enum


class AlertsTransitionIncidentAlertPayloadV2State(str, Enum):
    RELATED = "related"
    UNRELATED = "unrelated"

    def __str__(self) -> str:
        return str(self.value)
