import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_layer_update_payload_v2 import ScheduleLayerUpdatePayloadV2
    from ..models.schedule_rotation_handover_v2 import ScheduleRotationHandoverV2
    from ..models.schedule_rotation_working_interval_update_payload_v2 import (
        ScheduleRotationWorkingIntervalUpdatePayloadV2,
    )
    from ..models.user_reference_payload_v2 import UserReferencePayloadV2


T = TypeVar("T", bound="ScheduleRotationUpdatePayloadV2")


@_attrs_define
class ScheduleRotationUpdatePayloadV2:
    """
    Example:
        {'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z',
            'handovers': [{'interval': 1, 'interval_type': 'daily'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name': 'My Rotation', 'users': [{'email': 'bob@example.com',
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}], 'working_interval': [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'tuesday'}]}

    Attributes:
        effective_from (Union[Unset, datetime.datetime]):  Example: 2021-08-17T13:28:57.801578Z.
        handover_start_at (Union[Unset, datetime.datetime]):  Example: 2021-08-17T13:28:57.801578Z.
        handovers (Union[Unset, List['ScheduleRotationHandoverV2']]):  Example: [{'interval': 1, 'interval_type':
            'daily'}].
        id (Union[Unset, str]): Unique identifier of the rotation Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        layers (Union[Unset, List['ScheduleLayerUpdatePayloadV2']]):  Example: [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}].
        name (Union[Unset, str]): Name of the rotation Example: My Rotation.
        users (Union[Unset, List['UserReferencePayloadV2']]):  Example: [{'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}].
        working_interval (Union[Unset, List['ScheduleRotationWorkingIntervalUpdatePayloadV2']]):  Example: [{'end_time':
            '17:00', 'start_time': '09:00', 'weekday': 'tuesday'}].
    """

    effective_from: Union[Unset, datetime.datetime] = UNSET
    handover_start_at: Union[Unset, datetime.datetime] = UNSET
    handovers: Union[Unset, List["ScheduleRotationHandoverV2"]] = UNSET
    id: Union[Unset, str] = UNSET
    layers: Union[Unset, List["ScheduleLayerUpdatePayloadV2"]] = UNSET
    name: Union[Unset, str] = UNSET
    users: Union[Unset, List["UserReferencePayloadV2"]] = UNSET
    working_interval: Union[Unset, List["ScheduleRotationWorkingIntervalUpdatePayloadV2"]] = UNSET
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
        if users is not UNSET:
            field_dict["users"] = users
        if working_interval is not UNSET:
            field_dict["working_interval"] = working_interval

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schedule_layer_update_payload_v2 import (
            ScheduleLayerUpdatePayloadV2,
        )
        from ..models.schedule_rotation_handover_v2 import ScheduleRotationHandoverV2
        from ..models.schedule_rotation_working_interval_update_payload_v2 import (
            ScheduleRotationWorkingIntervalUpdatePayloadV2,
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

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = UserReferencePayloadV2.from_dict(users_item_data)

            users.append(users_item)

        working_interval = []
        _working_interval = d.pop("working_interval", UNSET)
        for working_interval_item_data in _working_interval or []:
            working_interval_item = ScheduleRotationWorkingIntervalUpdatePayloadV2.from_dict(
                working_interval_item_data
            )

            working_interval.append(working_interval_item)

        schedule_rotation_update_payload_v2 = cls(
            effective_from=effective_from,
            handover_start_at=handover_start_at,
            handovers=handovers,
            id=id,
            layers=layers,
            name=name,
            users=users,
            working_interval=working_interval,
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
