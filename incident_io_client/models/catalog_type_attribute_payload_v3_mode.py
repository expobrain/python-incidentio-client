from enum import Enum


class CatalogTypeAttributePayloadV3Mode(str, Enum):
    API = "api"
    BACKLINK = "backlink"
    DASHBOARD = "dashboard"
    DYNAMIC = "dynamic"
    EXTERNAL = "external"
    INTERNAL = "internal"
    PATH = "path"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
