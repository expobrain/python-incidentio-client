import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.custom_field_option_response_body import CustomFieldOptionResponseBody
from ..models.custom_field_response_body_field_type import (
    CustomFieldResponseBodyFieldType,
)

T = TypeVar("T", bound="CustomFieldResponseBody")


@attr.s(auto_attribs=True)
class CustomFieldResponseBody:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Which team is impacted by this issue',
            'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key':
            10, 'value': 'Product'}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'sort_key': 10, 'value': 'Product'}], 'require_before_closure': True, 'require_before_creation': True,
            'show_before_closure': True, 'show_before_creation': True, 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When the action was created Example: 2021-08-17T13:28:57.801578Z.
        description (str): Description of the custom field Example: Which team is impacted by this issue.
        field_type (CustomFieldResponseBodyFieldType): Type of custom field Example: single_select.
        id (str): Unique identifier for the custom field Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Human readable name for the custom field Example: Affected Team.
        options (List[CustomFieldOptionResponseBody]): What options are available for this custom field, if this field
            has options Example: [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'sort_key': 10, 'value': 'Product'}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}, {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}].
        require_before_closure (bool): Whether a custom field should be required in the incident close modal Example:
            True.
        require_before_creation (bool): Whether a custom field should be required in the incident creation modal
            Example: True.
        show_before_closure (bool): Whether a custom field should be shown in the incident close modal Example: True.
        show_before_creation (bool): Whether a custom field should be shown in the incident creation modal Example:
            True.
        updated_at (datetime.datetime): When the action was last updated Example: 2021-08-17T13:28:57.801578Z.
    """

    created_at: datetime.datetime
    description: str
    field_type: CustomFieldResponseBodyFieldType
    id: str
    name: str
    options: List[CustomFieldOptionResponseBody]
    require_before_closure: bool
    require_before_creation: bool
    show_before_closure: bool
    show_before_creation: bool
    updated_at: datetime.datetime
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

        require_before_closure = self.require_before_closure
        require_before_creation = self.require_before_creation
        show_before_closure = self.show_before_closure
        show_before_creation = self.show_before_creation
        updated_at = self.updated_at.isoformat()

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
                "require_before_closure": require_before_closure,
                "require_before_creation": require_before_creation,
                "show_before_closure": show_before_closure,
                "show_before_creation": show_before_creation,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        description = d.pop("description")

        field_type = CustomFieldResponseBodyFieldType(d.pop("field_type"))

        id = d.pop("id")

        name = d.pop("name")

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = CustomFieldOptionResponseBody.from_dict(options_item_data)

            options.append(options_item)

        require_before_closure = d.pop("require_before_closure")

        require_before_creation = d.pop("require_before_creation")

        show_before_closure = d.pop("show_before_closure")

        show_before_creation = d.pop("show_before_creation")

        updated_at = isoparse(d.pop("updated_at"))

        custom_field_response_body = cls(
            created_at=created_at,
            description=description,
            field_type=field_type,
            id=id,
            name=name,
            options=options,
            require_before_closure=require_before_closure,
            require_before_creation=require_before_creation,
            show_before_closure=show_before_closure,
            show_before_creation=show_before_creation,
            updated_at=updated_at,
        )

        custom_field_response_body.additional_properties = d
        return custom_field_response_body

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
