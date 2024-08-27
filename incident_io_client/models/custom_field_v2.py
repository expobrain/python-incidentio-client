import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.custom_field_v2_field_type import CustomFieldV2FieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldV2")


@_attrs_define
class CustomFieldV2:
    """
    Example:
        {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Which team is impacted by this issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Affected Team', 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When the action was created Example: 2021-08-17T13:28:57.801578Z.
        description (str): Description of the custom field Example: Which team is impacted by this issue.
        field_type (CustomFieldV2FieldType): Type of custom field Example: single_select.
        id (str): Unique identifier for the custom field Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Human readable name for the custom field Example: Affected Team.
        updated_at (datetime.datetime): When the action was last updated Example: 2021-08-17T13:28:57.801578Z.
        catalog_type_id (Union[Unset, str]): For catalog fields, the ID of the associated catalog type Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
    """

    created_at: datetime.datetime
    description: str
    field_type: CustomFieldV2FieldType
    id: str
    name: str
    updated_at: datetime.datetime
    catalog_type_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description

        field_type = self.field_type.value

        id = self.id

        name = self.name

        updated_at = self.updated_at.isoformat()

        catalog_type_id = self.catalog_type_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "field_type": field_type,
                "id": id,
                "name": name,
                "updated_at": updated_at,
            }
        )
        if catalog_type_id is not UNSET:
            field_dict["catalog_type_id"] = catalog_type_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        description = d.pop("description")

        field_type = CustomFieldV2FieldType(d.pop("field_type"))

        id = d.pop("id")

        name = d.pop("name")

        updated_at = isoparse(d.pop("updated_at"))

        catalog_type_id = d.pop("catalog_type_id", UNSET)

        custom_field_v2 = cls(
            created_at=created_at,
            description=description,
            field_type=field_type,
            id=id,
            name=name,
            updated_at=updated_at,
            catalog_type_id=catalog_type_id,
        )

        custom_field_v2.additional_properties = d
        return custom_field_v2

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
