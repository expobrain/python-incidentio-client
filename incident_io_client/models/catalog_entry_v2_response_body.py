import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.catalog_entry_v2_response_body_attribute_values import (
        CatalogEntryV2ResponseBodyAttributeValues,
    )


T = TypeVar("T", bound="CatalogEntryV2ResponseBody")


@attr.s(auto_attribs=True)
class CatalogEntryV2ResponseBody:
    """
    Example:
        {'attribute_values': {'abc123': {'array_value': [{'catalog_entry': {'catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'image_url':
            'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon':
            False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}], 'value': {'catalog_entry':
            {'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'image_url': 'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg',
            'is_image_slack_icon': False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}}},
            'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call', 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        attribute_values (CatalogEntryV2ResponseBodyAttributeValues): Values of this entry Example: {'abc123':
            {'array_value': [{'catalog_entry': {'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}], 'value': {'catalog_entry': {'catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'image_url':
            'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon':
            False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}}}.
        catalog_type_id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        created_at (datetime.datetime): When this entry was created Example: 2021-08-17T13:28:57.801578Z.
        id (str): ID of this resource Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Name is the human readable name of this entry Example: Primary On-call.
        updated_at (datetime.datetime): When this entry was last updated Example: 2021-08-17T13:28:57.801578Z.
    """

    attribute_values: "CatalogEntryV2ResponseBodyAttributeValues"
    catalog_type_id: str
    created_at: datetime.datetime
    id: str
    name: str
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_values = self.attribute_values.to_dict()

        catalog_type_id = self.catalog_type_id
        created_at = self.created_at.isoformat()

        id = self.id
        name = self.name
        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_values": attribute_values,
                "catalog_type_id": catalog_type_id,
                "created_at": created_at,
                "id": id,
                "name": name,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_entry_v2_response_body_attribute_values import (
            CatalogEntryV2ResponseBodyAttributeValues,
        )

        d = src_dict.copy()
        attribute_values = CatalogEntryV2ResponseBodyAttributeValues.from_dict(
            d.pop("attribute_values")
        )

        catalog_type_id = d.pop("catalog_type_id")

        created_at = isoparse(d.pop("created_at"))

        id = d.pop("id")

        name = d.pop("name")

        updated_at = isoparse(d.pop("updated_at"))

        catalog_entry_v2_response_body = cls(
            attribute_values=attribute_values,
            catalog_type_id=catalog_type_id,
            created_at=created_at,
            id=id,
            name=name,
            updated_at=updated_at,
        )

        catalog_entry_v2_response_body.additional_properties = d
        return catalog_entry_v2_response_body

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
