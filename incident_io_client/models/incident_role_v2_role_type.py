from enum import Enum


class IncidentRoleV2RoleType(str, Enum):
    CUSTOM = "custom"
    LEAD = "lead"
    REPORTER = "reporter"

    def __str__(self) -> str:
        return str(self.value)
