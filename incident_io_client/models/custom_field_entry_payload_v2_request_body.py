from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_field_value_payload_v2_request_body import (
        CustomFieldValuePayloadV2RequestBody,
    )


T = TypeVar("T", bound="CustomFieldEntryPayloadV2RequestBody")


@_attrs_define
class CustomFieldEntryPayloadV2RequestBody:
    """
    Example:
        {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you
            like it', 'value_timestamp': ''}]}

    Attributes:
        custom_field_id (str): ID of the custom field this entry is linked against Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        values (List['CustomFieldValuePayloadV2RequestBody']): List of values to associate with this entry. Use an empty
            array to unset the value of the custom field. Example: [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you
            like it', 'value_timestamp': ''}].
    """

    custom_field_id: str
    values: List["CustomFieldValuePayloadV2RequestBody"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_field_id = self.custom_field_id
        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()

            values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field_id": custom_field_id,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_value_payload_v2_request_body import (
            CustomFieldValuePayloadV2RequestBody,
        )

        d = src_dict.copy()
        custom_field_id = d.pop("custom_field_id")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = CustomFieldValuePayloadV2RequestBody.from_dict(values_item_data)

            values.append(values_item)

        custom_field_entry_payload_v2_request_body = cls(
            custom_field_id=custom_field_id,
            values=values,
        )

        custom_field_entry_payload_v2_request_body.additional_properties = d
        return custom_field_entry_payload_v2_request_body

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
