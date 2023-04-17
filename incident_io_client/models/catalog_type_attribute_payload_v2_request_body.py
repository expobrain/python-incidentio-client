from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogTypeAttributePayloadV2RequestBody")


@attr.s(auto_attribs=True)
class CatalogTypeAttributePayloadV2RequestBody:
    """
    Example:
        {'array': False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'tier'}

    Attributes:
        array (bool): Whether this column is an array
        name (str): Unique name of this column Example: tier.
        type (str): The type of this column Example: tier.
        id (Union[Unset, str]): The ID of this column Example: 01GW2G3V0S59R238FAHPDS1R66.
    """

    array: bool
    name: str
    type: str
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        array = self.array
        name = self.name
        type = self.type
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "name": name,
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        array = d.pop("array")

        name = d.pop("name")

        type = d.pop("type")

        id = d.pop("id", UNSET)

        catalog_type_attribute_payload_v2_request_body = cls(
            array=array,
            name=name,
            type=type,
            id=id,
        )

        catalog_type_attribute_payload_v2_request_body.additional_properties = d
        return catalog_type_attribute_payload_v2_request_body

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
