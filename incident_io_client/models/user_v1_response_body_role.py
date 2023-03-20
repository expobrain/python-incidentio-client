from enum import Enum


class UserV1ResponseBodyRole(str, Enum):
    VIEWER = "viewer"
    RESPONDER = "responder"
    ADMINISTRATOR = "administrator"
    OWNER = "owner"
    UNSET = "unset"

    def __str__(self) -> str:
        return str(self.value)
