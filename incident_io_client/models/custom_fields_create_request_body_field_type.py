from enum import Enum


class CustomFieldsCreateRequestBodyFieldType(str, Enum):
    SINGLE_SELECT = "single_select"
    MULTI_SELECT = "multi_select"
    TEXT = "text"
    LINK = "link"
    NUMERIC = "numeric"
    TIMESTAMP = "timestamp"

    def __str__(self) -> str:
        return str(self.value)
