from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CustomFieldsV2UpdateRequestBody")


@_attrs_define
class CustomFieldsV2UpdateRequestBody:
    """
    Example:
        {'description': 'Which team is impacted by this issue', 'name': 'Affected Team'}

    Attributes:
        description (str): Description of the custom field Example: Which team is impacted by this issue.
        name (str): Human readable name for the custom field Example: Affected Team.
    """

    description: str
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        name = d.pop("name")

        custom_fields_v2_update_request_body = cls(
            description=description,
            name=name,
        )

        custom_fields_v2_update_request_body.additional_properties = d
        return custom_fields_v2_update_request_body

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
