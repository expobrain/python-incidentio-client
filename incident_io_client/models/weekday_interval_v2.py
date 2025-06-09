from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WeekdayIntervalV2")


@_attrs_define
class WeekdayIntervalV2:
    """
    Example:
        {'end_time': '17:00', 'start_time': '09:00', 'weekday': 'abc123'}

    Attributes:
        end_time (str): End time of the interval, in 24hr format Example: 17:00.
        start_time (str): Start time of the interval, in 24hr format Example: 09:00.
        weekday (str): Weekday this interval applies to Example: abc123.
    """

    end_time: str
    start_time: str
    weekday: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_time = self.end_time

        start_time = self.start_time

        weekday = self.weekday

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_time = d.pop("end_time")

        start_time = d.pop("start_time")

        weekday = d.pop("weekday")

        weekday_interval_v2 = cls(
            end_time=end_time,
            start_time=start_time,
            weekday=weekday,
        )

        weekday_interval_v2.additional_properties = d
        return weekday_interval_v2

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
