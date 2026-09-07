from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogEngineParamBindingValuePayloadV3")


@_attrs_define
class CatalogEngineParamBindingValuePayloadV3:
    """
    Example:
        {'literal': 'SEV123'}

    Attributes:
        literal (Union[Unset, str]): If set, this is the literal value of the step parameter Example: SEV123.
    """

    literal: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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

        catalog_engine_param_binding_value_payload_v3 = cls(
            literal=literal,
        )

        catalog_engine_param_binding_value_payload_v3.additional_properties = d
        return catalog_engine_param_binding_value_payload_v3

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
