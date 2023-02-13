from enum import Enum


class WebhooksPublicIncidentFollowUpCreatedV1ResponseBodyEventType(str, Enum):
    PUBLIC_INCIDENT_INCIDENT_CREATED_V2 = "public_incident.incident_created_v2"
    PRIVATE_INCIDENT_INCIDENT_CREATED_V2 = "private_incident.incident_created_v2"
    PUBLIC_INCIDENT_INCIDENT_UPDATED_V2 = "public_incident.incident_updated_v2"
    PRIVATE_INCIDENT_INCIDENT_UPDATED_V2 = "private_incident.incident_updated_v2"
    PUBLIC_INCIDENT_FOLLOW_UP_CREATED_V1 = "public_incident.follow_up_created_v1"
    PRIVATE_INCIDENT_FOLLOW_UP_CREATED_V1 = "private_incident.follow_up_created_v1"
    PUBLIC_INCIDENT_FOLLOW_UP_UPDATED_V1 = "public_incident.follow_up_updated_v1"
    PRIVATE_INCIDENT_FOLLOW_UP_UPDATED_V1 = "private_incident.follow_up_updated_v1"

    def __str__(self) -> str:
        return str(self.value)
