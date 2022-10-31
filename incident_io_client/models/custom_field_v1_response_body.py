import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.custom_field_option_v1_response_body import (
    CustomFieldOptionV1ResponseBody,
)
from ..models.custom_field_v1_response_body_field_type import (
    CustomFieldV1ResponseBodyFieldType,
)
from ..models.custom_field_v1_response_body_required import (
    CustomFieldV1ResponseBodyRequired,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldV1ResponseBody")


@attr.s(auto_attribs=True)
class CustomFieldV1ResponseBody:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Which team is impacted by this issue',
            'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key':
            10, 'value': 'Product'}], 'required': 'never', 'show_before_closure': True, 'show_before_creation': True,
            'show_in_announcement_post': True, 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When the action was created Example: 2021-08-17T13:28:57.801578Z.
        description (str): Description of the custom field Example: Which team is impacted by this issue.
        field_type (CustomFieldV1ResponseBodyFieldType): Type of custom field Example: single_select.
        id (str): Unique identifier for the custom field Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Human readable name for the custom field Example: Affected Team.
        options (List[CustomFieldOptionV1ResponseBody]): What options are available for this custom field, if this field
            has options Example: [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'sort_key': 10, 'value': 'Product'}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}].
        required (CustomFieldV1ResponseBodyRequired): When this custom field must be set during the incident lifecycle.
            Example: never.
        show_before_closure (bool): Whether a custom field should be shown in the incident close modal. If this custom
            field is required before closure, but no value has been set for it, the field will be shown in the closure modal
            whatever the value of this setting. Example: True.
        show_before_creation (bool): Whether a custom field should be shown in the incident creation modal. This must be
            true if the field is always required. Example: True.
        updated_at (datetime.datetime): When the action was last updated Example: 2021-08-17T13:28:57.801578Z.
        show_in_announcement_post (Union[Unset, bool]): Whether a custom field should be shown in the list of fields as
            part of the announcement post when set. Example: True.
    """

    created_at: datetime.datetime
    description: str
    field_type: CustomFieldV1ResponseBodyFieldType
    id: str
    name: str
    options: List[CustomFieldOptionV1ResponseBody]
    required: CustomFieldV1ResponseBodyRequired
    show_before_closure: bool
    show_before_creation: bool
    updated_at: datetime.datetime
    show_in_announcement_post: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description
        field_type = self.field_type.value

        id = self.id
        name = self.name
        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()

            options.append(options_item)

        required = self.required.value

        show_before_closure = self.show_before_closure
        show_before_creation = self.show_before_creation
        updated_at = self.updated_at.isoformat()

        show_in_announcement_post = self.show_in_announcement_post

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "field_type": field_type,
                "id": id,
                "name": name,
                "options": options,
                "required": required,
                "show_before_closure": show_before_closure,
                "show_before_creation": show_before_creation,
                "updated_at": updated_at,
            }
        )
        if show_in_announcement_post is not UNSET:
            field_dict["show_in_announcement_post"] = show_in_announcement_post

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        description = d.pop("description")

        field_type = CustomFieldV1ResponseBodyFieldType(d.pop("field_type"))

        id = d.pop("id")

        name = d.pop("name")

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = CustomFieldOptionV1ResponseBody.from_dict(options_item_data)

            options.append(options_item)

        required = CustomFieldV1ResponseBodyRequired(d.pop("required"))

        show_before_closure = d.pop("show_before_closure")

        show_before_creation = d.pop("show_before_creation")

        updated_at = isoparse(d.pop("updated_at"))

        show_in_announcement_post = d.pop("show_in_announcement_post", UNSET)

        custom_field_v1_response_body = cls(
            created_at=created_at,
            description=description,
            field_type=field_type,
            id=id,
            name=name,
            options=options,
            required=required,
            show_before_closure=show_before_closure,
            show_before_creation=show_before_creation,
            updated_at=updated_at,
            show_in_announcement_post=show_in_announcement_post,
        )

        custom_field_v1_response_body.additional_properties = d
        return custom_field_v1_response_body

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
