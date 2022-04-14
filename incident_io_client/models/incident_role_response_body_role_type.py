from enum import Enum


class IncidentRoleResponseBodyRoleType(str, Enum):
    LEAD = "lead"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)
