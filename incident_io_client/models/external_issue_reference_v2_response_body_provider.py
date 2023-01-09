from enum import Enum


class ExternalIssueReferenceV2ResponseBodyProvider(str, Enum):
    ASANA = "asana"
    LINEAR = "linear"
    JIRA = "jira"
    JIRA_SERVER = "jira_server"
    GITHUB = "github"
    SHORTCUT = "shortcut"

    def __str__(self) -> str:
        return str(self.value)
