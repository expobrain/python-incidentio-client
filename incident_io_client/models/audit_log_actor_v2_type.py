from enum import Enum


class AuditLogActorV2Type(str, Enum):
    API_KEY = "api_key"
    EXTERNAL_RESOURCE = "external_resource"
    SYSTEM = "system"
    USER = "user"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
