from enum import Enum


class IncidentParticipantV2ParticipantType(str, Enum):
    COLLABORATOR = "collaborator"
    OBSERVER = "observer"
    RESPONDER = "responder"

    def __str__(self) -> str:
        return str(self.value)
