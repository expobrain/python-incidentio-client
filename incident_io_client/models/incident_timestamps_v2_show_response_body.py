from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_timestamp_v2_response_body import (
        IncidentTimestampV2ResponseBody,
    )


T = TypeVar("T", bound="IncidentTimestampsV2ShowResponseBody")


@_attrs_define
class IncidentTimestampsV2ShowResponseBody:
    """
    Example:
        {'incident_timestamp': {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1}}

    Attributes:
        incident_timestamp (IncidentTimestampV2ResponseBody):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name':
            'Impact started', 'rank': 1}.
    """

    incident_timestamp: "IncidentTimestampV2ResponseBody"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_timestamp = self.incident_timestamp.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_timestamp": incident_timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.incident_timestamp_v2_response_body import (
            IncidentTimestampV2ResponseBody,
        )

        d = src_dict.copy()
        incident_timestamp = IncidentTimestampV2ResponseBody.from_dict(d.pop("incident_timestamp"))

        incident_timestamps_v2_show_response_body = cls(
            incident_timestamp=incident_timestamp,
        )

        incident_timestamps_v2_show_response_body.additional_properties = d
        return incident_timestamps_v2_show_response_body

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
