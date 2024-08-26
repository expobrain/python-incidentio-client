from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrospectiveIncidentOptionsV2")


@_attrs_define
class RetrospectiveIncidentOptionsV2:
    """
    Example:
        {'postmortem_document_url': 'https://docs.google.com/my_doc_id', 'slack_channel_id': 'abc123'}

    Attributes:
        postmortem_document_url (Union[Unset, str]): If the incident mode is 'retrospective', pass the URL of the
            postmortem to attach it to the incident Example: https://docs.google.com/my_doc_id.
        slack_channel_id (Union[Unset, str]): If the incident mode is 'retrospective', pass the ID of a Slack channel in
            your workspace to attach the incident to an existing channel, rather than creating a new one Example: abc123.
    """

    postmortem_document_url: Union[Unset, str] = UNSET
    slack_channel_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        postmortem_document_url = self.postmortem_document_url

        slack_channel_id = self.slack_channel_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if postmortem_document_url is not UNSET:
            field_dict["postmortem_document_url"] = postmortem_document_url
        if slack_channel_id is not UNSET:
            field_dict["slack_channel_id"] = slack_channel_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        postmortem_document_url = d.pop("postmortem_document_url", UNSET)

        slack_channel_id = d.pop("slack_channel_id", UNSET)

        retrospective_incident_options_v2 = cls(
            postmortem_document_url=postmortem_document_url,
            slack_channel_id=slack_channel_id,
        )

        retrospective_incident_options_v2.additional_properties = d
        return retrospective_incident_options_v2

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
