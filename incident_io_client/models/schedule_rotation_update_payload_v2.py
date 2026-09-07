import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.schedule_rotation_update_payload_v2_scheduling_mode import (
    ScheduleRotationUpdatePayloadV2SchedulingMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_layer_update_payload_v2 import ScheduleLayerUpdatePayloadV2
    from ..models.schedule_rotation_handover_v2 import ScheduleRotationHandoverV2
    from ..models.schedule_rotation_working_interval_v2 import (
        ScheduleRotationWorkingIntervalV2,
    )
    from ..models.user_reference_payload_v2 import UserReferencePayloadV2


T = TypeVar("T", bound="ScheduleRotationUpdatePayloadV2")


@_attrs_define
class ScheduleRotationUpdatePayloadV2:
    """
    Example:
        {'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z',
            'handovers': [{'interval': 1, 'interval_type': 'hourly'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name': 'My Rotation', 'scheduling_mode': 'fair', 'users':
            [{'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}],
            'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}], 'working_intervals':
            [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}]}

    Attributes:
        effective_from (Union[Unset, datetime.datetime]): When this version of the rotation takes effect. A rotation can
            appear multiple times in `rotations` with the same `id` to schedule changes ahead of time: each version applies
            from its `effective_from` until the next version's. Leave it unset on a rotation's first or only version.
            Example: 2021-08-17T13:28:57.801578Z.
        handover_start_at (Union[Unset, datetime.datetime]): Determines when shifts change hands and who takes them: the
            first user in `users` comes on shift at this time, handing over to the next user after each `handovers`
            interval, cycling through the list — for example, weekly handovers from a Monday 09:00 give week-long shifts
            that change hands on Mondays at 09:00. Example: 2021-08-17T13:28:57.801578Z.
        handovers (Union[Unset, List['ScheduleRotationHandoverV2']]): The cadence shifts hand over on. With more than
            one entry, the intervals apply in turn — for example, one day then three days produces alternating one-day and
            three-day shifts. Example: [{'interval': 1, 'interval_type': 'hourly'}].
        id (Union[Unset, str]): Unique identifier of the rotation Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        layers (Union[Unset, List['ScheduleLayerUpdatePayloadV2']]):  Example: [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}].
        name (Union[Unset, str]): Name of the rotation Example: My Rotation.
        scheduling_mode (Union[Unset, ScheduleRotationUpdatePayloadV2SchedulingMode]): Scheduling algorithm to use for
            this rotation. 'fair' balances workload by considering handover duration, while 'sequential' uses simple round-
            robin rotation through users. Only applies when you have asymmetric handovers (e.g., 2 days then 5 days).
            Example: fair.
        users (Union[Unset, List['UserReferencePayloadV2']]): The people in the rotation, in the order they take shifts.
            Example: [{'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}].
        working_interval (Union[Unset, List['ScheduleRotationWorkingIntervalV2']]): DEPRECATED: Use working_intervals
            instead. Example: [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'monday'}].
        working_intervals (Union[Unset, List['ScheduleRotationWorkingIntervalV2']]):  Example: [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'monday'}].
    """

    effective_from: Union[Unset, datetime.datetime] = UNSET
    handover_start_at: Union[Unset, datetime.datetime] = UNSET
    handovers: Union[Unset, List["ScheduleRotationHandoverV2"]] = UNSET
    id: Union[Unset, str] = UNSET
    layers: Union[Unset, List["ScheduleLayerUpdatePayloadV2"]] = UNSET
    name: Union[Unset, str] = UNSET
    scheduling_mode: Union[Unset, ScheduleRotationUpdatePayloadV2SchedulingMode] = UNSET
    users: Union[Unset, List["UserReferencePayloadV2"]] = UNSET
    working_interval: Union[Unset, List["ScheduleRotationWorkingIntervalV2"]] = UNSET
    working_intervals: Union[Unset, List["ScheduleRotationWorkingIntervalV2"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        effective_from: Union[Unset, str] = UNSET
        if not isinstance(self.effective_from, Unset):
            effective_from = self.effective_from.isoformat()

        handover_start_at: Union[Unset, str] = UNSET
        if not isinstance(self.handover_start_at, Unset):
            handover_start_at = self.handover_start_at.isoformat()

        handovers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.handovers, Unset):
            handovers = []
            for handovers_item_data in self.handovers:
                handovers_item = handovers_item_data.to_dict()
                handovers.append(handovers_item)

        id = self.id

        layers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.layers, Unset):
            layers = []
            for layers_item_data in self.layers:
                layers_item = layers_item_data.to_dict()
                layers.append(layers_item)

        name = self.name

        scheduling_mode: Union[Unset, str] = UNSET
        if not isinstance(self.scheduling_mode, Unset):
            scheduling_mode = self.scheduling_mode.value

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

        working_intervals: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.working_intervals, Unset):
            working_intervals = []
            for working_intervals_item_data in self.working_intervals:
                working_intervals_item = working_intervals_item_data.to_dict()
                working_intervals.append(working_intervals_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if effective_from is not UNSET:
            field_dict["effective_from"] = effective_from
        if handover_start_at is not UNSET:
            field_dict["handover_start_at"] = handover_start_at
        if handovers is not UNSET:
            field_dict["handovers"] = handovers
        if id is not UNSET:
            field_dict["id"] = id
        if layers is not UNSET:
            field_dict["layers"] = layers
        if name is not UNSET:
            field_dict["name"] = name
        if scheduling_mode is not UNSET:
            field_dict["scheduling_mode"] = scheduling_mode
        if users is not UNSET:
            field_dict["users"] = users
        if working_interval is not UNSET:
            field_dict["working_interval"] = working_interval
        if working_intervals is not UNSET:
            field_dict["working_intervals"] = working_intervals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schedule_layer_update_payload_v2 import (
            ScheduleLayerUpdatePayloadV2,
        )
        from ..models.schedule_rotation_handover_v2 import ScheduleRotationHandoverV2
        from ..models.schedule_rotation_working_interval_v2 import (
            ScheduleRotationWorkingIntervalV2,
        )
        from ..models.user_reference_payload_v2 import UserReferencePayloadV2

        d = src_dict.copy()
        _effective_from = d.pop("effective_from", UNSET)
        effective_from: Union[Unset, datetime.datetime]
        if isinstance(_effective_from, Unset):
            effective_from = UNSET
        else:
            effective_from = isoparse(_effective_from)

        _handover_start_at = d.pop("handover_start_at", UNSET)
        handover_start_at: Union[Unset, datetime.datetime]
        if isinstance(_handover_start_at, Unset):
            handover_start_at = UNSET
        else:
            handover_start_at = isoparse(_handover_start_at)

        handovers = []
        _handovers = d.pop("handovers", UNSET)
        for handovers_item_data in _handovers or []:
            handovers_item = ScheduleRotationHandoverV2.from_dict(handovers_item_data)

            handovers.append(handovers_item)

        id = d.pop("id", UNSET)

        layers = []
        _layers = d.pop("layers", UNSET)
        for layers_item_data in _layers or []:
            layers_item = ScheduleLayerUpdatePayloadV2.from_dict(layers_item_data)

            layers.append(layers_item)

        name = d.pop("name", UNSET)

        _scheduling_mode = d.pop("scheduling_mode", UNSET)
        scheduling_mode: Union[Unset, ScheduleRotationUpdatePayloadV2SchedulingMode]
        if isinstance(_scheduling_mode, Unset):
            scheduling_mode = UNSET
        else:
            scheduling_mode = ScheduleRotationUpdatePayloadV2SchedulingMode(_scheduling_mode)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = UserReferencePayloadV2.from_dict(users_item_data)

            users.append(users_item)

        working_interval = []
        _working_interval = d.pop("working_interval", UNSET)
        for working_interval_item_data in _working_interval or []:
            working_interval_item = ScheduleRotationWorkingIntervalV2.from_dict(
                working_interval_item_data
            )

            working_interval.append(working_interval_item)

        working_intervals = []
        _working_intervals = d.pop("working_intervals", UNSET)
        for working_intervals_item_data in _working_intervals or []:
            working_intervals_item = ScheduleRotationWorkingIntervalV2.from_dict(
                working_intervals_item_data
            )

            working_intervals.append(working_intervals_item)

        schedule_rotation_update_payload_v2 = cls(
            effective_from=effective_from,
            handover_start_at=handover_start_at,
            handovers=handovers,
            id=id,
            layers=layers,
            name=name,
            scheduling_mode=scheduling_mode,
            users=users,
            working_interval=working_interval,
            working_intervals=working_intervals,
        )

        schedule_rotation_update_payload_v2.additional_properties = d
        return schedule_rotation_update_payload_v2

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
