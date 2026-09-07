from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_entry_engine_param_binding_value_v3 import (
        CatalogEntryEngineParamBindingValueV3,
    )


T = TypeVar("T", bound="CatalogEntryEngineParamBindingV3")


@_attrs_define
class CatalogEntryEngineParamBindingV3:
    """
    Example:
        {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123'}], 'value': {'label': 'Lawrence Jones',
            'literal': 'SEV123'}}

    Attributes:
        array_value (Union[Unset, List['CatalogEntryEngineParamBindingValueV3']]): If the attribute is multi-valued, the
            value will be returned here. Example: [{'label': 'Lawrence Jones', 'literal': 'SEV123'}].
        value (Union[Unset, CatalogEntryEngineParamBindingValueV3]):  Example: {'label': 'Lawrence Jones', 'literal':
            'SEV123'}.
    """

    array_value: Union[Unset, List["CatalogEntryEngineParamBindingValueV3"]] = UNSET
    value: Union[Unset, "CatalogEntryEngineParamBindingValueV3"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        from ..models.catalog_entry_engine_param_binding_value_v3 import (
            CatalogEntryEngineParamBindingValueV3,
        )

        d = src_dict.copy()
        array_value = []
        _array_value = d.pop("array_value", UNSET)
        for array_value_item_data in _array_value or []:
            array_value_item = CatalogEntryEngineParamBindingValueV3.from_dict(
                array_value_item_data
            )

            array_value.append(array_value_item)

        _value = d.pop("value", UNSET)
        value: Union[Unset, CatalogEntryEngineParamBindingValueV3]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = CatalogEntryEngineParamBindingValueV3.from_dict(_value)

        catalog_entry_engine_param_binding_v3 = cls(
            array_value=array_value,
            value=value,
        )

        catalog_entry_engine_param_binding_v3.additional_properties = d
        return catalog_entry_engine_param_binding_v3

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
