from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.custom_fields_create_request_body_field_type import (
    CustomFieldsCreateRequestBodyFieldType,
)
from ..models.custom_fields_create_request_body_required import (
    CustomFieldsCreateRequestBodyRequired,
)

T = TypeVar("T", bound="CustomFieldsCreateRequestBody")


@attr.s(auto_attribs=True)
class CustomFieldsCreateRequestBody:
    """
    Example:
        {'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team',
            'required': 'never', 'show_before_closure': True, 'show_before_creation': True}

    Attributes:
        description (str): Description of the custom field Example: Which team is impacted by this issue.
        field_type (CustomFieldsCreateRequestBodyFieldType): Type of custom field Example: single_select.
        name (str): Human readable name for the custom field Example: Affected Team.
        required (CustomFieldsCreateRequestBodyRequired): When this custom field must be set during the incident
            lifecycle. Example: never.
        show_before_closure (bool): Whether a custom field should be shown in the incident close modal. If this custom
            field is required before closure, but no value has been set for it, the field will be shown in the closure modal
            whatever the value of this setting. Example: True.
        show_before_creation (bool): Whether a custom field should be shown in the incident creation modal. This must be
            true if the field is always required. Example: True.
    """

    description: str
    field_type: CustomFieldsCreateRequestBodyFieldType
    name: str
    required: CustomFieldsCreateRequestBodyRequired
    show_before_closure: bool
    show_before_creation: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        field_type = self.field_type.value

        name = self.name
        required = self.required.value

        show_before_closure = self.show_before_closure
        show_before_creation = self.show_before_creation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "field_type": field_type,
                "name": name,
                "required": required,
                "show_before_closure": show_before_closure,
                "show_before_creation": show_before_creation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        field_type = CustomFieldsCreateRequestBodyFieldType(d.pop("field_type"))

        name = d.pop("name")

        required = CustomFieldsCreateRequestBodyRequired(d.pop("required"))

        show_before_closure = d.pop("show_before_closure")

        show_before_creation = d.pop("show_before_creation")

        custom_fields_create_request_body = cls(
            description=description,
            field_type=field_type,
            name=name,
            required=required,
            show_before_closure=show_before_closure,
            show_before_creation=show_before_creation,
        )

        custom_fields_create_request_body.additional_properties = d
        return custom_fields_create_request_body

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
