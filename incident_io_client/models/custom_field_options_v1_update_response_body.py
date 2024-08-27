from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_field_option_v1 import CustomFieldOptionV1


T = TypeVar("T", bound="CustomFieldOptionsV1UpdateResponseBody")


@_attrs_define
class CustomFieldOptionsV1UpdateResponseBody:
    """
    Example:
        {'custom_field_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'sort_key': 10, 'value': 'Product'}}

    Attributes:
        custom_field_option (CustomFieldOptionV1):  Example: {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}.
    """

    custom_field_option: "CustomFieldOptionV1"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_field_option = self.custom_field_option.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field_option": custom_field_option,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_option_v1 import CustomFieldOptionV1

        d = src_dict.copy()
        custom_field_option = CustomFieldOptionV1.from_dict(d.pop("custom_field_option"))

        custom_field_options_v1_update_response_body = cls(
            custom_field_option=custom_field_option,
        )

        custom_field_options_v1_update_response_body.additional_properties = d
        return custom_field_options_v1_update_response_body

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
