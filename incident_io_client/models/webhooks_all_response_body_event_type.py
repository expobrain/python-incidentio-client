from enum import Enum


class WebhooksAllResponseBodyEventType(str, Enum):
    PRIVATE_INCIDENT_ACTION_CREATED_V1 = "private_incident.action_created_v1"
    PRIVATE_INCIDENT_ACTION_UPDATED_V1 = "private_incident.action_updated_v1"
    PRIVATE_INCIDENT_FOLLOW_UP_CREATED_V1 = "private_incident.follow_up_created_v1"
    PRIVATE_INCIDENT_FOLLOW_UP_UPDATED_V1 = "private_incident.follow_up_updated_v1"
    PRIVATE_INCIDENT_INCIDENT_CREATED_V2 = "private_incident.incident_created_v2"
    PRIVATE_INCIDENT_INCIDENT_UPDATED_V2 = "private_incident.incident_updated_v2"
    PRIVATE_INCIDENT_MEMBERSHIP_GRANTED_V1 = "private_incident.membership_granted_v1"
    PRIVATE_INCIDENT_MEMBERSHIP_REVOKED_V1 = "private_incident.membership_revoked_v1"
    PUBLIC_INCIDENT_ACTION_CREATED_V1 = "public_incident.action_created_v1"
    PUBLIC_INCIDENT_ACTION_UPDATED_V1 = "public_incident.action_updated_v1"
    PUBLIC_INCIDENT_FOLLOW_UP_CREATED_V1 = "public_incident.follow_up_created_v1"
    PUBLIC_INCIDENT_FOLLOW_UP_UPDATED_V1 = "public_incident.follow_up_updated_v1"
    PUBLIC_INCIDENT_INCIDENT_CREATED_V2 = "public_incident.incident_created_v2"
    PUBLIC_INCIDENT_INCIDENT_STATUS_UPDATED_V2 = "public_incident.incident_status_updated_v2"
    PUBLIC_INCIDENT_INCIDENT_UPDATED_V2 = "public_incident.incident_updated_v2"

    def __str__(self) -> str:
        return str(self.value)
