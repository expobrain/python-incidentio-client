from enum import Enum


class UsersUpdatePagingProviderPayloadV2PreferredEscalationProvider(str, Enum):
    NATIVE = "native"
    OPSGENIE = "opsgenie"
    PAGERDUTY = "pagerduty"
    SPLUNK_ON_CALL = "splunk_on_call"

    def __str__(self) -> str:
        return str(self.value)
