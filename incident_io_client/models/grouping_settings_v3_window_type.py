from enum import Enum


class GroupingSettingsV3WindowType(str, Enum):
    FIXED = "fixed"
    ROLLING = "rolling"

    def __str__(self) -> str:
        return str(self.value)
