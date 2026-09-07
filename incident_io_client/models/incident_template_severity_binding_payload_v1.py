from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_template_severity_binding_payload_v1_merge_strategy import (
    IncidentTemplateSeverityBindingPayloadV1MergeStrategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_payload_v3 import EngineParamBindingPayloadV3


T = TypeVar("T", bound="IncidentTemplateSeverityBindingPayloadV1")


@_attrs_define
class IncidentTemplateSeverityBindingPayloadV1:
    """
    Example:
        {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'merge_strategy': 'first-wins'}

    Attributes:
        merge_strategy (IncidentTemplateSeverityBindingPayloadV1MergeStrategy): Strategy for merging severity when
            multiple alerts create/update the same incident Example: first-wins.
        binding (Union[Unset, EngineParamBindingPayloadV3]):  Example: {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
    """

    merge_strategy: IncidentTemplateSeverityBindingPayloadV1MergeStrategy
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
        merge_strategy = IncidentTemplateSeverityBindingPayloadV1MergeStrategy(
            d.pop("merge_strategy")
        )

        _binding = d.pop("binding", UNSET)
        binding: Union[Unset, EngineParamBindingPayloadV3]
        if isinstance(_binding, Unset):
            binding = UNSET
        else:
            binding = EngineParamBindingPayloadV3.from_dict(_binding)

        incident_template_severity_binding_payload_v1 = cls(
            merge_strategy=merge_strategy,
            binding=binding,
        )

        incident_template_severity_binding_payload_v1.additional_properties = d
        return incident_template_severity_binding_payload_v1

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
