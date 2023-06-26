from enum import Enum


class CatalogTypeAttributeV2ResponseBodyMode(str, Enum):
    VALUE_0 = ""
    MANUAL = "manual"
    EXTERNAL = "external"

    def __str__(self) -> str:
        return str(self.value)
