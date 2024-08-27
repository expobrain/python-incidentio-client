from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertRouteIncidentTemplatePayloadV2CustomFieldPriorities")


@_attrs_define
class AlertRouteIncidentTemplatePayloadV2CustomFieldPriorities:
    """lookup of the priority options for each custom field in the template

    Example:
        {'abc123': 'abc123'}

    """

    additional_properties: Dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_route_incident_template_payload_v2_custom_field_priorities = cls()

        alert_route_incident_template_payload_v2_custom_field_priorities.additional_properties = d
        return alert_route_incident_template_payload_v2_custom_field_priorities

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
