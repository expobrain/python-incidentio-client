from enum import Enum


class CatalogTypeAttributePayloadV2RequestBodyMode(str, Enum):
    VALUE_0 = ""
    MANUAL = "manual"
    EXTERNAL = "external"

    def __str__(self) -> str:
        return str(self.value)
