from enum import Enum


class IdentityV1ResponseBodyRolesItem(str, Enum):
    VIEWER = "viewer"
    INCIDENT_CREATOR = "incident_creator"
    INCIDENT_EDITOR = "incident_editor"
    MANAGE_SETTINGS = "manage_settings"
    GLOBAL_ACCESS = "global_access"

    def __str__(self) -> str:
        return str(self.value)
