from enum import Enum


class CustomFieldsV1CreateRequestBodyRequired(str, Enum):
    ALWAYS = "always"
    BEFORE_CLOSURE = "before_closure"
    NEVER = "never"

    def __str__(self) -> str:
        return str(self.value)
