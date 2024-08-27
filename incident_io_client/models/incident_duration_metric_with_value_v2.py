from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_duration_metric_v2 import IncidentDurationMetricV2


T = TypeVar("T", bound="IncidentDurationMetricWithValueV2")


@_attrs_define
class IncidentDurationMetricWithValueV2:
    """
    Example:
        {'duration_metric': {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Lasted'}, 'value_seconds': 1}

    Attributes:
        duration_metric (IncidentDurationMetricV2):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Lasted'}.
        value_seconds (Union[Unset, int]): The calculated durations for this metric Example: 1.
    """

    duration_metric: "IncidentDurationMetricV2"
    value_seconds: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duration_metric = self.duration_metric.to_dict()

        value_seconds = self.value_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration_metric": duration_metric,
            }
        )
        if value_seconds is not UNSET:
            field_dict["value_seconds"] = value_seconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.incident_duration_metric_v2 import IncidentDurationMetricV2

        d = src_dict.copy()
        duration_metric = IncidentDurationMetricV2.from_dict(d.pop("duration_metric"))

        value_seconds = d.pop("value_seconds", UNSET)

        incident_duration_metric_with_value_v2 = cls(
            duration_metric=duration_metric,
            value_seconds=value_seconds,
        )

        incident_duration_metric_with_value_v2.additional_properties = d
        return incident_duration_metric_with_value_v2

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
