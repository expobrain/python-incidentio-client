from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertResult")


@_attrs_define
class AlertResult:
    """
    Example:
        {'deduplication_key': 'unique-key', 'message': 'Event accepted for processing', 'status': 'success'}

    Attributes:
        deduplication_key (str): The deduplication key that the event has been processed with Example: unique-key.
        message (str): Human readable message giving detail about the event Example: Event accepted for processing.
        status (str): Status of the event Example: success.
    """

    deduplication_key: str
    message: str
    status: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deduplication_key = self.deduplication_key

        message = self.message

        status = self.status

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
        deduplication_key = d.pop("deduplication_key")

        message = d.pop("message")

        status = d.pop("status")

        alert_result = cls(
            deduplication_key=deduplication_key,
            message=message,
            status=status,
        )

        alert_result.additional_properties = d
        return alert_result

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
