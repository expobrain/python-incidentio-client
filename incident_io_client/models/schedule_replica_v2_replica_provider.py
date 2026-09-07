from enum import Enum


class ScheduleReplicaV2ReplicaProvider(str, Enum):
    JSM = "jsm"
    NATIVE = "native"
    OPSGENIE = "opsgenie"
    PAGERDUTY = "pagerduty"

    def __str__(self) -> str:
        return str(self.value)
