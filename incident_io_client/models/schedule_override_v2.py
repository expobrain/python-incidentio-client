import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ScheduleOverrideV2")


@_attrs_define
class ScheduleOverrideV2:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'end_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'schedule_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at':
            '2021-08-17T13:28:57.801578Z', 'updated_at': '2021-08-17T13:28:57.801578Z', 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}}

    Attributes:
        created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        end_at (datetime.datetime): End of the override Example: 2021-08-17T13:28:57.801578Z.
        id (str): Unique internal ID of the schedule override Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        layer_id (str): The layer on the rotation on the schedule that this override applies to Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        rotation_id (str): The rotation on the schedule that this override applies to Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        schedule_id (str): The schedule that this override applies to Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        start_at (datetime.datetime): Start of the override Example: 2021-08-17T13:28:57.801578Z.
        updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        user (UserV2):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}.
    """

    created_at: datetime.datetime
    end_at: datetime.datetime
    id: str
    layer_id: str
    rotation_id: str
    schedule_id: str
    start_at: datetime.datetime
    updated_at: datetime.datetime
    user: "UserV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        end_at = self.end_at.isoformat()

        id = self.id

        layer_id = self.layer_id

        rotation_id = self.rotation_id

        schedule_id = self.schedule_id

        start_at = self.start_at.isoformat()

        updated_at = self.updated_at.isoformat()

        user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "end_at": end_at,
                "id": id,
                "layer_id": layer_id,
                "rotation_id": rotation_id,
                "schedule_id": schedule_id,
                "start_at": start_at,
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

        end_at = isoparse(d.pop("end_at"))

        id = d.pop("id")

        layer_id = d.pop("layer_id")

        rotation_id = d.pop("rotation_id")

        schedule_id = d.pop("schedule_id")

        start_at = isoparse(d.pop("start_at"))

        updated_at = isoparse(d.pop("updated_at"))

        user = UserV2.from_dict(d.pop("user"))

        schedule_override_v2 = cls(
            created_at=created_at,
            end_at=end_at,
            id=id,
            layer_id=layer_id,
            rotation_id=rotation_id,
            schedule_id=schedule_id,
            start_at=start_at,
            updated_at=updated_at,
            user=user,
        )

        schedule_override_v2.additional_properties = d
        return schedule_override_v2

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
