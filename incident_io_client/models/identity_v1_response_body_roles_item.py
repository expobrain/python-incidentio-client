from enum import Enum


class IdentityV1ResponseBodyRolesItem(str, Enum):
    CATALOG_EDITOR = "catalog_editor"
    CATALOG_VIEWER = "catalog_viewer"
    GLOBAL_ACCESS = "global_access"
    INCIDENT_CREATOR = "incident_creator"
    INCIDENT_EDITOR = "incident_editor"
    INCIDENT_MEMBERSHIPS_EDITOR = "incident_memberships_editor"
    MANAGE_SETTINGS = "manage_settings"
    PRIVATE_WORKFLOWS_EDITOR = "private_workflows_editor"
    SCHEDULES_EDITOR = "schedules_editor"
    SCHEDULES_READER = "schedules_reader"
    VIEWER = "viewer"
    WORKFLOWS_EDITOR = "workflows_editor"

    def __str__(self) -> str:
        return str(self.value)
