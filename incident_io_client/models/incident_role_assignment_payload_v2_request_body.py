from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_reference_payload_v2_request_body import (
    UserReferencePayloadV2RequestBody,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentRoleAssignmentPayloadV2RequestBody")


@attr.s(auto_attribs=True)
class IncidentRoleAssignmentPayloadV2RequestBody:
    """
    Example:
        {'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}

    Attributes:
        incident_role_id (str): Unique ID of an incident role Example: 01FH5TZRWMNAFB0DZ23FD1TV96.
        assignee (Union[Unset, UserReferencePayloadV2RequestBody]):  Example: {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}.
    """

    incident_role_id: str
    assignee: Union[Unset, UserReferencePayloadV2RequestBody] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_role_id = self.incident_role_id
        assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_role_id": incident_role_id,
            }
        )
        if assignee is not UNSET:
            field_dict["assignee"] = assignee

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        incident_role_id = d.pop("incident_role_id")

        _assignee = d.pop("assignee", UNSET)
        assignee: Union[Unset, UserReferencePayloadV2RequestBody]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = UserReferencePayloadV2RequestBody.from_dict(_assignee)

        incident_role_assignment_payload_v2_request_body = cls(
            incident_role_id=incident_role_id,
            assignee=assignee,
        )

        incident_role_assignment_payload_v2_request_body.additional_properties = d
        return incident_role_assignment_payload_v2_request_body

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
