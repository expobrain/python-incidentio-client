from enum import Enum


class CatalogResourceV2ResponseBodyCategory(str, Enum):
    CUSTOM = "custom"
    EXTERNAL = "external"
    PRIMITIVE = "primitive"

    def __str__(self) -> str:
        return str(self.value)
