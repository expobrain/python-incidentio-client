import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentTimelineItemsUpdatePayloadV2")


@_attrs_define
class IncidentTimelineItemsUpdatePayloadV2:
    """
    Example:
        {'description': 'Rolled back **payments-api** to v411 after error rate hit 12%.', 'timestamp':
            '2026-09-01T15:30:00Z', 'title': 'Rolled back payments-api'}

    Attributes:
        description (Union[Unset, str]): Description of the timeline item, in markdown. Send an empty string to remove
            it. Example: Rolled back **payments-api** to v411 after error rate hit 12%..
        timestamp (Union[Unset, datetime.datetime]): When the thing this item describes happened. Only editable on a
            custom item. Example: 2026-09-01T15:30:00Z.
        title (Union[Unset, str]): Title of the timeline item Example: Rolled back payments-api.
    """

    description: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        title = d.pop("title", UNSET)

        incident_timeline_items_update_payload_v2 = cls(
            description=description,
            timestamp=timestamp,
            title=title,
        )

        incident_timeline_items_update_payload_v2.additional_properties = d
        return incident_timeline_items_update_payload_v2

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
