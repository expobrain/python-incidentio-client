from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.custom_field_type_info_v1_response_body import (
        CustomFieldTypeInfoV1ResponseBody,
    )
    from ..models.custom_field_value_v1_response_body import (
        CustomFieldValueV1ResponseBody,
    )


T = TypeVar("T", bound="CustomFieldEntryV1ResponseBody")


@attr.s(auto_attribs=True)
class CustomFieldEntryV1ResponseBody:
    """
    Example:
        {'custom_field': {'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}]},
            'values': [{'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}]}

    Attributes:
        custom_field (CustomFieldTypeInfoV1ResponseBody):  Example: {'description': 'Which team is impacted by this
            issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}]}.
        values (List['CustomFieldValueV1ResponseBody']): List of custom field values set on this entry Example:
            [{'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}].
    """

    custom_field: "CustomFieldTypeInfoV1ResponseBody"
    values: List["CustomFieldValueV1ResponseBody"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_field = self.custom_field.to_dict()

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()

            values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field": custom_field,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_type_info_v1_response_body import (
            CustomFieldTypeInfoV1ResponseBody,
        )
        from ..models.custom_field_value_v1_response_body import (
            CustomFieldValueV1ResponseBody,
        )

        d = src_dict.copy()
        custom_field = CustomFieldTypeInfoV1ResponseBody.from_dict(d.pop("custom_field"))

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = CustomFieldValueV1ResponseBody.from_dict(values_item_data)

            values.append(values_item)

        custom_field_entry_v1_response_body = cls(
            custom_field=custom_field,
            values=values,
        )

        custom_field_entry_v1_response_body.additional_properties = d
        return custom_field_entry_v1_response_body

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
