from enum import Enum


class CatalogTypeAttributePayloadV2RequestBodyMode(str, Enum):
    EXTERNAL = "external"
    MANUAL = "manual"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
