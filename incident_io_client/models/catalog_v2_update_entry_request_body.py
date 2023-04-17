from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.catalog_v2_update_entry_request_body_attribute_values import (
        CatalogV2UpdateEntryRequestBodyAttributeValues,
    )


T = TypeVar("T", bound="CatalogV2UpdateEntryRequestBody")


@attr.s(auto_attribs=True)
class CatalogV2UpdateEntryRequestBody:
    """
    Example:
        {'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}},
            'name': 'Primary On-call'}

    Attributes:
        attribute_values (CatalogV2UpdateEntryRequestBodyAttributeValues): Values of this entry Example: {'abc123':
            {'array_value': [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}}.
        name (str): Name is the human readable name of this entry Example: Primary On-call.
    """

    attribute_values: "CatalogV2UpdateEntryRequestBodyAttributeValues"
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_values = self.attribute_values.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_values": attribute_values,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_v2_update_entry_request_body_attribute_values import (
            CatalogV2UpdateEntryRequestBodyAttributeValues,
        )

        d = src_dict.copy()
        attribute_values = CatalogV2UpdateEntryRequestBodyAttributeValues.from_dict(
            d.pop("attribute_values")
        )

        name = d.pop("name")

        catalog_v2_update_entry_request_body = cls(
            attribute_values=attribute_values,
            name=name,
        )

        catalog_v2_update_entry_request_body.additional_properties = d
        return catalog_v2_update_entry_request_body

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
