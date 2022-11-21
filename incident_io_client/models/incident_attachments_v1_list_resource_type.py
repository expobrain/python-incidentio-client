from enum import Enum


class IncidentAttachmentsV1ListResourceType(str, Enum):
    PAGER_DUTY_INCIDENT = "pager_duty_incident"
    GITHUB_PULL_REQUEST = "github_pull_request"
    SENTRY_ISSUE = "sentry_issue"
    STATUSPAGE_INCIDENT = "statuspage_incident"
    ZENDESK_TICKET = "zendesk_ticket"

    def __str__(self) -> str:
        return str(self.value)
