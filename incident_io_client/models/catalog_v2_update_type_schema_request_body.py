from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_type_attribute_payload_v2 import CatalogTypeAttributePayloadV2


T = TypeVar("T", bound="CatalogV2UpdateTypeSchemaRequestBody")


@_attrs_define
class CatalogV2UpdateTypeSchemaRequestBody:
    """
    Example:
        {'attributes': [{'array': False, 'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode':
            'manual', 'name': 'tier', 'path': [{'attribute_id': 'abc123'}], 'type': 'Custom["Service"]'}], 'version': 1}

    Attributes:
        attributes (List['CatalogTypeAttributePayloadV2']):  Example: [{'array': False, 'backlink_attribute': 'abc123',
            'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual', 'name': 'tier', 'path': [{'attribute_id': 'abc123'}],
            'type': 'Custom["Service"]'}].
        version (int):  Example: 1.
    """

    attributes: List["CatalogTypeAttributePayloadV2"]
    version: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_type_attribute_payload_v2 import (
            CatalogTypeAttributePayloadV2,
        )

        d = src_dict.copy()
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = CatalogTypeAttributePayloadV2.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        version = d.pop("version")

        catalog_v2_update_type_schema_request_body = cls(
            attributes=attributes,
            version=version,
        )

        catalog_v2_update_type_schema_request_body.additional_properties = d
        return catalog_v2_update_type_schema_request_body

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
