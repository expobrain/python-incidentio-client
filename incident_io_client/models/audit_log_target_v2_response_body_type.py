from enum import Enum


class AuditLogTargetV2ResponseBodyType(str, Enum):
    USER = "user"
    SYSTEM = "system"
    API_KEY = "api_key"
    WORKFLOW = "workflow"
    EXTERNAL_RESOURCE = "external_resource"

    def __str__(self) -> str:
        return str(self.value)
