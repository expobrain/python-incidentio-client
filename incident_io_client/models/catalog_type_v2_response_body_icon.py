from enum import Enum


class CatalogTypeV2ResponseBodyIcon(str, Enum):
    BOLT = "bolt"
    BOX = "box"
    BRIEFCASE = "briefcase"
    BROWSER = "browser"
    BULB = "bulb"
    CALENDAR = "calendar"
    CLOCK = "clock"
    COG = "cog"
    DATABASE = "database"
    DOC = "doc"
    EMAIL = "email"
    FILES = "files"
    FLAG = "flag"
    MONEY = "money"
    SERVER = "server"
    SEVERITY = "severity"
    STAR = "star"
    STORE = "store"
    TAG = "tag"
    USER = "user"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
