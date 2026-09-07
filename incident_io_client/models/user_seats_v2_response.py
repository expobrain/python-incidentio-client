from enum import Enum


class UserSeatsV2Response(str, Enum):
    FULL_ACCESS = "full_access"
    NONE = "none"
    VIEWER_ONLY = "viewer_only"

    def __str__(self) -> str:
        return str(self.value)
