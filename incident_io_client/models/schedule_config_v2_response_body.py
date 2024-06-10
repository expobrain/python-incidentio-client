from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_rotation_v2_response_body import (
        ScheduleRotationV2ResponseBody,
    )


T = TypeVar("T", bound="ScheduleConfigV2ResponseBody")


@_attrs_define
class ScheduleConfigV2ResponseBody:
    """
    Example:
        {'rotations': [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'daily'}], 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name':
            'Primary On-Call Schedule', 'users': [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}], 'working_interval': [{'end_time':
            '17:00', 'start_time': '09:00', 'weekday': 'tuesday'}]}]}

    Attributes:
        rotations (List['ScheduleRotationV2ResponseBody']): Rotas in this schedule Example: [{'effective_from':
            '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1,
            'interval_type': 'daily'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'Primary On-Call Schedule', 'users': [{'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}],
            'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'tuesday'}]}].
    """

    rotations: List["ScheduleRotationV2ResponseBody"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rotations = []
        for rotations_item_data in self.rotations:
            rotations_item = rotations_item_data.to_dict()
            rotations.append(rotations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rotations": rotations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schedule_rotation_v2_response_body import (
            ScheduleRotationV2ResponseBody,
        )

        d = src_dict.copy()
        rotations = []
        _rotations = d.pop("rotations")
        for rotations_item_data in _rotations:
            rotations_item = ScheduleRotationV2ResponseBody.from_dict(rotations_item_data)

            rotations.append(rotations_item)

        schedule_config_v2_response_body = cls(
            rotations=rotations,
        )

        schedule_config_v2_response_body.additional_properties = d
        return schedule_config_v2_response_body

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
