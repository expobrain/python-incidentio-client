from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_template_attribute_binding_payload_v2_merge_strategy import (
    AlertTemplateAttributeBindingPayloadV2MergeStrategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_value_payload_v2 import (
        EngineParamBindingValuePayloadV2,
    )


T = TypeVar("T", bound="AlertTemplateAttributeBindingPayloadV2")


@_attrs_define
class AlertTemplateAttributeBindingPayloadV2:
    """
    Example:
        {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'merge_strategy': 'first_wins',
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}

    Attributes:
        array_value (Union[Unset, List['EngineParamBindingValuePayloadV2']]): If set, this is the array value of the
            step parameter Example: [{'literal': 'SEV123', 'reference': 'incident.severity'}].
        merge_strategy (Union[Unset, AlertTemplateAttributeBindingPayloadV2MergeStrategy]): Merge strategy for this
            attribute when alert updates Example: first_wins.
        value (Union[Unset, EngineParamBindingValuePayloadV2]):  Example: {'literal': 'SEV123', 'reference':
            'incident.severity'}.
    """

    array_value: Union[Unset, List["EngineParamBindingValuePayloadV2"]] = UNSET
    merge_strategy: Union[
        Unset, AlertTemplateAttributeBindingPayloadV2MergeStrategy
    ] = UNSET
    value: Union[Unset, "EngineParamBindingValuePayloadV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        array_value: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.array_value, Unset):
            array_value = []
            for array_value_item_data in self.array_value:
                array_value_item = array_value_item_data.to_dict()
                array_value.append(array_value_item)

        merge_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.merge_strategy, Unset):
            merge_strategy = self.merge_strategy.value

        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if array_value is not UNSET:
            field_dict["array_value"] = array_value
        if merge_strategy is not UNSET:
            field_dict["merge_strategy"] = merge_strategy
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.engine_param_binding_value_payload_v2 import (
            EngineParamBindingValuePayloadV2,
        )

        d = src_dict.copy()
        array_value = []
        _array_value = d.pop("array_value", UNSET)
        for array_value_item_data in _array_value or []:
            array_value_item = EngineParamBindingValuePayloadV2.from_dict(
                array_value_item_data
            )

            array_value.append(array_value_item)

        _merge_strategy = d.pop("merge_strategy", UNSET)
        merge_strategy: Union[
            Unset, AlertTemplateAttributeBindingPayloadV2MergeStrategy
        ]
        if isinstance(_merge_strategy, Unset):
            merge_strategy = UNSET
        else:
            merge_strategy = AlertTemplateAttributeBindingPayloadV2MergeStrategy(
                _merge_strategy
            )

        _value = d.pop("value", UNSET)
        value: Union[Unset, EngineParamBindingValuePayloadV2]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = EngineParamBindingValuePayloadV2.from_dict(_value)

        alert_template_attribute_binding_payload_v2 = cls(
            array_value=array_value,
            merge_strategy=merge_strategy,
            value=value,
        )

        alert_template_attribute_binding_payload_v2.additional_properties = d
        return alert_template_attribute_binding_payload_v2

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
