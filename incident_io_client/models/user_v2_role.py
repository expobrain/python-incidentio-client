from enum import Enum


class UserV2Role(str, Enum):
    ADMINISTRATOR = "administrator"
    OWNER = "owner"
    RESPONDER = "responder"
    UNSET = "unset"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
