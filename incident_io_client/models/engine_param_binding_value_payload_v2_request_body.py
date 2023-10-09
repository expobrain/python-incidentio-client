from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EngineParamBindingValuePayloadV2RequestBody")


@_attrs_define
class EngineParamBindingValuePayloadV2RequestBody:
    """
    Example:
        {'literal': 'SEV123', 'reference': 'incident.severity'}

    Attributes:
        literal (Union[Unset, str]): If set, this is the literal value of the step parameter Example: SEV123.
        reference (Union[Unset, str]): If set, this is the reference into the trigger scope that is the value of this
            parameter Example: incident.severity.
    """

    literal: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        literal = self.literal
        reference = self.reference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if literal is not UNSET:
            field_dict["literal"] = literal
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        literal = d.pop("literal", UNSET)

        reference = d.pop("reference", UNSET)

        engine_param_binding_value_payload_v2_request_body = cls(
            literal=literal,
            reference=reference,
        )

        engine_param_binding_value_payload_v2_request_body.additional_properties = d
        return engine_param_binding_value_payload_v2_request_body

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
