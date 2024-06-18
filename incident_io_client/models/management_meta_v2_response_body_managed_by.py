from enum import Enum


class ManagementMetaV2ResponseBodyManagedBy(str, Enum):
    DASHBOARD = "dashboard"
    EXTERNAL = "external"
    TERRAFORM = "terraform"

    def __str__(self) -> str:
        return str(self.value)
