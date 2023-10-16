from enum import Enum


class IncidentRoleV1ResponseBodyRoleType(str, Enum):
    CUSTOM = "custom"
    LEAD = "lead"
    REPORTER = "reporter"

    def __str__(self) -> str:
        return str(self.value)
