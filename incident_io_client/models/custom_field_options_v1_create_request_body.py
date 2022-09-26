from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldOptionsV1CreateRequestBody")


@attr.s(auto_attribs=True)
class CustomFieldOptionsV1CreateRequestBody:
    """
    Example:
        {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}

    Attributes:
        custom_field_id (str): ID of the custom field this option belongs to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        value (str): Human readable name for the custom field option Example: Product.
        sort_key (Union[Unset, int]): Sort key used to order the custom field options correctly Default: 1000. Example:
            10.
    """

    custom_field_id: str
    value: str
    sort_key: Union[Unset, int] = 1000
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_field_id = self.custom_field_id
        value = self.value
        sort_key = self.sort_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field_id": custom_field_id,
                "value": value,
            }
        )
        if sort_key is not UNSET:
            field_dict["sort_key"] = sort_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        custom_field_id = d.pop("custom_field_id")

        value = d.pop("value")

        sort_key = d.pop("sort_key", UNSET)

        custom_field_options_v1_create_request_body = cls(
            custom_field_id=custom_field_id,
            value=value,
            sort_key=sort_key,
        )

        custom_field_options_v1_create_request_body.additional_properties = d
        return custom_field_options_v1_create_request_body

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
