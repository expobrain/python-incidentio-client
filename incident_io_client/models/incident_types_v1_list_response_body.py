from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_type_v1 import IncidentTypeV1


T = TypeVar("T", bound="IncidentTypesV1ListResponseBody")


@_attrs_define
class IncidentTypesV1ListResponseBody:
    """
    Example:
        {'incident_types': [{'create_in_triage': 'always', 'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Customer facing production outages', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name':
            'Production Outage', 'private_incidents_only': False, 'updated_at': '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        incident_types (List['IncidentTypeV1']):  Example: [{'create_in_triage': 'always', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'private_incidents_only': False,
            'updated_at': '2021-08-17T13:28:57.801578Z'}].
    """

    incident_types: List["IncidentTypeV1"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_types = []
        for incident_types_item_data in self.incident_types:
            incident_types_item = incident_types_item_data.to_dict()
            incident_types.append(incident_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_types": incident_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.incident_type_v1 import IncidentTypeV1

        d = src_dict.copy()
        incident_types = []
        _incident_types = d.pop("incident_types")
        for incident_types_item_data in _incident_types:
            incident_types_item = IncidentTypeV1.from_dict(incident_types_item_data)

            incident_types.append(incident_types_item)

        incident_types_v1_list_response_body = cls(
            incident_types=incident_types,
        )

        incident_types_v1_list_response_body.additional_properties = d
        return incident_types_v1_list_response_body

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
