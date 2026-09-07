import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkloadMetadataV2")


@_attrs_define
class WorkloadMetadataV2:
    """
    Example:
        {'data_synced_at': '2021-08-17T13:00:00Z'}

    Attributes:
        data_synced_at (Union[Unset, datetime.datetime]): The time the workload figures are calculated up to. Workload
            is complete up to this time. Null if we have not calculated any workload for this incident yet. Example:
            2021-08-17T13:00:00Z.
    """

    data_synced_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_synced_at: Union[Unset, str] = UNSET
        if not isinstance(self.data_synced_at, Unset):
            data_synced_at = self.data_synced_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_synced_at is not UNSET:
            field_dict["data_synced_at"] = data_synced_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _data_synced_at = d.pop("data_synced_at", UNSET)
        data_synced_at: Union[Unset, datetime.datetime]
        if isinstance(_data_synced_at, Unset):
            data_synced_at = UNSET
        else:
            data_synced_at = isoparse(_data_synced_at)

        workload_metadata_v2 = cls(
            data_synced_at=data_synced_at,
        )

        workload_metadata_v2.additional_properties = d
        return workload_metadata_v2

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
