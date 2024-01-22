from enum import Enum


class CatalogTypeAttributeV2ResponseBodyMode(str, Enum):
    EXTERNAL = "external"
    INTERNAL = "internal"
    MANUAL = "manual"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
