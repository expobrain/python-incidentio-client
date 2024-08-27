from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_field_option_v1 import CustomFieldOptionV1
    from ..models.pagination_meta_result import PaginationMetaResult


T = TypeVar("T", bound="CustomFieldOptionsV1ListResponseBody")


@_attrs_define
class CustomFieldOptionsV1ListResponseBody:
    """
    Example:
        {'custom_field_options': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'sort_key': 10, 'value': 'Product'}], 'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size':
            25}}

    Attributes:
        custom_field_options (List['CustomFieldOptionV1']):  Example: [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}].
        pagination_meta (PaginationMetaResult):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
    """

    custom_field_options: List["CustomFieldOptionV1"]
    pagination_meta: "PaginationMetaResult"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_field_options = []
        for custom_field_options_item_data in self.custom_field_options:
            custom_field_options_item = custom_field_options_item_data.to_dict()
            custom_field_options.append(custom_field_options_item)

        pagination_meta = self.pagination_meta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field_options": custom_field_options,
                "pagination_meta": pagination_meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_option_v1 import CustomFieldOptionV1
        from ..models.pagination_meta_result import PaginationMetaResult

        d = src_dict.copy()
        custom_field_options = []
        _custom_field_options = d.pop("custom_field_options")
        for custom_field_options_item_data in _custom_field_options:
            custom_field_options_item = CustomFieldOptionV1.from_dict(
                custom_field_options_item_data
            )

            custom_field_options.append(custom_field_options_item)

        pagination_meta = PaginationMetaResult.from_dict(d.pop("pagination_meta"))

        custom_field_options_v1_list_response_body = cls(
            custom_field_options=custom_field_options,
            pagination_meta=pagination_meta,
        )

        custom_field_options_v1_list_response_body.additional_properties = d
        return custom_field_options_v1_list_response_body

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
