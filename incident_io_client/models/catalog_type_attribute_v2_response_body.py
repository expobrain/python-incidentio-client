from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CatalogTypeAttributeV2ResponseBody")


@attr.s(auto_attribs=True)
class CatalogTypeAttributeV2ResponseBody:
    """
    Example:
        {'array': False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'Custom["Service"]'}

    Attributes:
        array (bool): Whether this attribute is an array
        id (str): The ID of this attribute Example: 01GW2G3V0S59R238FAHPDS1R66.
        name (str): Unique name of this attribute Example: tier.
        type (str): Catalog type name for this attribute Example: Custom["Service"].
    """

    array: bool
    id: str
    name: str
    type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        array = self.array
        id = self.id
        name = self.name
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "id": id,
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

        name = d.pop("name")

        type = d.pop("type")

        catalog_type_attribute_v2_response_body = cls(
            array=array,
            id=id,
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
