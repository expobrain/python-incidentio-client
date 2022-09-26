from enum import Enum


class ExternalResourceV1ResponseBodyResourceType(str, Enum):
    PAGER_DUTY_INCIDENT = "pager_duty_incident"
    GITHUB_PULL_REQUEST = "github_pull_request"
    SENTRY_ISSUE = "sentry_issue"
    ZENDESK_TICKET = "zendesk_ticket"

    def __str__(self) -> str:
        return str(self.value)
