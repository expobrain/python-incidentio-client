from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_entry_engine_param_binding_v2 import (
        CatalogEntryEngineParamBindingV2,
    )


T = TypeVar("T", bound="CatalogEntryV2AttributeValues")


@_attrs_define
class CatalogEntryV2AttributeValues:
    """Values of this entry

    Example:
        {'abc123': {'array_value': [{'catalog_entry': {'archived_at': '2021-08-17T14:28:57.801578Z', 'catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'abc123', 'image_url': 'abc123', 'is_image_slack_icon': False,
            'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity', 'sort_key': 'abc123',
            'unavailable': False, 'value': 'abc123'}], 'value': {'catalog_entry': {'archived_at':
            '2021-08-17T14:28:57.801578Z', 'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary
            escalation', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'abc123', 'image_url': 'abc123',
            'is_image_slack_icon': False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity',
            'sort_key': 'abc123', 'unavailable': False, 'value': 'abc123'}}}

    """

    additional_properties: Dict[str, "CatalogEntryEngineParamBindingV2"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_entry_engine_param_binding_v2 import (
            CatalogEntryEngineParamBindingV2,
        )

        d = src_dict.copy()
        catalog_entry_v2_attribute_values = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CatalogEntryEngineParamBindingV2.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        catalog_entry_v2_attribute_values.additional_properties = additional_properties
        return catalog_entry_v2_attribute_values

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "CatalogEntryEngineParamBindingV2":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "CatalogEntryEngineParamBindingV2") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
