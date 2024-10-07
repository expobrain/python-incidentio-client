from enum import Enum


class ExpressionOperationPayloadV2OperationType(str, Enum):
    BRANCHES = "branches"
    COUNT = "count"
    FILTER = "filter"
    FIRST = "first"
    MAX = "max"
    MIN = "min"
    NAVIGATE = "navigate"
    PARSE = "parse"
    RANDOM = "random"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
