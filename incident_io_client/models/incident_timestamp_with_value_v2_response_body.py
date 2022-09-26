from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.incident_timestamp_v2_response_body import IncidentTimestampV2ResponseBody
from ..models.incident_timestamp_value_v2_response_body import (
    IncidentTimestampValueV2ResponseBody,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentTimestampWithValueV2ResponseBody")


@attr.s(auto_attribs=True)
class IncidentTimestampWithValueV2ResponseBody:
    """
    Example:
        {'timestamp': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'When this incident started impacting
            customers.', 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1, 'required': 'never',
            'set_on_creation': True, 'set_on_status_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'set_on_transition': 'enter',
            'set_on_visit': 'first', 'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post':
            True, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'value': {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        timestamp (IncidentTimestampV2ResponseBody):  Example: {'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'When this incident started impacting customers.', 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name':
            'Impact started', 'rank': 1, 'required': 'never', 'set_on_creation': True, 'set_on_status_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'set_on_transition': 'enter', 'set_on_visit': 'first', 'show_before_closure':
            True, 'show_before_creation': True, 'show_in_announcement_post': True, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
        value (Union[Unset, IncidentTimestampValueV2ResponseBody]):  Example: {'created_at':
            '2021-08-17T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}.
    """

    timestamp: IncidentTimestampV2ResponseBody
    value: Union[Unset, IncidentTimestampValueV2ResponseBody] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.to_dict()

        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = IncidentTimestampV2ResponseBody.from_dict(d.pop("timestamp"))

        _value = d.pop("value", UNSET)
        value: Union[Unset, IncidentTimestampValueV2ResponseBody]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = IncidentTimestampValueV2ResponseBody.from_dict(_value)

        incident_timestamp_with_value_v2_response_body = cls(
            timestamp=timestamp,
            value=value,
        )

        incident_timestamp_with_value_v2_response_body.additional_properties = d
        return incident_timestamp_with_value_v2_response_body

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
