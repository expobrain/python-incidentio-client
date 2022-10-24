from enum import Enum


class CustomFieldV1ResponseBodyFieldType(str, Enum):
    SINGLE_SELECT = "single_select"
    MULTI_SELECT = "multi_select"
    TEXT = "text"
    LINK = "link"
    NUMERIC = "numeric"

    def __str__(self) -> str:
        return str(self.value)
