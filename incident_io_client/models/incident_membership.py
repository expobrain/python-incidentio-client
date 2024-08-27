import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="IncidentMembership")


@_attrs_define
class IncidentMembership:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'updated_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id':
            'U02AYNF2XJM'}}

    Attributes:
        created_at (datetime.datetime): When the membership was created Example: 2021-08-17T13:28:57.801578Z.
        id (str): Unique identifier of this incident membership Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_id (str): Unique identifier of the incident Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        updated_at (datetime.datetime): When the membership was last updated Example: 2021-08-17T13:28:57.801578Z.
        user (UserV2):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}.
    """

    created_at: datetime.datetime
    id: str
    incident_id: str
    updated_at: datetime.datetime
    user: "UserV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        incident_id = self.incident_id

        updated_at = self.updated_at.isoformat()

        user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "incident_id": incident_id,
                "updated_at": updated_at,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_v2 import UserV2

        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        id = d.pop("id")

        incident_id = d.pop("incident_id")

        updated_at = isoparse(d.pop("updated_at"))

        user = UserV2.from_dict(d.pop("user"))

        incident_membership = cls(
            created_at=created_at,
            id=id,
            incident_id=incident_id,
            updated_at=updated_at,
            user=user,
        )

        incident_membership.additional_properties = d
        return incident_membership

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
