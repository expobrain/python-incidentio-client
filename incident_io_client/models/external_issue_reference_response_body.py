from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.external_issue_reference_response_body_provider import (
    ExternalIssueReferenceResponseBodyProvider,
)

T = TypeVar("T", bound="ExternalIssueReferenceResponseBody")


@attr.s(auto_attribs=True)
class ExternalIssueReferenceResponseBody:
    """
    Example:
        {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-
            write-up', 'provider': 'linear'}

    Attributes:
        issue_name (str): Human readable ID for the issue Example: INC-123.
        issue_permalink (str): URL linking directly to the action in the issue tracker Example:
            https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-write-up.
        provider (ExternalIssueReferenceResponseBodyProvider): ID of the issue tracker provider Example: linear.
    """

    issue_name: str
    issue_permalink: str
    provider: ExternalIssueReferenceResponseBodyProvider
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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

        provider = ExternalIssueReferenceResponseBodyProvider(d.pop("provider"))

        external_issue_reference_response_body = cls(
            issue_name=issue_name,
            issue_permalink=issue_permalink,
            provider=provider,
        )

        external_issue_reference_response_body.additional_properties = d
        return external_issue_reference_response_body

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
