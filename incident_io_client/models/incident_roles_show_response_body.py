from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.incident_role_response_body import IncidentRoleResponseBody

T = TypeVar("T", bound="IncidentRolesShowResponseBody")


@attr.s(auto_attribs=True)
class IncidentRolesShowResponseBody:
    """
    Example:
        {'incident_role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently
            coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident;
            Make sure people are clear on responsibilities', 'lead_role': True, 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        incident_role (IncidentRoleResponseBody):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'The person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take
            point on the incident; Make sure people are clear on responsibilities', 'lead_role': True, 'name': 'Incident
            Lead', 'required': True, 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    incident_role: IncidentRoleResponseBody
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_role = self.incident_role.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_role": incident_role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        incident_role = IncidentRoleResponseBody.from_dict(d.pop("incident_role"))

        incident_roles_show_response_body = cls(
            incident_role=incident_role,
        )

        incident_roles_show_response_body.additional_properties = d
        return incident_roles_show_response_body

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
