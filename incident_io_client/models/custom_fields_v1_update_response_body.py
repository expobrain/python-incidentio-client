from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_field_v1_response_body import CustomFieldV1ResponseBody


T = TypeVar("T", bound="CustomFieldsV1UpdateResponseBody")


@_attrs_define
class CustomFieldsV1UpdateResponseBody:
    """
    Example:
        {'custom_field': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}],
            'required': 'never', 'required_v2': 'never', 'show_before_closure': True, 'show_before_creation': True,
            'show_before_update': True, 'show_in_announcement_post': True, 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        custom_field (CustomFieldV1ResponseBody):  Example: {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Which team is impacted by this issue',
            'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}], 'required': 'never', 'required_v2': 'never', 'show_before_closure': True, 'show_before_creation':
            True, 'show_before_update': True, 'show_in_announcement_post': True, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
    """

    custom_field: "CustomFieldV1ResponseBody"
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
        from ..models.custom_field_v1_response_body import CustomFieldV1ResponseBody

        d = src_dict.copy()
        custom_field = CustomFieldV1ResponseBody.from_dict(d.pop("custom_field"))

        custom_fields_v1_update_response_body = cls(
            custom_field=custom_field,
        )

        custom_fields_v1_update_response_body.additional_properties = d
        return custom_fields_v1_update_response_body

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
