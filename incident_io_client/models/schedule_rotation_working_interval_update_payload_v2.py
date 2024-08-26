from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_rotation_working_interval_update_payload_v2_weekday import (
    ScheduleRotationWorkingIntervalUpdatePayloadV2Weekday,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleRotationWorkingIntervalUpdatePayloadV2")


@_attrs_define
class ScheduleRotationWorkingIntervalUpdatePayloadV2:
    """
    Example:
        {'end_time': '17:00', 'start_time': '09:00', 'weekday': 'tuesday'}

    Attributes:
        end_time (Union[Unset, str]): End time of the interval, in 24hr format Example: 17:00.
        start_time (Union[Unset, str]): Start time of the interval, in 24hr format Example: 09:00.
        weekday (Union[Unset, ScheduleRotationWorkingIntervalUpdatePayloadV2Weekday]): Weekday this interval applies to
            Example: tuesday.
    """

    end_time: Union[Unset, str] = UNSET
    start_time: Union[Unset, str] = UNSET
    weekday: Union[Unset, ScheduleRotationWorkingIntervalUpdatePayloadV2Weekday] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_time = self.end_time

        start_time = self.start_time

        weekday: Union[Unset, str] = UNSET
        if not isinstance(self.weekday, Unset):
            weekday = self.weekday.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if weekday is not UNSET:
            field_dict["weekday"] = weekday

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end_time = d.pop("end_time", UNSET)

        start_time = d.pop("start_time", UNSET)

        _weekday = d.pop("weekday", UNSET)
        weekday: Union[Unset, ScheduleRotationWorkingIntervalUpdatePayloadV2Weekday]
        if isinstance(_weekday, Unset):
            weekday = UNSET
        else:
            weekday = ScheduleRotationWorkingIntervalUpdatePayloadV2Weekday(_weekday)

        schedule_rotation_working_interval_update_payload_v2 = cls(
            end_time=end_time,
            start_time=start_time,
            weekday=weekday,
        )

        schedule_rotation_working_interval_update_payload_v2.additional_properties = d
        return schedule_rotation_working_interval_update_payload_v2

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
