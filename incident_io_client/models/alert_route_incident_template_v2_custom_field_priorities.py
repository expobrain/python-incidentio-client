from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_route_incident_template_v2_custom_field_priorities_additional_property import (
    AlertRouteIncidentTemplateV2CustomFieldPrioritiesAdditionalProperty,
)

T = TypeVar("T", bound="AlertRouteIncidentTemplateV2CustomFieldPriorities")


@_attrs_define
class AlertRouteIncidentTemplateV2CustomFieldPriorities:
    """lookup of the priority options for each custom field in the template

    Example:
        {'abc123': 'first-wins'}

    """

    additional_properties: Dict[
        str, AlertRouteIncidentTemplateV2CustomFieldPrioritiesAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_route_incident_template_v2_custom_field_priorities = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                AlertRouteIncidentTemplateV2CustomFieldPrioritiesAdditionalProperty(prop_dict)
            )

            additional_properties[prop_name] = additional_property

        alert_route_incident_template_v2_custom_field_priorities.additional_properties = (
            additional_properties
        )
        return alert_route_incident_template_v2_custom_field_priorities

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> AlertRouteIncidentTemplateV2CustomFieldPrioritiesAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: AlertRouteIncidentTemplateV2CustomFieldPrioritiesAdditionalProperty,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
