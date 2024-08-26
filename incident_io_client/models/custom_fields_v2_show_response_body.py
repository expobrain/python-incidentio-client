from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_field_v2 import CustomFieldV2


T = TypeVar("T", bound="CustomFieldsV2ShowResponseBody")


@_attrs_define
class CustomFieldsV2ShowResponseBody:
    """
    Example:
        {'custom_field': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        custom_field (CustomFieldV2):  Example: {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Which team is impacted by this issue', 'field_type':
            'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
    """

    custom_field: "CustomFieldV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_field = self.custom_field.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field": custom_field,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_v2 import CustomFieldV2

        d = src_dict.copy()
        custom_field = CustomFieldV2.from_dict(d.pop("custom_field"))

        custom_fields_v2_show_response_body = cls(
            custom_field=custom_field,
        )

        custom_fields_v2_show_response_body.additional_properties = d
        return custom_fields_v2_show_response_body

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
