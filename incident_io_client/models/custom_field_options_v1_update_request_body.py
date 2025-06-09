from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CustomFieldOptionsV1UpdateRequestBody")


@_attrs_define
class CustomFieldOptionsV1UpdateRequestBody:
    """
    Example:
        {'sort_key': 10, 'value': 'Product'}

    Attributes:
        sort_key (int): Sort key used to order the custom field options correctly Default: 1000. Example: 10.
        value (str): Human readable name for the custom field option Example: Product.
    """

    value: str
    sort_key: int = 1000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sort_key = self.sort_key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sort_key": sort_key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sort_key = d.pop("sort_key")

        value = d.pop("value")

        custom_field_options_v1_update_request_body = cls(
            sort_key=sort_key,
            value=value,
        )

        custom_field_options_v1_update_request_body.additional_properties = d
        return custom_field_options_v1_update_request_body

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
