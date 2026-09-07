from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ErrorSource")


@_attrs_define
class ErrorSource:
    """
    Example:
        {'field': 'default_call_url', 'pointer': '/settings/default_call_url'}

    Attributes:
        field (str): Field name that is the source of the error Example: default_call_url.
        pointer (str): JSON pointer to the request field that is the source of the error Example:
            /settings/default_call_url.
    """

    field: str
    pointer: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field = self.field

        pointer = self.pointer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "pointer": pointer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field = d.pop("field")

        pointer = d.pop("pointer")

        error_source = cls(
            field=field,
            pointer=pointer,
        )

        error_source.additional_properties = d
        return error_source

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
