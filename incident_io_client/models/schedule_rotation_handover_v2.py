from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_rotation_handover_v2_interval_type import (
    ScheduleRotationHandoverV2IntervalType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleRotationHandoverV2")


@_attrs_define
class ScheduleRotationHandoverV2:
    """
    Example:
        {'interval': 1, 'interval_type': 'daily'}

    Attributes:
        interval (Union[Unset, int]):  Example: 1.
        interval_type (Union[Unset, ScheduleRotationHandoverV2IntervalType]):  Example: daily.
    """

    interval: Union[Unset, int] = UNSET
    interval_type: Union[Unset, ScheduleRotationHandoverV2IntervalType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interval = self.interval

        interval_type: Union[Unset, str] = UNSET
        if not isinstance(self.interval_type, Unset):
            interval_type = self.interval_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interval is not UNSET:
            field_dict["interval"] = interval
        if interval_type is not UNSET:
            field_dict["interval_type"] = interval_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interval = d.pop("interval", UNSET)

        _interval_type = d.pop("interval_type", UNSET)
        interval_type: Union[Unset, ScheduleRotationHandoverV2IntervalType]
        if isinstance(_interval_type, Unset):
            interval_type = UNSET
        else:
            interval_type = ScheduleRotationHandoverV2IntervalType(_interval_type)

        schedule_rotation_handover_v2 = cls(
            interval=interval,
            interval_type=interval_type,
        )

        schedule_rotation_handover_v2.additional_properties = d
        return schedule_rotation_handover_v2

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
