import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.action_v2_status import ActionV2Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ActionV2")


@_attrs_define
class ActionV2:
    """
    Example:
        {'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}, 'completed_at': '2021-08-17T13:28:57.801578Z', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Call the fire brigade', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'status': 'outstanding', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When the action was created Example: 2021-08-17T13:28:57.801578Z.
        description (str): Description of the action Example: Call the fire brigade.
        id (str): Unique identifier for the action Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        incident_id (str): Unique identifier of the incident the action belongs to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        status (ActionV2Status): Status of the action Example: outstanding.
        updated_at (datetime.datetime): When the action was last updated Example: 2021-08-17T13:28:57.801578Z.
        assignee (Union[Unset, UserV2]):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}.
        completed_at (Union[Unset, datetime.datetime]): When the action was completed Example:
            2021-08-17T13:28:57.801578Z.
    """

    created_at: datetime.datetime
    description: str
    id: str
    incident_id: str
    status: ActionV2Status
    updated_at: datetime.datetime
    assignee: Union[Unset, "UserV2"] = UNSET
    completed_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description

        id = self.id

        incident_id = self.incident_id

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "id": id,
                "incident_id": incident_id,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_v2 import UserV2

        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        description = d.pop("description")

        id = d.pop("id")

        incident_id = d.pop("incident_id")

        status = ActionV2Status(d.pop("status"))

        updated_at = isoparse(d.pop("updated_at"))

        _assignee = d.pop("assignee", UNSET)
        assignee: Union[Unset, UserV2]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = UserV2.from_dict(_assignee)

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        action_v2 = cls(
            created_at=created_at,
            description=description,
            id=id,
            incident_id=incident_id,
            status=status,
            updated_at=updated_at,
            assignee=assignee,
            completed_at=completed_at,
        )

        action_v2.additional_properties = d
        return action_v2

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
