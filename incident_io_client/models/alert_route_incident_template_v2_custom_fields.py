from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.engine_param_binding_v2 import EngineParamBindingV2


T = TypeVar("T", bound="AlertRouteIncidentTemplateV2CustomFields")


@_attrs_define
class AlertRouteIncidentTemplateV2CustomFields:
    """Custom field keys mapped to values

    Example:
        {'custom_field_10014': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}

    """

    additional_properties: Dict[str, "EngineParamBindingV2"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.engine_param_binding_v2 import EngineParamBindingV2

        d = src_dict.copy()
        alert_route_incident_template_v2_custom_fields = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = EngineParamBindingV2.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        alert_route_incident_template_v2_custom_fields.additional_properties = (
            additional_properties
        )
        return alert_route_incident_template_v2_custom_fields

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "EngineParamBindingV2":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "EngineParamBindingV2") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
