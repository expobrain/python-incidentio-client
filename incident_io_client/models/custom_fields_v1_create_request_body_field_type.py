from enum import Enum


class CustomFieldsV1CreateRequestBodyFieldType(str, Enum):
    SINGLE_SELECT = "single_select"
    MULTI_SELECT = "multi_select"
    TEXT = "text"
    LINK = "link"
    NUMERIC = "numeric"

    def __str__(self) -> str:
        return str(self.value)
