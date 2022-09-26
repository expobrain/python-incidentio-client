import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentTimestampV1ResponseBody")


@attr.s(auto_attribs=True)
class IncidentTimestampV1ResponseBody:
    """
    Example:
        {'last_occurred_at': '2021-08-17T13:28:57.801578Z', 'name': 'last_activity'}

    Attributes:
        name (str): Name of the lifecycle event Example: last_activity.
        last_occurred_at (Union[Unset, datetime.datetime]): When this last occurred, if it did Example:
            2021-08-17T13:28:57.801578Z.
    """

    name: str
    last_occurred_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        last_occurred_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_occurred_at, Unset):
            last_occurred_at = self.last_occurred_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if last_occurred_at is not UNSET:
            field_dict["last_occurred_at"] = last_occurred_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        _last_occurred_at = d.pop("last_occurred_at", UNSET)
        last_occurred_at: Union[Unset, datetime.datetime]
        if isinstance(_last_occurred_at, Unset):
            last_occurred_at = UNSET
        else:
            last_occurred_at = isoparse(_last_occurred_at)

        incident_timestamp_v1_response_body = cls(
            name=name,
            last_occurred_at=last_occurred_at,
        )

        incident_timestamp_v1_response_body.additional_properties = d
        return incident_timestamp_v1_response_body

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
