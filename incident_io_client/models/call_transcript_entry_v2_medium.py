from enum import Enum


class CallTranscriptEntryV2Medium(str, Enum):
    CALL_CHAT = "call_chat"
    SPOKEN = "spoken"

    def __str__(self) -> str:
        return str(self.value)
