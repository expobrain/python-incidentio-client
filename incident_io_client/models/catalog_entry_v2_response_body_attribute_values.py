from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.catalog_attribute_binding_v2_response_body import (
        CatalogAttributeBindingV2ResponseBody,
    )


T = TypeVar("T", bound="CatalogEntryV2ResponseBodyAttributeValues")


@attr.s(auto_attribs=True)
class CatalogEntryV2ResponseBodyAttributeValues:
    """Values of this entry

    Example:
        {'abc123': {'array_value': [{'catalog_entry': {'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'catalog_entry_name': 'Primary escalation', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'image_url':
            'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon':
            False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}], 'value': {'catalog_entry':
            {'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation',
            'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}}}

    """

    additional_properties: Dict[str, "CatalogAttributeBindingV2ResponseBody"] = attr.ib(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_attribute_binding_v2_response_body import (
            CatalogAttributeBindingV2ResponseBody,
        )

        d = src_dict.copy()
        catalog_entry_v2_response_body_attribute_values = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CatalogAttributeBindingV2ResponseBody.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        catalog_entry_v2_response_body_attribute_values.additional_properties = (
            additional_properties
        )
        return catalog_entry_v2_response_body_attribute_values

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "CatalogAttributeBindingV2ResponseBody":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "CatalogAttributeBindingV2ResponseBody") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
