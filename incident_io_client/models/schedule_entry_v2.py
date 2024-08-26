import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ScheduleEntryV2")


@_attrs_define
class ScheduleEntryV2:
    """
    Example:
        {'end_at': '2021-08-17T13:28:57.801578Z', 'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id':
            'U02AYNF2XJM'}}

    Attributes:
        end_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        start_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        entry_id (Union[Unset, str]): Unique identifier of the schedule entry Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        fingerprint (Union[Unset, str]): A unique identifier for this entry, used to determine a unique shift Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        layer_id (Union[Unset, str]): If present, the layer this entry applies to on the rota Example:
            01G0J1EXE7AXZ2C93K61WBPYNH.
        rotation_id (Union[Unset, str]): If present, the rotation this entry applies to on the schedule Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        user (Union[Unset, UserV2]):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}.
    """

    end_at: datetime.datetime
    start_at: datetime.datetime
    entry_id: Union[Unset, str] = UNSET
    fingerprint: Union[Unset, str] = UNSET
    layer_id: Union[Unset, str] = UNSET
    rotation_id: Union[Unset, str] = UNSET
    user: Union[Unset, "UserV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_at = self.end_at.isoformat()

        start_at = self.start_at.isoformat()

        entry_id = self.entry_id

        fingerprint = self.fingerprint

        layer_id = self.layer_id

        rotation_id = self.rotation_id

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_at": end_at,
                "start_at": start_at,
            }
        )
        if entry_id is not UNSET:
            field_dict["entry_id"] = entry_id
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if layer_id is not UNSET:
            field_dict["layer_id"] = layer_id
        if rotation_id is not UNSET:
            field_dict["rotation_id"] = rotation_id
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_v2 import UserV2

        d = src_dict.copy()
        end_at = isoparse(d.pop("end_at"))

        start_at = isoparse(d.pop("start_at"))

        entry_id = d.pop("entry_id", UNSET)

        fingerprint = d.pop("fingerprint", UNSET)

        layer_id = d.pop("layer_id", UNSET)

        rotation_id = d.pop("rotation_id", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserV2]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserV2.from_dict(_user)

        schedule_entry_v2 = cls(
            end_at=end_at,
            start_at=start_at,
            entry_id=entry_id,
            fingerprint=fingerprint,
            layer_id=layer_id,
            rotation_id=rotation_id,
            user=user,
        )

        schedule_entry_v2.additional_properties = d
        return schedule_entry_v2

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
