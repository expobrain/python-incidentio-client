from enum import Enum


class PostmortemDocumentV1Type(str, Enum):
    EXTERNAL = "external"
    IN_APP = "in_app"

    def __str__(self) -> str:
        return str(self.value)
