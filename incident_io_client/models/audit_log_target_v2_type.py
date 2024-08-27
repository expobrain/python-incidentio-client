from enum import Enum


class AuditLogTargetV2Type(str, Enum):
    ALERT_ROUTE = "alert_route"
    ALERT_SCHEMA = "alert_schema"
    ALERT_SOURCE = "alert_source"
    ANNOUNCEMENT_RULE = "announcement_rule"
    API_KEY = "api_key"
    CATALOG_TYPE = "catalog_type"
    CUSTOM_FIELD = "custom_field"
    DEBRIEF_INVITE_RULE = "debrief_invite_rule"
    ESCALATION_PATH = "escalation_path"
    FOLLOW_UP_PRIORITY = "follow_up_priority"
    HOLIDAY_USER_FEED = "holiday_user_feed"
    INCIDENT = "incident"
    INCIDENT_CALL_SETTING = "incident_call_setting"
    INCIDENT_DURATION_METRIC = "incident_duration_metric"
    INCIDENT_ROLE = "incident_role"
    INCIDENT_STATUS = "incident_status"
    INCIDENT_TIMESTAMP = "incident_timestamp"
    INCIDENT_TYPE = "incident_type"
    INTEGRATION = "integration"
    INTERNAL_STATUS_PAGE = "internal_status_page"
    NUDGE = "nudge"
    POLICY = "policy"
    PRIVATE_INCIDENT_MEMBERSHIP = "private_incident_membership"
    RBAC_ROLE = "rbac_role"
    SCHEDULE = "schedule"
    SCIM_GROUP = "scim_group"
    SEVERITY = "severity"
    STATUS_PAGE = "status_page"
    STATUS_PAGE_SUB_PAGE = "status_page_sub_page"
    STATUS_PAGE_TEMPLATE = "status_page_template"
    USER = "user"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
