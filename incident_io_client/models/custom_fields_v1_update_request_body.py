from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_fields_v1_update_request_body_required import (
    CustomFieldsV1UpdateRequestBodyRequired,
)
from ..models.custom_fields_v1_update_request_body_required_v2 import (
    CustomFieldsV1UpdateRequestBodyRequiredV2,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldsV1UpdateRequestBody")


@_attrs_define
class CustomFieldsV1UpdateRequestBody:
    """
    Example:
        {'description': 'Which team is impacted by this issue', 'name': 'Affected Team', 'required': 'never',
            'required_v2': 'never', 'show_before_closure': True, 'show_before_creation': True, 'show_before_update': True,
            'show_in_announcement_post': True}

    Attributes:
        description (str): Description of the custom field Example: Which team is impacted by this issue.
        name (str): Human readable name for the custom field Example: Affected Team.
        show_before_closure (bool): Whether a custom field should be shown in the incident resolve modal. If this custom
            field is required before resolution, but no value has been set for it, the field will be shown in the resolve
            modal whatever the value of this setting. Example: True.
        show_before_creation (bool): Whether a custom field should be shown in the incident creation modal. This must be
            true if the field is always required. Example: True.
        show_before_update (bool): Whether a custom field should be shown in the incident update modal. Example: True.
        required (Union[Unset, CustomFieldsV1UpdateRequestBodyRequired]): When this custom field must be set during the
            incident lifecycle. [DEPRECATED: please use required_v2 instead]. Example: never.
        required_v2 (Union[Unset, CustomFieldsV1UpdateRequestBodyRequiredV2]): When this custom field must be set during
            the incident lifecycle. Example: never.
        show_in_announcement_post (Union[Unset, bool]): Whether a custom field should be shown in the list of fields as
            part of the announcement post when set. Example: True.
    """

    description: str
    name: str
    show_before_closure: bool
    show_before_creation: bool
    show_before_update: bool
    required: Union[Unset, CustomFieldsV1UpdateRequestBodyRequired] = UNSET
    required_v2: Union[Unset, CustomFieldsV1UpdateRequestBodyRequiredV2] = UNSET
    show_in_announcement_post: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        name = self.name

        show_before_closure = self.show_before_closure

        show_before_creation = self.show_before_creation

        show_before_update = self.show_before_update

        required: Union[Unset, str] = UNSET
        if not isinstance(self.required, Unset):
            required = self.required.value

        required_v2: Union[Unset, str] = UNSET
        if not isinstance(self.required_v2, Unset):
            required_v2 = self.required_v2.value

        show_in_announcement_post = self.show_in_announcement_post

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
                "show_before_closure": show_before_closure,
                "show_before_creation": show_before_creation,
                "show_before_update": show_before_update,
            }
        )
        if required is not UNSET:
            field_dict["required"] = required
        if required_v2 is not UNSET:
            field_dict["required_v2"] = required_v2
        if show_in_announcement_post is not UNSET:
            field_dict["show_in_announcement_post"] = show_in_announcement_post

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        name = d.pop("name")

        show_before_closure = d.pop("show_before_closure")

        show_before_creation = d.pop("show_before_creation")

        show_before_update = d.pop("show_before_update")

        _required = d.pop("required", UNSET)
        required: Union[Unset, CustomFieldsV1UpdateRequestBodyRequired]
        if isinstance(_required, Unset):
            required = UNSET
        else:
            required = CustomFieldsV1UpdateRequestBodyRequired(_required)

        _required_v2 = d.pop("required_v2", UNSET)
        required_v2: Union[Unset, CustomFieldsV1UpdateRequestBodyRequiredV2]
        if isinstance(_required_v2, Unset):
            required_v2 = UNSET
        else:
            required_v2 = CustomFieldsV1UpdateRequestBodyRequiredV2(_required_v2)

        show_in_announcement_post = d.pop("show_in_announcement_post", UNSET)

        custom_fields_v1_update_request_body = cls(
            description=description,
            name=name,
            show_before_closure=show_before_closure,
            show_before_creation=show_before_creation,
            show_before_update=show_before_update,
            required=required,
            required_v2=required_v2,
            show_in_announcement_post=show_in_announcement_post,
        )

        custom_fields_v1_update_request_body.additional_properties = d
        return custom_fields_v1_update_request_body

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
