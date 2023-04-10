from enum import Enum


class CatalogV2UpdateTypeRequestBodyIcon(str, Enum):
    BOX = "box"
    BRIEFCASE = "briefcase"
    BULB = "bulb"
    CLOCK = "clock"
    COG = "cog"
    DOC = "doc"
    EMAIL = "email"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
