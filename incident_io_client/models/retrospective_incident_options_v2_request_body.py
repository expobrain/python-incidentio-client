from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrospectiveIncidentOptionsV2RequestBody")


@attr.s(auto_attribs=True)
class RetrospectiveIncidentOptionsV2RequestBody:
    """
    Example:
        {'slack_channel_id': 'abc123'}

    Attributes:
        slack_channel_id (Union[Unset, str]): If the incident mode is 'retrospective', pass the ID of a Slack channel in
            your workspace to attach the incident to an existing channel, rather than creating a new one Example: abc123.
    """

    slack_channel_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        slack_channel_id = self.slack_channel_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slack_channel_id is not UNSET:
            field_dict["slack_channel_id"] = slack_channel_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        slack_channel_id = d.pop("slack_channel_id", UNSET)

        retrospective_incident_options_v2_request_body = cls(
            slack_channel_id=slack_channel_id,
        )

        retrospective_incident_options_v2_request_body.additional_properties = d
        return retrospective_incident_options_v2_request_body

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
