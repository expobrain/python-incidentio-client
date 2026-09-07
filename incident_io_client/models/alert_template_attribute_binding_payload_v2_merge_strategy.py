from enum import Enum


class AlertTemplateAttributeBindingPayloadV2MergeStrategy(str, Enum):
    APPEND = "append"
    FIRST_WINS = "first_wins"
    LAST_WINS = "last_wins"
    MAX = "max"
    MIN = "min"

    def __str__(self) -> str:
        return str(self.value)
