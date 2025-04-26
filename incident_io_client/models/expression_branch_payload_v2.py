from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2
    from ..models.engine_param_binding_payload_v2 import EngineParamBindingPayloadV2


T = TypeVar("T", bound="ExpressionBranchPayloadV2")


@_attrs_define
class ExpressionBranchPayloadV2:
    """
    Example:
        {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}

    Attributes:
        condition_groups (List['ConditionGroupPayloadV2']): When one of these condition groups are satisfied, this
            branch will be evaluated Example: [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}].
        result (EngineParamBindingPayloadV2):  Example: {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
    """

    condition_groups: List["ConditionGroupPayloadV2"]
    result: "EngineParamBindingPayloadV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        result = self.result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition_groups": condition_groups,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2
        from ..models.engine_param_binding_payload_v2 import EngineParamBindingPayloadV2

        d = src_dict.copy()
        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV2.from_dict(condition_groups_item_data)

            condition_groups.append(condition_groups_item)

        result = EngineParamBindingPayloadV2.from_dict(d.pop("result"))

        expression_branch_payload_v2 = cls(
            condition_groups=condition_groups,
            result=result,
        )

        expression_branch_payload_v2.additional_properties = d
        return expression_branch_payload_v2

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
