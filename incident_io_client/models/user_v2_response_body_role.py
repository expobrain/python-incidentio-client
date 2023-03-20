from enum import Enum


class UserV2ResponseBodyRole(str, Enum):
    VIEWER = "viewer"
    RESPONDER = "responder"
    ADMINISTRATOR = "administrator"
    OWNER = "owner"
    UNSET = "unset"

    def __str__(self) -> str:
        return str(self.value)
