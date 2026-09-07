from enum import Enum


class MaintenanceWindowsV1ListStatus(str, Enum):
    ACTIVE = "active"
    PAST = "past"
    UPCOMING = "upcoming"

    def __str__(self) -> str:
        return str(self.value)
