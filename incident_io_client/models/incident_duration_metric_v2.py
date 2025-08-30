from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IncidentDurationMetricV2")


@_attrs_define
class IncidentDurationMetricV2:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Lasted'}

    Attributes:
        id (str): Unique ID of this incident duration metric Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        name (str): Unique name of this duration metric Example: Lasted.
    """

    id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        incident_duration_metric_v2 = cls(
            id=id,
            name=name,
        )

        incident_duration_metric_v2.additional_properties = d
        return incident_duration_metric_v2

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
