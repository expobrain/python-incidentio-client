from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.catalog_attribute_binding_payload_v2_request_body import (
        CatalogAttributeBindingPayloadV2RequestBody,
    )


T = TypeVar("T", bound="CatalogV2CreateEntryRequestBodyAttributeValues")


@attr.s(auto_attribs=True)
class CatalogV2CreateEntryRequestBodyAttributeValues:
    """Values of this entry

    Example:
        {'abc123': {'array_value': [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}}

    """

    additional_properties: Dict[str, "CatalogAttributeBindingPayloadV2RequestBody"] = attr.ib(
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
        from ..models.catalog_attribute_binding_payload_v2_request_body import (
            CatalogAttributeBindingPayloadV2RequestBody,
        )

        d = src_dict.copy()
        catalog_v2_create_entry_request_body_attribute_values = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CatalogAttributeBindingPayloadV2RequestBody.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        catalog_v2_create_entry_request_body_attribute_values.additional_properties = (
            additional_properties
        )
        return catalog_v2_create_entry_request_body_attribute_values

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "CatalogAttributeBindingPayloadV2RequestBody":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "CatalogAttributeBindingPayloadV2RequestBody") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
