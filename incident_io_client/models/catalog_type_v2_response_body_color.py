from enum import Enum


class CatalogTypeV2ResponseBodyColor(str, Enum):
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    VIOLET = "violet"
    PINK = "pink"
    CYAN = "cyan"
    ORANGE = "orange"

    def __str__(self) -> str:
        return str(self.value)
