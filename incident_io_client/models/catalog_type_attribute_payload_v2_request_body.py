from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_type_attribute_payload_v2_request_body_mode import (
    CatalogTypeAttributePayloadV2RequestBodyMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogTypeAttributePayloadV2RequestBody")


@_attrs_define
class CatalogTypeAttributePayloadV2RequestBody:
    """
    Example:
        {'array': False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual', 'name': 'tier', 'type':
            'Custom["Service"]'}

    Attributes:
        array (bool): Whether this attribute is an array
        name (str): Unique name of this attribute Example: tier.
        type (str): Catalog type name for this attribute Example: Custom["Service"].
        id (Union[Unset, str]): The ID of this attribute Example: 01GW2G3V0S59R238FAHPDS1R66.
        mode (Union[Unset, CatalogTypeAttributePayloadV2RequestBodyMode]): Controls how this attribute is modified
            Example: manual.
    """

    array: bool
    name: str
    type: str
    id: Union[Unset, str] = UNSET
    mode: Union[Unset, CatalogTypeAttributePayloadV2RequestBodyMode] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        array = self.array
        name = self.name
        type = self.type
        id = self.id
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

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
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        array = d.pop("array")

        name = d.pop("name")

        type = d.pop("type")

        id = d.pop("id", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, CatalogTypeAttributePayloadV2RequestBodyMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CatalogTypeAttributePayloadV2RequestBodyMode(_mode)

        catalog_type_attribute_payload_v2_request_body = cls(
            array=array,
            name=name,
            type=type,
            id=id,
            mode=mode,
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
