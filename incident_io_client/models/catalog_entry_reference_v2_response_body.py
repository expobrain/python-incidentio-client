from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CatalogEntryReferenceV2ResponseBody")


@_attrs_define
class CatalogEntryReferenceV2ResponseBody:
    """
    Example:
        {'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation',
            'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        catalog_entry_id (str): ID of this catalog entry Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        catalog_entry_name (str): The name of this entry Example: Primary escalation.
        catalog_type_id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    catalog_entry_id: str
    catalog_entry_name: str
    catalog_type_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        catalog_entry_id = self.catalog_entry_id
        catalog_entry_name = self.catalog_entry_name
        catalog_type_id = self.catalog_type_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_entry_id": catalog_entry_id,
                "catalog_entry_name": catalog_entry_name,
                "catalog_type_id": catalog_type_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        catalog_entry_id = d.pop("catalog_entry_id")

        catalog_entry_name = d.pop("catalog_entry_name")

        catalog_type_id = d.pop("catalog_type_id")

        catalog_entry_reference_v2_response_body = cls(
            catalog_entry_id=catalog_entry_id,
            catalog_entry_name=catalog_entry_name,
            catalog_type_id=catalog_type_id,
        )

        catalog_entry_reference_v2_response_body.additional_properties = d
        return catalog_entry_reference_v2_response_body

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
