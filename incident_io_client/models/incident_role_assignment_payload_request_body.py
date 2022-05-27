from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.user_reference_payload_request_body import UserReferencePayloadRequestBody

T = TypeVar("T", bound="IncidentRoleAssignmentPayloadRequestBody")


@attr.s(auto_attribs=True)
class IncidentRoleAssignmentPayloadRequestBody:
    """
    Example:
        {'assignee': {'email': 'Iure facilis.', 'id': 'Non velit optio qui ea.', 'slack_user_id': 'Sint enim aut
            doloremque.'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}

    Attributes:
        assignee (UserReferencePayloadRequestBody):  Example: {'email': 'Quo optio voluptatum rerum.', 'id': 'Eius ut
            consequuntur fuga atque dignissimos accusamus.', 'slack_user_id': 'Alias temporibus et amet non sed sit.'}.
        incident_role_id (str): Unique ID of an incident role Example: 01FH5TZRWMNAFB0DZ23FD1TV96.
    """

    assignee: UserReferencePayloadRequestBody
    incident_role_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assignee = self.assignee.to_dict()

        incident_role_id = self.incident_role_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignee": assignee,
                "incident_role_id": incident_role_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        assignee = UserReferencePayloadRequestBody.from_dict(d.pop("assignee"))

        incident_role_id = d.pop("incident_role_id")

        incident_role_assignment_payload_request_body = cls(
            assignee=assignee,
            incident_role_id=incident_role_id,
        )

        incident_role_assignment_payload_request_body.additional_properties = d
        return incident_role_assignment_payload_request_body

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
