from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.custom_fields_v1_create_request_body_field_type import (
    CustomFieldsV1CreateRequestBodyFieldType,
)
from ..models.custom_fields_v1_create_request_body_required import (
    CustomFieldsV1CreateRequestBodyRequired,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldsV1CreateRequestBody")


@attr.s(auto_attribs=True)
class CustomFieldsV1CreateRequestBody:
    """
    Example:
        {'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team',
            'required': 'never', 'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post':
            True}

    Attributes:
        description (str): Description of the custom field Example: Which team is impacted by this issue.
        field_type (CustomFieldsV1CreateRequestBodyFieldType): Type of custom field Example: single_select.
        name (str): Human readable name for the custom field Example: Affected Team.
        required (CustomFieldsV1CreateRequestBodyRequired): When this custom field must be set during the incident
            lifecycle. Example: never.
        show_before_closure (bool): Whether a custom field should be shown in the incident close modal. If this custom
            field is required before closure, but no value has been set for it, the field will be shown in the closure modal
            whatever the value of this setting. Example: True.
        show_before_creation (bool): Whether a custom field should be shown in the incident creation modal. This must be
            true if the field is always required. Example: True.
        show_in_announcement_post (Union[Unset, bool]): Whether a custom field should be shown in the list of fields as
            part of the announcement post when set. Example: True.
    """

    description: str
    field_type: CustomFieldsV1CreateRequestBodyFieldType
    name: str
    required: CustomFieldsV1CreateRequestBodyRequired
    show_before_closure: bool
    show_before_creation: bool
    show_in_announcement_post: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        field_type = self.field_type.value

        name = self.name
        required = self.required.value

        show_before_closure = self.show_before_closure
        show_before_creation = self.show_before_creation
        show_in_announcement_post = self.show_in_announcement_post

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
        if show_in_announcement_post is not UNSET:
            field_dict["show_in_announcement_post"] = show_in_announcement_post

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        field_type = CustomFieldsV1CreateRequestBodyFieldType(d.pop("field_type"))

        name = d.pop("name")

        required = CustomFieldsV1CreateRequestBodyRequired(d.pop("required"))

        show_before_closure = d.pop("show_before_closure")

        show_before_creation = d.pop("show_before_creation")

        show_in_announcement_post = d.pop("show_in_announcement_post", UNSET)

        custom_fields_v1_create_request_body = cls(
            description=description,
            field_type=field_type,
            name=name,
            required=required,
            show_before_closure=show_before_closure,
            show_before_creation=show_before_creation,
            show_in_announcement_post=show_in_announcement_post,
        )

        custom_fields_v1_create_request_body.additional_properties = d
        return custom_fields_v1_create_request_body

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
