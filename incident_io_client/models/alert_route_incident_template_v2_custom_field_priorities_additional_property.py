from enum import Enum


class AlertRouteIncidentTemplateV2CustomFieldPrioritiesAdditionalProperty(str, Enum):
    APPEND = "append"
    FIRST_WINS = "first-wins"
    LAST_WINS = "last-wins"

    def __str__(self) -> str:
        return str(self.value)
