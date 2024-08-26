from enum import Enum


class CatalogTypeV2Icon(str, Enum):
    ALERT = "alert"
    BOLT = "bolt"
    BOX = "box"
    BRIEFCASE = "briefcase"
    BROWSER = "browser"
    BULB = "bulb"
    CALENDAR = "calendar"
    CLOCK = "clock"
    COG = "cog"
    COMPONENTS = "components"
    DATABASE = "database"
    DOC = "doc"
    EMAIL = "email"
    ESCALATION_PATH = "escalation-path"
    FILES = "files"
    FLAG = "flag"
    FOLDER = "folder"
    GLOBE = "globe"
    MONEY = "money"
    SERVER = "server"
    SEVERITY = "severity"
    STAR = "star"
    STATUS_PAGE = "status-page"
    STORE = "store"
    TAG = "tag"
    USER = "user"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
