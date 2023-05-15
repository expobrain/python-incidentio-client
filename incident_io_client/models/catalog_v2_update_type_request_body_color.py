from enum import Enum


class CatalogV2UpdateTypeRequestBodyColor(str, Enum):
    SLATE = "slate"
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    VIOLET = "violet"

    def __str__(self) -> str:
        return str(self.value)
