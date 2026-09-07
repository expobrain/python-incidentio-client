from enum import Enum


class CustomFieldsCreatePayloadV1RequiredV2(str, Enum):
    ALWAYS = "always"
    BEFORE_RESOLUTION = "before_resolution"
    NEVER = "never"

    def __str__(self) -> str:
        return str(self.value)
