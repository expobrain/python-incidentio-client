import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_entry_v2_response_body_attribute_values import (
        CatalogEntryV2ResponseBodyAttributeValues,
    )


T = TypeVar("T", bound="CatalogEntryV2ResponseBody")


@_attrs_define
class CatalogEntryV2ResponseBody:
    """
    Example:
        {'aliases': ['lawrence@incident.io', 'lawrence'], 'archived_at': '2021-08-17T14:28:57.801578Z',
            'attribute_values': {'abc123': {'array_value': [{'catalog_entry': {'archived_at': '2021-08-17T14:28:57.801578Z',
            'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'Collection of standalone automations like auto-closing incidents.',
            'image_url': 'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg',
            'is_image_slack_icon': False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity',
            'sort_key': '000020', 'unavailable': False, 'value': 'abc123'}], 'value': {'catalog_entry': {'archived_at':
            '2021-08-17T14:28:57.801578Z', 'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary
            escalation', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'Collection of standalone automations
            like auto-closing incidents.', 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity', 'sort_key': '000020', 'unavailable':
            False, 'value': 'abc123'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call', 'rank': 3, 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        aliases (List[str]): Optional aliases that can be used to reference this entry Example: ['lawrence@incident.io',
            'lawrence'].
        attribute_values (CatalogEntryV2ResponseBodyAttributeValues): Values of this entry Example: {'abc123':
            {'array_value': [{'catalog_entry': {'archived_at': '2021-08-17T14:28:57.801578Z', 'catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'Collection of standalone automations like auto-closing incidents.',
            'image_url': 'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg',
            'is_image_slack_icon': False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity',
            'sort_key': '000020', 'unavailable': False, 'value': 'abc123'}], 'value': {'catalog_entry': {'archived_at':
            '2021-08-17T14:28:57.801578Z', 'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary
            escalation', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'Collection of standalone automations
            like auto-closing incidents.', 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity', 'sort_key': '000020', 'unavailable':
            False, 'value': 'abc123'}}}.
        catalog_type_id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        created_at (datetime.datetime): When this entry was created Example: 2021-08-17T13:28:57.801578Z.
        id (str): ID of this catalog entry Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Name is the human readable name of this entry Example: Primary On-call.
        rank (int): When catalog type is ranked, this is used to help order things Example: 3.
        updated_at (datetime.datetime): When this entry was last updated Example: 2021-08-17T13:28:57.801578Z.
        archived_at (Union[Unset, datetime.datetime]): When this entry was archived Example:
            2021-08-17T14:28:57.801578Z.
        external_id (Union[Unset, str]): An optional alternative ID for this entry, which is ensured to be unique for
            the type Example: 761722cd-d1d7-477b-ac7e-90f9e079dc33.
    """

    aliases: List[str]
    attribute_values: "CatalogEntryV2ResponseBodyAttributeValues"
    catalog_type_id: str
    created_at: datetime.datetime
    id: str
    name: str
    rank: int
    updated_at: datetime.datetime
    archived_at: Union[Unset, datetime.datetime] = UNSET
    external_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aliases = self.aliases

        attribute_values = self.attribute_values.to_dict()

        catalog_type_id = self.catalog_type_id
        created_at = self.created_at.isoformat()

        id = self.id
        name = self.name
        rank = self.rank
        updated_at = self.updated_at.isoformat()

        archived_at: Union[Unset, str] = UNSET
        if not isinstance(self.archived_at, Unset):
            archived_at = self.archived_at.isoformat()

        external_id = self.external_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aliases": aliases,
                "attribute_values": attribute_values,
                "catalog_type_id": catalog_type_id,
                "created_at": created_at,
                "id": id,
                "name": name,
                "rank": rank,
                "updated_at": updated_at,
            }
        )
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_entry_v2_response_body_attribute_values import (
            CatalogEntryV2ResponseBodyAttributeValues,
        )

        d = src_dict.copy()
        aliases = cast(List[str], d.pop("aliases"))

        attribute_values = CatalogEntryV2ResponseBodyAttributeValues.from_dict(
            d.pop("attribute_values")
        )

        catalog_type_id = d.pop("catalog_type_id")

        created_at = isoparse(d.pop("created_at"))

        id = d.pop("id")

        name = d.pop("name")

        rank = d.pop("rank")

        updated_at = isoparse(d.pop("updated_at"))

        _archived_at = d.pop("archived_at", UNSET)
        archived_at: Union[Unset, datetime.datetime]
        if isinstance(_archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = isoparse(_archived_at)

        external_id = d.pop("external_id", UNSET)

        catalog_entry_v2_response_body = cls(
            aliases=aliases,
            attribute_values=attribute_values,
            catalog_type_id=catalog_type_id,
            created_at=created_at,
            id=id,
            name=name,
            rank=rank,
            updated_at=updated_at,
            archived_at=archived_at,
            external_id=external_id,
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
