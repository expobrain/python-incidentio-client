from enum import Enum


class CatalogResourceV3Category(str, Enum):
    CUSTOM = "custom"
    EXTERNAL = "external"
    PRIMITIVE = "primitive"

    def __str__(self) -> str:
        return str(self.value)
