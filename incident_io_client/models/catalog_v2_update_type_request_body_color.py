from enum import Enum


class CatalogV2UpdateTypeRequestBodyColor(str, Enum):
    BLUE = "blue"
    CYAN = "cyan"
    GREEN = "green"
    ORANGE = "orange"
    PINK = "pink"
    VIOLET = "violet"
    YELLOW = "yellow"

    def __str__(self) -> str:
        return str(self.value)
