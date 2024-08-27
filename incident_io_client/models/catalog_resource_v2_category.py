from enum import Enum


class CatalogResourceV2Category(str, Enum):
    CUSTOM = "custom"
    EXTERNAL = "external"
    PRIMITIVE = "primitive"

    def __str__(self) -> str:
        return str(self.value)
