from enum import Enum


class AlertRouteSeverityBindingPayloadV2MergeStrategy(str, Enum):
    FIRST_WINS = "first-wins"
    MAX = "max"

    def __str__(self) -> str:
        return str(self.value)
