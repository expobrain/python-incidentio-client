from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_v2_create_entry_request_body_attribute_values import (
        CatalogV2CreateEntryRequestBodyAttributeValues,
    )


T = TypeVar("T", bound="CatalogV2CreateEntryRequestBody")


@_attrs_define
class CatalogV2CreateEntryRequestBody:
    """
    Example:
        {'aliases': ['lawrence@incident.io', 'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank': 3}

    Attributes:
        attribute_values (CatalogV2CreateEntryRequestBodyAttributeValues): Values of this entry Example: {'abc123':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}.
        catalog_type_id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Name is the human readable name of this entry Example: Primary On-call.
        aliases (Union[Unset, List[str]]): Optional aliases that can be used to reference this entry Example:
            ['lawrence@incident.io', 'lawrence'].
        external_id (Union[Unset, str]): An optional alternative ID for this entry, which is ensured to be unique for
            the type Example: 761722cd-d1d7-477b-ac7e-90f9e079dc33.
        rank (Union[Unset, int]): When catalog type is ranked, this is used to help order things Example: 3.
    """

    attribute_values: "CatalogV2CreateEntryRequestBodyAttributeValues"
    catalog_type_id: str
    name: str
    aliases: Union[Unset, List[str]] = UNSET
    external_id: Union[Unset, str] = UNSET
    rank: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_values = self.attribute_values.to_dict()

        catalog_type_id = self.catalog_type_id

        name = self.name

        aliases: Union[Unset, List[str]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        external_id = self.external_id

        rank = self.rank

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_values": attribute_values,
                "catalog_type_id": catalog_type_id,
                "name": name,
            }
        )
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_v2_create_entry_request_body_attribute_values import (
            CatalogV2CreateEntryRequestBodyAttributeValues,
        )

        d = src_dict.copy()
        attribute_values = CatalogV2CreateEntryRequestBodyAttributeValues.from_dict(
            d.pop("attribute_values")
        )

        catalog_type_id = d.pop("catalog_type_id")

        name = d.pop("name")

        aliases = cast(List[str], d.pop("aliases", UNSET))

        external_id = d.pop("external_id", UNSET)

        rank = d.pop("rank", UNSET)

        catalog_v2_create_entry_request_body = cls(
            attribute_values=attribute_values,
            catalog_type_id=catalog_type_id,
            name=name,
            aliases=aliases,
            external_id=external_id,
            rank=rank,
        )

        catalog_v2_create_entry_request_body.additional_properties = d
        return catalog_v2_create_entry_request_body

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
