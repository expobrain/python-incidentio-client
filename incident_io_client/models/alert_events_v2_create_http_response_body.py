from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_events_v2_create_http_response_body_deduplication_key import (
    AlertEventsV2CreateHTTPResponseBodyDeduplicationKey,
)
from ..models.alert_events_v2_create_http_response_body_message import (
    AlertEventsV2CreateHTTPResponseBodyMessage,
)
from ..models.alert_events_v2_create_http_response_body_status import (
    AlertEventsV2CreateHTTPResponseBodyStatus,
)

T = TypeVar("T", bound="AlertEventsV2CreateHTTPResponseBody")


@_attrs_define
class AlertEventsV2CreateHTTPResponseBody:
    """
    Example:
        {'deduplication_key': 'unique-key', 'message': 'Event accepted for processing', 'status': 'success'}

    Attributes:
        deduplication_key (AlertEventsV2CreateHTTPResponseBodyDeduplicationKey): The deduplication key that the event
            has been processed with Example: unique-key.
        message (AlertEventsV2CreateHTTPResponseBodyMessage): Human readable message giving detail about the event
            Example: Event accepted for processing.
        status (AlertEventsV2CreateHTTPResponseBodyStatus): Status of the event Example: success.
    """

    deduplication_key: AlertEventsV2CreateHTTPResponseBodyDeduplicationKey
    message: AlertEventsV2CreateHTTPResponseBodyMessage
    status: AlertEventsV2CreateHTTPResponseBodyStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deduplication_key = self.deduplication_key.value

        message = self.message.value

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deduplication_key": deduplication_key,
                "message": message,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        deduplication_key = AlertEventsV2CreateHTTPResponseBodyDeduplicationKey(
            d.pop("deduplication_key")
        )

        message = AlertEventsV2CreateHTTPResponseBodyMessage(d.pop("message"))

        status = AlertEventsV2CreateHTTPResponseBodyStatus(d.pop("status"))

        alert_events_v2_create_http_response_body = cls(
            deduplication_key=deduplication_key,
            message=message,
            status=status,
        )

        alert_events_v2_create_http_response_body.additional_properties = d
        return alert_events_v2_create_http_response_body

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
