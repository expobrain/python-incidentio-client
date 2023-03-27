from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_attribute_value_payload_v2_request_body import (
        CatalogAttributeValuePayloadV2RequestBody,
    )


T = TypeVar("T", bound="CatalogAttributeBindingPayloadV2RequestBody")


@attr.s(auto_attribs=True)
class CatalogAttributeBindingPayloadV2RequestBody:
    """
    Example:
        {'array_value': [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}

    Attributes:
        array_value (Union[Unset, List['CatalogAttributeValuePayloadV2RequestBody']]): If set, this is the array value
            of the attribute Example: [{'literal': 'SEV123'}].
        value (Union[Unset, CatalogAttributeValuePayloadV2RequestBody]):  Example: {'literal': 'SEV123'}.
    """

    array_value: Union[Unset, List["CatalogAttributeValuePayloadV2RequestBody"]] = UNSET
    value: Union[Unset, "CatalogAttributeValuePayloadV2RequestBody"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        array_value: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.array_value, Unset):
            array_value = []
            for array_value_item_data in self.array_value:
                array_value_item = array_value_item_data.to_dict()

                array_value.append(array_value_item)

        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if array_value is not UNSET:
            field_dict["array_value"] = array_value
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_attribute_value_payload_v2_request_body import (
            CatalogAttributeValuePayloadV2RequestBody,
        )

        d = src_dict.copy()
        array_value = []
        _array_value = d.pop("array_value", UNSET)
        for array_value_item_data in _array_value or []:
            array_value_item = CatalogAttributeValuePayloadV2RequestBody.from_dict(
                array_value_item_data
            )

            array_value.append(array_value_item)

        _value = d.pop("value", UNSET)
        value: Union[Unset, CatalogAttributeValuePayloadV2RequestBody]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = CatalogAttributeValuePayloadV2RequestBody.from_dict(_value)

        catalog_attribute_binding_payload_v2_request_body = cls(
            array_value=array_value,
            value=value,
        )

        catalog_attribute_binding_payload_v2_request_body.additional_properties = d
        return catalog_attribute_binding_payload_v2_request_body

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
