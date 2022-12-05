from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.incident_role_v1_response_body import IncidentRoleV1ResponseBody


T = TypeVar("T", bound="IncidentRolesV1ListResponseBody")


@attr.s(auto_attribs=True)
class IncidentRolesV1ListResponseBody:
    """
    Example:
        {'incident_roles': [{'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently
            coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident;
            Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True, 'role_type': 'lead',
            'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        incident_roles (List['IncidentRoleV1ResponseBody']):  Example: [{'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'The person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'instructions': 'Take point on the incident; Make sure people are clear on responsibilities', 'name': 'Incident
            Lead', 'required': True, 'role_type': 'lead', 'shortform': 'lead', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}].
    """

    incident_roles: List["IncidentRoleV1ResponseBody"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_roles = []
        for incident_roles_item_data in self.incident_roles:
            incident_roles_item = incident_roles_item_data.to_dict()

            incident_roles.append(incident_roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_roles": incident_roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.incident_role_v1_response_body import IncidentRoleV1ResponseBody

        d = src_dict.copy()
        incident_roles = []
        _incident_roles = d.pop("incident_roles")
        for incident_roles_item_data in _incident_roles:
            incident_roles_item = IncidentRoleV1ResponseBody.from_dict(incident_roles_item_data)

            incident_roles.append(incident_roles_item)

        incident_roles_v1_list_response_body = cls(
            incident_roles=incident_roles,
        )

        incident_roles_v1_list_response_body.additional_properties = d
        return incident_roles_v1_list_response_body

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
