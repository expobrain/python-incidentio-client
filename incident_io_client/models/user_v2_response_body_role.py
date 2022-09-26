from enum import Enum


class UserV2ResponseBodyRole(str, Enum):
    VIEWER = "viewer"
    RESPONDER = "responder"
    ADMINISTRATOR = "administrator"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
