from enum import Enum


class CustomFieldV2ResponseBodyFieldType(str, Enum):
    LINK = "link"
    MULTI_SELECT = "multi_select"
    NUMERIC = "numeric"
    SINGLE_SELECT = "single_select"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
