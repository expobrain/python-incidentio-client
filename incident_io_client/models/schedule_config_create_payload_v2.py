from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_rotation_create_payload_v2 import (
        ScheduleRotationCreatePayloadV2,
    )


T = TypeVar("T", bound="ScheduleConfigCreatePayloadV2")


@_attrs_define
class ScheduleConfigCreatePayloadV2:
    """
    Example:
        {'rotations': [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'daily'}], 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name': 'My
            Rotation', 'users': [{'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id':
            'USER123'}], 'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'tuesday'}]}]}

    Attributes:
        rotations (Union[Unset, list['ScheduleRotationCreatePayloadV2']]):  Example: [{'effective_from':
            '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1,
            'interval_type': 'daily'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'My Rotation', 'users': [{'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}], 'working_interval': [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'tuesday'}]}].
    """

    rotations: Union[Unset, list["ScheduleRotationCreatePayloadV2"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rotations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rotations, Unset):
            rotations = []
            for rotations_item_data in self.rotations:
                rotations_item = rotations_item_data.to_dict()
                rotations.append(rotations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rotations is not UNSET:
            field_dict["rotations"] = rotations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_rotation_create_payload_v2 import (
            ScheduleRotationCreatePayloadV2,
        )

        d = dict(src_dict)
        rotations = []
        _rotations = d.pop("rotations", UNSET)
        for rotations_item_data in _rotations or []:
            rotations_item = ScheduleRotationCreatePayloadV2.from_dict(rotations_item_data)

            rotations.append(rotations_item)

        schedule_config_create_payload_v2 = cls(
            rotations=rotations,
        )

        schedule_config_create_payload_v2.additional_properties = d
        return schedule_config_create_payload_v2

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
