from enum import Enum


class IncidentAttachmentsV1CreateRequestBodyResourceResourceType(str, Enum):
    ATLASSIAN_STATUSPAGE_INCIDENT = "atlassian_statuspage_incident"
    DATADOG_MONITOR_ALERT = "datadog_monitor_alert"
    GITHUB_PULL_REQUEST = "github_pull_request"
    GITLAB_MERGE_REQUEST = "gitlab_merge_request"
    GOOGLE_CALENDAR_EVENT = "google_calendar_event"
    JIRA_ISSUE = "jira_issue"
    OPSGENIE_ALERT = "opsgenie_alert"
    PAGER_DUTY_INCIDENT = "pager_duty_incident"
    SCRUBBED = "scrubbed"
    SENTRY_ISSUE = "sentry_issue"
    STATUSPAGE_INCIDENT = "statuspage_incident"
    ZENDESK_TICKET = "zendesk_ticket"

    def __str__(self) -> str:
        return str(self.value)
