from enum import Enum


class ExternalIssueReferenceV1ResponseBodyProvider(str, Enum):
    ASANA = "asana"
    LINEAR = "linear"
    JIRA = "jira"
    JIRA_SERVER = "jira_server"
    GITHUB = "github"
    CLUBHOUSE = "clubhouse"

    def __str__(self) -> str:
        return str(self.value)
