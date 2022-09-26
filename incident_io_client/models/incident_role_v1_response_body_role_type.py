from enum import Enum


class IncidentRoleV1ResponseBodyRoleType(str, Enum):
    LEAD = "lead"
    REPORTER = "reporter"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)
