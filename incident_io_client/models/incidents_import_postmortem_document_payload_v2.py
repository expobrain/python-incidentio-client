from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IncidentsImportPostmortemDocumentPayloadV2")


@_attrs_define
class IncidentsImportPostmortemDocumentPayloadV2:
    r"""
    Example:
        {'content': '## Summary\n\nA database migration caused increased latency...', 'title': 'INC-123: Post-incident
            review'}

    Attributes:
        content (str): The document content as GitHub-Flavored Markdown Example: ## Summary

            A database migration caused increased latency....
        title (str): Title of the postmortem document Example: INC-123: Post-incident review.
    """

    content: str
    title: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content")

        title = d.pop("title")

        incidents_import_postmortem_document_payload_v2 = cls(
            content=content,
            title=title,
        )

        incidents_import_postmortem_document_payload_v2.additional_properties = d
        return incidents_import_postmortem_document_payload_v2

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
