from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.external_issue_reference_v1_provider import (
    ExternalIssueReferenceV1Provider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalIssueReferenceV1")


@_attrs_define
class ExternalIssueReferenceV1:
    """
    Example:
        {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-
            write-up', 'provider': 'asana'}

    Attributes:
        issue_name (Union[Unset, str]): Human readable ID for the issue Example: INC-123.
        issue_permalink (Union[Unset, str]): URL linking directly to the action in the issue tracker Example:
            https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-write-up.
        provider (Union[Unset, ExternalIssueReferenceV1Provider]): ID of the issue tracker provider Example: asana.
    """

    issue_name: Union[Unset, str] = UNSET
    issue_permalink: Union[Unset, str] = UNSET
    provider: Union[Unset, ExternalIssueReferenceV1Provider] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issue_name = self.issue_name

        issue_permalink = self.issue_permalink

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issue_name is not UNSET:
            field_dict["issue_name"] = issue_name
        if issue_permalink is not UNSET:
            field_dict["issue_permalink"] = issue_permalink
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issue_name = d.pop("issue_name", UNSET)

        issue_permalink = d.pop("issue_permalink", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, ExternalIssueReferenceV1Provider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = ExternalIssueReferenceV1Provider(_provider)

        external_issue_reference_v1 = cls(
            issue_name=issue_name,
            issue_permalink=issue_permalink,
            provider=provider,
        )

        external_issue_reference_v1.additional_properties = d
        return external_issue_reference_v1

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
