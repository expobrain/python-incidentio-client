from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.incident_role_response_body import IncidentRoleResponseBody
from ..models.user_response_body import UserResponseBody
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentRoleAssignmentResponseBody")


@attr.s(auto_attribs=True)
class IncidentRoleAssignmentResponseBody:
    """
    Example:
        {'assignee': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer'}, 'role':
            {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'name': 'Incident Lead', 'required': True, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        role (IncidentRoleResponseBody):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The
            person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on
            the incident; Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'role_type': 'lead', 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
        assignee (Union[Unset, UserResponseBody]):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'viewer'}.
    """

    role: IncidentRoleResponseBody
    assignee: Union[Unset, UserResponseBody] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.to_dict()

        assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )
        if assignee is not UNSET:
            field_dict["assignee"] = assignee

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = IncidentRoleResponseBody.from_dict(d.pop("role"))

        _assignee = d.pop("assignee", UNSET)
        assignee: Union[Unset, UserResponseBody]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = UserResponseBody.from_dict(_assignee)

        incident_role_assignment_response_body = cls(
            role=role,
            assignee=assignee,
        )

        incident_role_assignment_response_body.additional_properties = d
        return incident_role_assignment_response_body

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
