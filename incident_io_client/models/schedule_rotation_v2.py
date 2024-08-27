import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_layer_v2 import ScheduleLayerV2
    from ..models.schedule_rotation_handover_v2 import ScheduleRotationHandoverV2
    from ..models.schedule_rotation_working_interval_v2 import (
        ScheduleRotationWorkingIntervalV2,
    )
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ScheduleRotationV2")


@_attrs_define
class ScheduleRotationV2:
    """
    Example:
        {'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z',
            'handovers': [{'interval': 1, 'interval_type': 'daily'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name': 'Primary On-Call Schedule', 'users': [{'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}], 'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'tuesday'}]}

    Attributes:
        handover_start_at (datetime.datetime): Defines the next moment we'll trigger a handover Example:
            2021-08-17T13:28:57.801578Z.
        handovers (List['ScheduleRotationHandoverV2']): Defines the handover intervals for this rota, in order they
            should apply Example: [{'interval': 1, 'interval_type': 'daily'}].
        id (str): Unique internal ID of the rotation Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        layers (List['ScheduleLayerV2']): Controls how many people are on-call concurrently Example: [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}].
        name (str): Human readable name synced from external provider Example: Primary On-Call Schedule.
        effective_from (Union[Unset, datetime.datetime]): When this rotation config will be effective from Example:
            2021-08-17T13:28:57.801578Z.
        users (Union[Unset, List['UserV2']]):  Example: [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}].
        working_interval (Union[Unset, List['ScheduleRotationWorkingIntervalV2']]):  Example: [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'tuesday'}].
    """

    handover_start_at: datetime.datetime
    handovers: List["ScheduleRotationHandoverV2"]
    id: str
    layers: List["ScheduleLayerV2"]
    name: str
    effective_from: Union[Unset, datetime.datetime] = UNSET
    users: Union[Unset, List["UserV2"]] = UNSET
    working_interval: Union[Unset, List["ScheduleRotationWorkingIntervalV2"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        handover_start_at = self.handover_start_at.isoformat()

        handovers = []
        for handovers_item_data in self.handovers:
            handovers_item = handovers_item_data.to_dict()
            handovers.append(handovers_item)

        id = self.id

        layers = []
        for layers_item_data in self.layers:
            layers_item = layers_item_data.to_dict()
            layers.append(layers_item)

        name = self.name

        effective_from: Union[Unset, str] = UNSET
        if not isinstance(self.effective_from, Unset):
            effective_from = self.effective_from.isoformat()

        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        working_interval: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.working_interval, Unset):
            working_interval = []
            for working_interval_item_data in self.working_interval:
                working_interval_item = working_interval_item_data.to_dict()
                working_interval.append(working_interval_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "handover_start_at": handover_start_at,
                "handovers": handovers,
                "id": id,
                "layers": layers,
                "name": name,
            }
        )
        if effective_from is not UNSET:
            field_dict["effective_from"] = effective_from
        if users is not UNSET:
            field_dict["users"] = users
        if working_interval is not UNSET:
            field_dict["working_interval"] = working_interval

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schedule_layer_v2 import ScheduleLayerV2
        from ..models.schedule_rotation_handover_v2 import ScheduleRotationHandoverV2
        from ..models.schedule_rotation_working_interval_v2 import (
            ScheduleRotationWorkingIntervalV2,
        )
        from ..models.user_v2 import UserV2

        d = src_dict.copy()
        handover_start_at = isoparse(d.pop("handover_start_at"))

        handovers = []
        _handovers = d.pop("handovers")
        for handovers_item_data in _handovers:
            handovers_item = ScheduleRotationHandoverV2.from_dict(handovers_item_data)

            handovers.append(handovers_item)

        id = d.pop("id")

        layers = []
        _layers = d.pop("layers")
        for layers_item_data in _layers:
            layers_item = ScheduleLayerV2.from_dict(layers_item_data)

            layers.append(layers_item)

        name = d.pop("name")

        _effective_from = d.pop("effective_from", UNSET)
        effective_from: Union[Unset, datetime.datetime]
        if isinstance(_effective_from, Unset):
            effective_from = UNSET
        else:
            effective_from = isoparse(_effective_from)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = UserV2.from_dict(users_item_data)

            users.append(users_item)

        working_interval = []
        _working_interval = d.pop("working_interval", UNSET)
        for working_interval_item_data in _working_interval or []:
            working_interval_item = ScheduleRotationWorkingIntervalV2.from_dict(
                working_interval_item_data
            )

            working_interval.append(working_interval_item)

        schedule_rotation_v2 = cls(
            handover_start_at=handover_start_at,
            handovers=handovers,
            id=id,
            layers=layers,
            name=name,
            effective_from=effective_from,
            users=users,
            working_interval=working_interval,
        )

        schedule_rotation_v2.additional_properties = d
        return schedule_rotation_v2

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
