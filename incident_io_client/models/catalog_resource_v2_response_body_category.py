from enum import Enum


class CatalogResourceV2ResponseBodyCategory(str, Enum):
    PRIMITIVE = "primitive"
    CUSTOM = "custom"
    EXTERNAL = "external"

    def __str__(self) -> str:
        return str(self.value)
