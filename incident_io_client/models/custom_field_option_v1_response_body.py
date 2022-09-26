from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CustomFieldOptionV1ResponseBody")


@attr.s(auto_attribs=True)
class CustomFieldOptionV1ResponseBody:
    """
    Example:
        {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}

    Attributes:
        custom_field_id (str): ID of the custom field this option belongs to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        id (str): Unique identifier for the custom field option Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        sort_key (int): Sort key used to order the custom field options correctly Default: 1000. Example: 10.
        value (str): Human readable name for the custom field option Example: Product.
    """

    custom_field_id: str
    id: str
    value: str
    sort_key: int = 1000
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_field_id = self.custom_field_id
        id = self.id
        sort_key = self.sort_key
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field_id": custom_field_id,
                "id": id,
                "sort_key": sort_key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        custom_field_id = d.pop("custom_field_id")

        id = d.pop("id")

        sort_key = d.pop("sort_key")

        value = d.pop("value")

        custom_field_option_v1_response_body = cls(
            custom_field_id=custom_field_id,
            id=id,
            sort_key=sort_key,
            value=value,
        )

        custom_field_option_v1_response_body.additional_properties = d
        return custom_field_option_v1_response_body

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
