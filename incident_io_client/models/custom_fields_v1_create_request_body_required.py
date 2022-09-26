from enum import Enum


class CustomFieldsV1CreateRequestBodyRequired(str, Enum):
    NEVER = "never"
    BEFORE_CLOSURE = "before_closure"
    ALWAYS = "always"

    def __str__(self) -> str:
        return str(self.value)
