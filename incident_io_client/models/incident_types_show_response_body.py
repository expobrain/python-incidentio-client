from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.incident_type_response_body import IncidentTypeResponseBody

T = TypeVar("T", bound="IncidentTypesShowResponseBody")


@attr.s(auto_attribs=True)
class IncidentTypesShowResponseBody:
    """
    Example:
        {'incident_type': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production
            outages', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage',
            'private_incidents_only': True, 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        incident_type (IncidentTypeResponseBody):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Customer facing production outages', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': True, 'name':
            'Production Outage', 'private_incidents_only': False, 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    incident_type: IncidentTypeResponseBody
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_type = self.incident_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_type": incident_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        incident_type = IncidentTypeResponseBody.from_dict(d.pop("incident_type"))

        incident_types_show_response_body = cls(
            incident_type=incident_type,
        )

        incident_types_show_response_body.additional_properties = d
        return incident_types_show_response_body

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
