from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_type_attribute_v2 import CatalogTypeAttributeV2


T = TypeVar("T", bound="CatalogTypeSchemaV2")


@_attrs_define
class CatalogTypeSchemaV2:
    """
    Example:
        {'attributes': [{'array': False, 'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode':
            'manual', 'name': 'tier', 'path': [{'attribute_id': 'abc123', 'attribute_name': 'abc123'}], 'type':
            'Custom["Service"]'}], 'version': 1}

    Attributes:
        attributes (List['CatalogTypeAttributeV2']): Attributes of this catalog type Example: [{'array': False,
            'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual', 'name': 'tier', 'path':
            [{'attribute_id': 'abc123', 'attribute_name': 'abc123'}], 'type': 'Custom["Service"]'}].
        version (int): The version number of this schema Example: 1.
    """

    attributes: List["CatalogTypeAttributeV2"]
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
        from ..models.catalog_type_attribute_v2 import CatalogTypeAttributeV2

        d = src_dict.copy()
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = CatalogTypeAttributeV2.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        version = d.pop("version")

        catalog_type_schema_v2 = cls(
            attributes=attributes,
            version=version,
        )

        catalog_type_schema_v2.additional_properties = d
        return catalog_type_schema_v2

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
