from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CatalogTypeAttributePathItemV2ResponseBody")


@_attrs_define
class CatalogTypeAttributePathItemV2ResponseBody:
    """
    Example:
        {'attribute_id': 'abc123', 'attribute_name': 'abc123'}

    Attributes:
        attribute_id (str): the ID of the attribute to use Example: abc123.
        attribute_name (str): the name of the attribute to use Example: abc123.
    """

    attribute_id: str
    attribute_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_id = self.attribute_id

        attribute_name = self.attribute_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute_id": attribute_id,
                "attribute_name": attribute_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_id = d.pop("attribute_id")

        attribute_name = d.pop("attribute_name")

        catalog_type_attribute_path_item_v2_response_body = cls(
            attribute_id=attribute_id,
            attribute_name=attribute_name,
        )

        catalog_type_attribute_path_item_v2_response_body.additional_properties = d
        return catalog_type_attribute_path_item_v2_response_body

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
