from enum import Enum


class IdentityV1ResponseBodyRolesItem(str, Enum):
    CATALOG_EDITOR = "catalog_editor"
    CATALOG_VIEWER = "catalog_viewer"
    GLOBAL_ACCESS = "global_access"
    INCIDENT_CREATOR = "incident_creator"
    INCIDENT_EDITOR = "incident_editor"
    INCIDENT_MEMBERSHIPS_EDITOR = "incident_memberships_editor"
    MANAGE_SETTINGS = "manage_settings"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
