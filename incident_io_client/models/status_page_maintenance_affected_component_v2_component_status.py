from enum import Enum


class StatusPageMaintenanceAffectedComponentV2ComponentStatus(str, Enum):
    OPERATIONAL = "operational"
    UNDER_MAINTENANCE = "under_maintenance"

    def __str__(self) -> str:
        return str(self.value)
