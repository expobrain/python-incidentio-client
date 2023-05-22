from enum import Enum


class CatalogV2CreateTypeRequestBodyIcon(str, Enum):
    BOLT = "bolt"
    BOX = "box"
    BRIEFCASE = "briefcase"
    BROWSER = "browser"
    BULB = "bulb"
    CLOCK = "clock"
    COG = "cog"
    DATABASE = "database"
    DOC = "doc"
    EMAIL = "email"
    SERVER = "server"
    SEVERITY = "severity"
    STAR = "star"
    TAG = "tag"
    USER = "user"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
