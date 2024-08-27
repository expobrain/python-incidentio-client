from enum import Enum


class ExternalIssueReferenceV1Provider(str, Enum):
    ASANA = "asana"
    CLICK_UP = "click_up"
    GITHUB = "github"
    GITLAB = "gitlab"
    JIRA = "jira"
    JIRA_SERVER = "jira_server"
    LINEAR = "linear"
    SHORTCUT = "shortcut"

    def __str__(self) -> str:
        return str(self.value)
