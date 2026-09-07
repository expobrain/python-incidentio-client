import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageMaintenanceComponentMaintenancePeriodV2")


@_attrs_define
class StatusPageMaintenanceComponentMaintenancePeriodV2:
    """
    Example:
        {'component_id': '01GW7P4ES31Q6V1ZQH321T0GJN', 'end_at': '2021-08-17T13:28:57.801578Z', 'start_at':
            '2021-08-17T13:28:57.801578Z'}

    Attributes:
        component_id (str): The ID of the affected component. This may be found by calling the ShowStatusPageStructure
            endpoint. Example: 01GW7P4ES31Q6V1ZQH321T0GJN.
        start_at (datetime.datetime): When the component started being under maintenance Example:
            2021-08-17T13:28:57.801578Z.
        end_at (Union[Unset, datetime.datetime]): When the component stopped being under maintenance. If this is null,
            the impact is ongoing. Example: 2021-08-17T13:28:57.801578Z.
    """

    component_id: str
    start_at: datetime.datetime
    end_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        component_id = self.component_id

        start_at = self.start_at.isoformat()

        end_at: Union[Unset, str] = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_id": component_id,
                "start_at": start_at,
            }
        )
        if end_at is not UNSET:
            field_dict["end_at"] = end_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        component_id = d.pop("component_id")

        start_at = isoparse(d.pop("start_at"))

        _end_at = d.pop("end_at", UNSET)
        end_at: Union[Unset, datetime.datetime]
        if isinstance(_end_at, Unset):
            end_at = UNSET
        else:
            end_at = isoparse(_end_at)

        status_page_maintenance_component_maintenance_period_v2 = cls(
            component_id=component_id,
            start_at=start_at,
            end_at=end_at,
        )

        status_page_maintenance_component_maintenance_period_v2.additional_properties = d
        return status_page_maintenance_component_maintenance_period_v2

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
