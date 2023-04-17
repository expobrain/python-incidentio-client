from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogAttributeValuePayloadV2RequestBody")


@attr.s(auto_attribs=True)
class CatalogAttributeValuePayloadV2RequestBody:
    """
    Example:
        {'literal': 'SEV123'}

    Attributes:
        literal (Union[Unset, str]): The literal value of this attribute Example: SEV123.
    """

    literal: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        literal = self.literal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if literal is not UNSET:
            field_dict["literal"] = literal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        literal = d.pop("literal", UNSET)

        catalog_attribute_value_payload_v2_request_body = cls(
            literal=literal,
        )

        catalog_attribute_value_payload_v2_request_body.additional_properties = d
        return catalog_attribute_value_payload_v2_request_body

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
