from enum import Enum


class IncidentTemplateCustomFieldBindingPayloadV1MergeStrategy(str, Enum):
    APPEND = "append"
    FIRST_WINS = "first-wins"
    LAST_WINS = "last-wins"

    def __str__(self) -> str:
        return str(self.value)
