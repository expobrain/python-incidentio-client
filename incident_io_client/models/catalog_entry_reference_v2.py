import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogEntryReferenceV2")


@_attrs_define
class CatalogEntryReferenceV2:
    """
    Example:
        {'archived_at': '2021-08-17T14:28:57.801578Z', 'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'catalog_entry_name': 'Primary escalation', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        catalog_entry_id (str): ID of this catalog entry Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        catalog_entry_name (str): The name of this entry Example: Primary escalation.
        catalog_type_id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        archived_at (Union[Unset, datetime.datetime]): When this entry was archived Example:
            2021-08-17T14:28:57.801578Z.
    """

    catalog_entry_id: str
    catalog_entry_name: str
    catalog_type_id: str
    archived_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        catalog_entry_id = self.catalog_entry_id

        catalog_entry_name = self.catalog_entry_name

        catalog_type_id = self.catalog_type_id

        archived_at: Union[Unset, str] = UNSET
        if not isinstance(self.archived_at, Unset):
            archived_at = self.archived_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_entry_id": catalog_entry_id,
                "catalog_entry_name": catalog_entry_name,
                "catalog_type_id": catalog_type_id,
            }
        )
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        catalog_entry_id = d.pop("catalog_entry_id")

        catalog_entry_name = d.pop("catalog_entry_name")

        catalog_type_id = d.pop("catalog_type_id")

        _archived_at = d.pop("archived_at", UNSET)
        archived_at: Union[Unset, datetime.datetime]
        if isinstance(_archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = isoparse(_archived_at)

        catalog_entry_reference_v2 = cls(
            catalog_entry_id=catalog_entry_id,
            catalog_entry_name=catalog_entry_name,
            catalog_type_id=catalog_type_id,
            archived_at=archived_at,
        )

        catalog_entry_reference_v2.additional_properties = d
        return catalog_entry_reference_v2

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
