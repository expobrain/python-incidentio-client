from enum import Enum


class AuditLogTargetV2ResponseBodyType(str, Enum):
    ANNOUNCEMENT_RULE = "announcement_rule"
    API_KEY = "api_key"
    CUSTOM_FIELD = "custom_field"
    FOLLOW_UP_PRIORITY = "follow_up_priority"
    INCIDENT = "incident"
    INCIDENT_DURATION_METRIC = "incident_duration_metric"
    INCIDENT_ROLE = "incident_role"
    INCIDENT_STATUS = "incident_status"
    INCIDENT_TIMESTAMP = "incident_timestamp"
    INCIDENT_TYPE = "incident_type"
    INTEGRATION = "integration"
    POLICY = "policy"
    PRIVATE_INCIDENT_MEMBERSHIP = "private_incident_membership"
    RBAC_ROLE = "rbac_role"
    SCIM_GROUP = "scim_group"
    SEVERITY = "severity"
    STATUS_PAGE = "status_page"
    USER = "user"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
