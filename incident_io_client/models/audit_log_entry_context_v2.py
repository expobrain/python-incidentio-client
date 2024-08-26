from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogEntryContextV2")


@_attrs_define
class AuditLogEntryContextV2:
    """
    Example:
        {'location': '1.2.3.4', 'user_agent': 'Chrome/91.0.4472.114'}

    Attributes:
        location (str): The location of the actor that performed this action Example: 1.2.3.4.
        user_agent (Union[Unset, str]): The user agent of the actor that performed this action Example:
            Chrome/91.0.4472.114.
    """

    location: str
    user_agent: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location = self.location

        user_agent = self.user_agent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
            }
        )
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        location = d.pop("location")

        user_agent = d.pop("user_agent", UNSET)

        audit_log_entry_context_v2 = cls(
            location=location,
            user_agent=user_agent,
        )

        audit_log_entry_context_v2.additional_properties = d
        return audit_log_entry_context_v2

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
