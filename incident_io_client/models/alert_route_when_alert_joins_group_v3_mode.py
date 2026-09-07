from enum import Enum


class AlertRouteWhenAlertJoinsGroupV3Mode(str, Enum):
    ON_EACH_NEW_ALERT = "on_each_new_alert"
    ON_PRIORITY_INCREASE = "on_priority_increase"

    def __str__(self) -> str:
        return str(self.value)
