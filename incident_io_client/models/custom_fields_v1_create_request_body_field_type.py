from enum import Enum


class CustomFieldsV1CreateRequestBodyFieldType(str, Enum):
    LINK = "link"
    MULTI_SELECT = "multi_select"
    NUMERIC = "numeric"
    SINGLE_SELECT = "single_select"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
