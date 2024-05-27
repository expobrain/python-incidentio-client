import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_layer_create_payload_v2_request_body import (
        ScheduleLayerCreatePayloadV2RequestBody,
    )
    from ..models.schedule_rotation_handover_v2_request_body import (
        ScheduleRotationHandoverV2RequestBody,
    )
    from ..models.schedule_rotation_working_interval_create_payload_v2_request_body import (
        ScheduleRotationWorkingIntervalCreatePayloadV2RequestBody,
    )
    from ..models.user_reference_payload_v2_request_body import (
        UserReferencePayloadV2RequestBody,
    )


T = TypeVar("T", bound="ScheduleRotationCreatePayloadV2RequestBody")


@_attrs_define
class ScheduleRotationCreatePayloadV2RequestBody:
    """
    Example:
        {'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z',
            'handovers': [{'interval': 1, 'interval_type': 'daily'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name': 'My Rotation', 'users': [{'email': 'bob@example.com',
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}], 'working_interval': [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'tuesday'}]}

    Attributes:
        name (str): Name of the rotation Example: My Rotation.
        effective_from (Union[Unset, datetime.datetime]):  Example: 2021-08-17T13:28:57.801578Z.
        handover_start_at (Union[Unset, datetime.datetime]):  Example: 2021-08-17T13:28:57.801578Z.
        handovers (Union[Unset, List['ScheduleRotationHandoverV2RequestBody']]):  Example: [{'interval': 1,
            'interval_type': 'daily'}].
        id (Union[Unset, str]): Unique identifier of the rotation Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        layers (Union[Unset, List['ScheduleLayerCreatePayloadV2RequestBody']]):  Example: [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}].
        users (Union[Unset, List['UserReferencePayloadV2RequestBody']]):  Example: [{'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}].
        working_interval (Union[Unset, List['ScheduleRotationWorkingIntervalCreatePayloadV2RequestBody']]):  Example:
            [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'tuesday'}].
    """

    name: str
    effective_from: Union[Unset, datetime.datetime] = UNSET
    handover_start_at: Union[Unset, datetime.datetime] = UNSET
    handovers: Union[Unset, List["ScheduleRotationHandoverV2RequestBody"]] = UNSET
    id: Union[Unset, str] = UNSET
    layers: Union[Unset, List["ScheduleLayerCreatePayloadV2RequestBody"]] = UNSET
    users: Union[Unset, List["UserReferencePayloadV2RequestBody"]] = UNSET
    working_interval: Union[
        Unset, List["ScheduleRotationWorkingIntervalCreatePayloadV2RequestBody"]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

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
                "name": name,
            }
        )
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
        if users is not UNSET:
            field_dict["users"] = users
        if working_interval is not UNSET:
            field_dict["working_interval"] = working_interval

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schedule_layer_create_payload_v2_request_body import (
            ScheduleLayerCreatePayloadV2RequestBody,
        )
        from ..models.schedule_rotation_handover_v2_request_body import (
            ScheduleRotationHandoverV2RequestBody,
        )
        from ..models.schedule_rotation_working_interval_create_payload_v2_request_body import (
            ScheduleRotationWorkingIntervalCreatePayloadV2RequestBody,
        )
        from ..models.user_reference_payload_v2_request_body import (
            UserReferencePayloadV2RequestBody,
        )

        d = src_dict.copy()
        name = d.pop("name")

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
            handovers_item = ScheduleRotationHandoverV2RequestBody.from_dict(handovers_item_data)

            handovers.append(handovers_item)

        id = d.pop("id", UNSET)

        layers = []
        _layers = d.pop("layers", UNSET)
        for layers_item_data in _layers or []:
            layers_item = ScheduleLayerCreatePayloadV2RequestBody.from_dict(layers_item_data)

            layers.append(layers_item)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = UserReferencePayloadV2RequestBody.from_dict(users_item_data)

            users.append(users_item)

        working_interval = []
        _working_interval = d.pop("working_interval", UNSET)
        for working_interval_item_data in _working_interval or []:
            working_interval_item = (
                ScheduleRotationWorkingIntervalCreatePayloadV2RequestBody.from_dict(
                    working_interval_item_data
                )
            )

            working_interval.append(working_interval_item)

        schedule_rotation_create_payload_v2_request_body = cls(
            name=name,
            effective_from=effective_from,
            handover_start_at=handover_start_at,
            handovers=handovers,
            id=id,
            layers=layers,
            users=users,
            working_interval=working_interval,
        )

        schedule_rotation_create_payload_v2_request_body.additional_properties = d
        return schedule_rotation_create_payload_v2_request_body

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
