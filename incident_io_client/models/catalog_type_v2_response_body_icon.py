from enum import Enum


class CatalogTypeV2ResponseBodyIcon(str, Enum):
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
