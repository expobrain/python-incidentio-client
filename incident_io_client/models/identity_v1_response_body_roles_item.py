from enum import Enum


class IdentityV1ResponseBodyRolesItem(str, Enum):
    VIEWER = "viewer"
    INCIDENT_CREATOR = "incident_creator"
    GLOBAL_ACCESS = "global_access"
    MANAGE_SETTINGS = "manage_settings"

    def __str__(self) -> str:
        return str(self.value)
