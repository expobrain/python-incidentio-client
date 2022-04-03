from enum import Enum


class ExternalIssueReferenceResponseBodyProvider(str, Enum):
    LINEAR = "linear"
    JIRA = "jira"
    JIRA_SERVER = "jira_server"
    GITHUB = "github"
    CLUBHOUSE = "clubhouse"

    def __str__(self) -> str:
        return str(self.value)
