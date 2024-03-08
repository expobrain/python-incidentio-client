from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertEventsV2CreateHTTPRequestBodyMetadata")


@_attrs_define
class AlertEventsV2CreateHTTPRequestBodyMetadata:
    """Any additional metadata that you've configured your alert source to parse

    Example:
        {'service': 'hello.world.com', 'team': ['my-team']}

    """

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_events_v2_create_http_request_body_metadata = cls()

        alert_events_v2_create_http_request_body_metadata.additional_properties = d
        return alert_events_v2_create_http_request_body_metadata

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
