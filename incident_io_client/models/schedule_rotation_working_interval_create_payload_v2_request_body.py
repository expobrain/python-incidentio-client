from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_rotation_working_interval_create_payload_v2_request_body_weekday import (
    ScheduleRotationWorkingIntervalCreatePayloadV2RequestBodyWeekday,
)

T = TypeVar("T", bound="ScheduleRotationWorkingIntervalCreatePayloadV2RequestBody")


@_attrs_define
class ScheduleRotationWorkingIntervalCreatePayloadV2RequestBody:
    """
    Example:
        {'end_time': '17:00', 'start_time': '09:00', 'weekday': 'tuesday'}

    Attributes:
        end_time (str): End time of the interval, in 24hr format Example: 17:00.
        start_time (str): Start time of the interval, in 24hr format Example: 09:00.
        weekday (ScheduleRotationWorkingIntervalCreatePayloadV2RequestBodyWeekday): Weekday this interval applies to
            Example: tuesday.
    """

    end_time: str
    start_time: str
    weekday: ScheduleRotationWorkingIntervalCreatePayloadV2RequestBodyWeekday
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_time = self.end_time

        start_time = self.start_time

        weekday = self.weekday.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_time": end_time,
                "start_time": start_time,
                "weekday": weekday,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end_time = d.pop("end_time")

        start_time = d.pop("start_time")

        weekday = ScheduleRotationWorkingIntervalCreatePayloadV2RequestBodyWeekday(
            d.pop("weekday")
        )

        schedule_rotation_working_interval_create_payload_v2_request_body = cls(
            end_time=end_time,
            start_time=start_time,
            weekday=weekday,
        )

        schedule_rotation_working_interval_create_payload_v2_request_body.additional_properties = d
        return schedule_rotation_working_interval_create_payload_v2_request_body

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
