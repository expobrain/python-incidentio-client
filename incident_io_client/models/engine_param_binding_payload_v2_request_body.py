from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_value_payload_v2_request_body import (
        EngineParamBindingValuePayloadV2RequestBody,
    )


T = TypeVar("T", bound="EngineParamBindingPayloadV2RequestBody")


@_attrs_define
class EngineParamBindingPayloadV2RequestBody:
    """
    Example:
        {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}

    Attributes:
        array_value (Union[Unset, List['EngineParamBindingValuePayloadV2RequestBody']]): If set, this is the array value
            of the step parameter Example: [{'literal': 'SEV123', 'reference': 'incident.severity'}].
        value (Union[Unset, EngineParamBindingValuePayloadV2RequestBody]):  Example: {'literal': 'SEV123', 'reference':
            'incident.severity'}.
    """

    array_value: Union[Unset, List["EngineParamBindingValuePayloadV2RequestBody"]] = UNSET
    value: Union[Unset, "EngineParamBindingValuePayloadV2RequestBody"] = UNSET
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
        from ..models.engine_param_binding_value_payload_v2_request_body import (
            EngineParamBindingValuePayloadV2RequestBody,
        )

        d = src_dict.copy()
        array_value = []
        _array_value = d.pop("array_value", UNSET)
        for array_value_item_data in _array_value or []:
            array_value_item = EngineParamBindingValuePayloadV2RequestBody.from_dict(
                array_value_item_data
            )

            array_value.append(array_value_item)

        _value = d.pop("value", UNSET)
        value: Union[Unset, EngineParamBindingValuePayloadV2RequestBody]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = EngineParamBindingValuePayloadV2RequestBody.from_dict(_value)

        engine_param_binding_payload_v2_request_body = cls(
            array_value=array_value,
            value=value,
        )

        engine_param_binding_payload_v2_request_body.additional_properties = d
        return engine_param_binding_payload_v2_request_body

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
