import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentTimestampValueV2")


@_attrs_define
class IncidentTimestampValueV2:
    """
    Example:
        {'value': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        value (Union[Unset, datetime.datetime]): The current value of this timestamp, for this incident Example:
            2021-08-17T13:28:57.801578Z.
    """

    value: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, str] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _value = d.pop("value", UNSET)
        value: Union[Unset, datetime.datetime]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = isoparse(_value)

        incident_timestamp_value_v2 = cls(
            value=value,
        )

        incident_timestamp_value_v2.additional_properties = d
        return incident_timestamp_value_v2

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
