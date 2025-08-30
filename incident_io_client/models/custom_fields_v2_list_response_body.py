from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_field_v2 import CustomFieldV2


T = TypeVar("T", bound="CustomFieldsV2ListResponseBody")


@_attrs_define
class CustomFieldsV2ListResponseBody:
    """
    Example:
        {'custom_fields': [{'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Which team is impacted by this issue', 'field_type':
            'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        custom_fields (list['CustomFieldV2']):  Example: [{'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Which team is impacted by this issue',
            'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}].
    """

    custom_fields: list["CustomFieldV2"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_fields = []
        for custom_fields_item_data in self.custom_fields:
            custom_fields_item = custom_fields_item_data.to_dict()
            custom_fields.append(custom_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_fields": custom_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_v2 import CustomFieldV2

        d = dict(src_dict)
        custom_fields = []
        _custom_fields = d.pop("custom_fields")
        for custom_fields_item_data in _custom_fields:
            custom_fields_item = CustomFieldV2.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        custom_fields_v2_list_response_body = cls(
            custom_fields=custom_fields,
        )

        custom_fields_v2_list_response_body.additional_properties = d
        return custom_fields_v2_list_response_body

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
