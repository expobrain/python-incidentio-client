from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.catalog_v2_create_entry_request_body_attribute_values import (
        CatalogV2CreateEntryRequestBodyAttributeValues,
    )


T = TypeVar("T", bound="CatalogV2CreateEntryRequestBody")


@attr.s(auto_attribs=True)
class CatalogV2CreateEntryRequestBody:
    """
    Example:
        {'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}},
            'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}

    Attributes:
        attribute_values (CatalogV2CreateEntryRequestBodyAttributeValues): Values of this entry Example: {'abc123':
            {'array_value': [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}}.
        catalog_type_id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Name is the human readable name of this entry Example: Primary On-call.
    """

    attribute_values: "CatalogV2CreateEntryRequestBodyAttributeValues"
    catalog_type_id: str
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_values = self.attribute_values.to_dict()

        catalog_type_id = self.catalog_type_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_values": attribute_values,
                "catalog_type_id": catalog_type_id,
                "name": name,
            }
        )

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

        catalog_v2_create_entry_request_body = cls(
            attribute_values=attribute_values,
            catalog_type_id=catalog_type_id,
            name=name,
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
