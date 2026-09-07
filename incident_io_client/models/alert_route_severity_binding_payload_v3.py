from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_route_severity_binding_payload_v3_merge_strategy import (
    AlertRouteSeverityBindingPayloadV3MergeStrategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_payload_v3 import EngineParamBindingPayloadV3


T = TypeVar("T", bound="AlertRouteSeverityBindingPayloadV3")


@_attrs_define
class AlertRouteSeverityBindingPayloadV3:
    """
    Example:
        {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'merge_strategy': 'first-wins'}

    Attributes:
        merge_strategy (AlertRouteSeverityBindingPayloadV3MergeStrategy): Strategy for merging severity when multiple
            alerts create/update the same incident Example: first-wins.
        binding (Union[Unset, EngineParamBindingPayloadV3]):  Example: {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
    """

    merge_strategy: AlertRouteSeverityBindingPayloadV3MergeStrategy
    binding: Union[Unset, "EngineParamBindingPayloadV3"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        merge_strategy = self.merge_strategy.value

        binding: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.binding, Unset):
            binding = self.binding.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "merge_strategy": merge_strategy,
            }
        )
        if binding is not UNSET:
            field_dict["binding"] = binding

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.engine_param_binding_payload_v3 import EngineParamBindingPayloadV3

        d = src_dict.copy()
        merge_strategy = AlertRouteSeverityBindingPayloadV3MergeStrategy(
            d.pop("merge_strategy")
        )

        _binding = d.pop("binding", UNSET)
        binding: Union[Unset, EngineParamBindingPayloadV3]
        if isinstance(_binding, Unset):
            binding = UNSET
        else:
            binding = EngineParamBindingPayloadV3.from_dict(_binding)

        alert_route_severity_binding_payload_v3 = cls(
            merge_strategy=merge_strategy,
            binding=binding,
        )

        alert_route_severity_binding_payload_v3.additional_properties = d
        return alert_route_severity_binding_payload_v3

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
