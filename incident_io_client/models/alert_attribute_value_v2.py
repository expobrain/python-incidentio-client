from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_attribute_catalog_entry_v2 import AlertAttributeCatalogEntryV2


T = TypeVar("T", bound="AlertAttributeValueV2")


@_attrs_define
class AlertAttributeValueV2:
    """
    Example:
        {'catalog_entry': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Primary On-call'}, 'label': 'Payments Team', 'literal': 'SEV123'}

    Attributes:
        catalog_entry (Union[Unset, AlertAttributeCatalogEntryV2]):  Example: {'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}.
        label (Union[Unset, str]): The human readable label of this value for convenience. Will match the literal if
            this is a primitive type, or be the name of the catalog entry if this is a catalog entry Example: Payments Team.
        literal (Union[Unset, str]): If set, this is the literal value of the step parameter Example: SEV123.
    """

    catalog_entry: Union[Unset, "AlertAttributeCatalogEntryV2"] = UNSET
    label: Union[Unset, str] = UNSET
    literal: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        catalog_entry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.catalog_entry, Unset):
            catalog_entry = self.catalog_entry.to_dict()

        label = self.label

        literal = self.literal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if catalog_entry is not UNSET:
            field_dict["catalog_entry"] = catalog_entry
        if label is not UNSET:
            field_dict["label"] = label
        if literal is not UNSET:
            field_dict["literal"] = literal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_attribute_catalog_entry_v2 import (
            AlertAttributeCatalogEntryV2,
        )

        d = src_dict.copy()
        _catalog_entry = d.pop("catalog_entry", UNSET)
        catalog_entry: Union[Unset, AlertAttributeCatalogEntryV2]
        if isinstance(_catalog_entry, Unset):
            catalog_entry = UNSET
        else:
            catalog_entry = AlertAttributeCatalogEntryV2.from_dict(_catalog_entry)

        label = d.pop("label", UNSET)

        literal = d.pop("literal", UNSET)

        alert_attribute_value_v2 = cls(
            catalog_entry=catalog_entry,
            label=label,
            literal=literal,
        )

        alert_attribute_value_v2.additional_properties = d
        return alert_attribute_value_v2

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
