from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_type_attribute_v2_response_body_mode import (
    CatalogTypeAttributeV2ResponseBodyMode,
)

T = TypeVar("T", bound="CatalogTypeAttributeV2ResponseBody")


@_attrs_define
class CatalogTypeAttributeV2ResponseBody:
    """
    Example:
        {'array': False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual', 'name': 'tier', 'type':
            'Custom["Service"]'}

    Attributes:
        array (bool): Whether this attribute is an array
        id (str): The ID of this attribute Example: 01GW2G3V0S59R238FAHPDS1R66.
        mode (CatalogTypeAttributeV2ResponseBodyMode): Controls how this attribute is modified Example: manual.
        name (str): Unique name of this attribute Example: tier.
        type (str): Catalog type name for this attribute Example: Custom["Service"].
    """

    array: bool
    id: str
    mode: CatalogTypeAttributeV2ResponseBodyMode
    name: str
    type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        array = self.array
        id = self.id
        mode = self.mode.value

        name = self.name
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "id": id,
                "mode": mode,
                "name": name,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        array = d.pop("array")

        id = d.pop("id")

        mode = CatalogTypeAttributeV2ResponseBodyMode(d.pop("mode"))

        name = d.pop("name")

        type = d.pop("type")

        catalog_type_attribute_v2_response_body = cls(
            array=array,
            id=id,
            mode=mode,
            name=name,
            type=type,
        )

        catalog_type_attribute_v2_response_body.additional_properties = d
        return catalog_type_attribute_v2_response_body

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
