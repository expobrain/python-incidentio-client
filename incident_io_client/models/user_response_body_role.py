from enum import Enum


class UserResponseBodyRole(str, Enum):
    VALUE_0 = ""
    VIEWER = "viewer"
    RESPONDER = "responder"
    ADMINISTRATOR = "administrator"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
