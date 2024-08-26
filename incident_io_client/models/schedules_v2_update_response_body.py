from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_v2 import ScheduleV2


T = TypeVar("T", bound="SchedulesV2UpdateResponseBody")


@_attrs_define
class SchedulesV2UpdateResponseBody:
    """
    Example:
        {'schedule': {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'config': {'rotations':
            [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z',
            'handovers': [{'interval': 1, 'interval_type': 'daily'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name': 'Primary On-Call Schedule', 'users': [{'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}], 'working_interval': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'tuesday'}]}]}, 'created_at': '2021-08-17T13:28:57.801578Z', 'current_shifts': [{'end_at':
            '2021-08-17T13:28:57.801578Z', 'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'fingerprint':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id':
            'U02AYNF2XJM'}}], 'holidays_public_config': {'country_codes': ['GB', 'FR']}, 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Primary On-Call Schedule', 'timezone': 'Europe/London', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        schedule (ScheduleV2):  Example: {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'config':
            {'rotations': [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'daily'}], 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name':
            'Primary On-Call Schedule', 'users': [{'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}], 'working_interval': [{'end_time':
            '17:00', 'start_time': '09:00', 'weekday': 'tuesday'}]}]}, 'created_at': '2021-08-17T13:28:57.801578Z',
            'current_shifts': [{'end_at': '2021-08-17T13:28:57.801578Z', 'entry_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'fingerprint': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at': '2021-08-17T13:28:57.801578Z', 'user': {'email': 'lisa@incident.io',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id':
            'U02AYNF2XJM'}}], 'holidays_public_config': {'country_codes': ['GB', 'FR']}, 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Primary On-Call Schedule', 'timezone': 'Europe/London', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    schedule: "ScheduleV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schedule = self.schedule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule": schedule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schedule_v2 import ScheduleV2

        d = src_dict.copy()
        schedule = ScheduleV2.from_dict(d.pop("schedule"))

        schedules_v2_update_response_body = cls(
            schedule=schedule,
        )

        schedules_v2_update_response_body.additional_properties = d
        return schedules_v2_update_response_body

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
