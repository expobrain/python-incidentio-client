from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.external_issue_reference_v2_response_body_provider import (
    ExternalIssueReferenceV2ResponseBodyProvider,
)

T = TypeVar("T", bound="ExternalIssueReferenceV2ResponseBody")


@_attrs_define
class ExternalIssueReferenceV2ResponseBody:
    """
    Example:
        {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-
            write-up', 'provider': 'asana'}

    Attributes:
        issue_name (str): Human readable ID for the issue Example: INC-123.
        issue_permalink (str): URL linking directly to the action in the issue tracker Example:
            https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-write-up.
        provider (ExternalIssueReferenceV2ResponseBodyProvider): ID of the issue tracker provider Example: asana.
    """

    issue_name: str
    issue_permalink: str
    provider: ExternalIssueReferenceV2ResponseBodyProvider
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issue_name = self.issue_name
        issue_permalink = self.issue_permalink
        provider = self.provider.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_name": issue_name,
                "issue_permalink": issue_permalink,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issue_name = d.pop("issue_name")

        issue_permalink = d.pop("issue_permalink")

        provider = ExternalIssueReferenceV2ResponseBodyProvider(d.pop("provider"))

        external_issue_reference_v2_response_body = cls(
            issue_name=issue_name,
            issue_permalink=issue_permalink,
            provider=provider,
        )

        external_issue_reference_v2_response_body.additional_properties = d
        return external_issue_reference_v2_response_body

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
