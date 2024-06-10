from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.engine_param_binding_v2_response_body import (
        EngineParamBindingV2ResponseBody,
    )


T = TypeVar("T", bound="ExpressionElseBranchV2ResponseBody")


@_attrs_define
class ExpressionElseBranchV2ResponseBody:
    """
    Example:
        {'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}}

    Attributes:
        result (EngineParamBindingV2ResponseBody):  Example: {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}.
    """

    result: "EngineParamBindingV2ResponseBody"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result = self.result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.engine_param_binding_v2_response_body import (
            EngineParamBindingV2ResponseBody,
        )

        d = src_dict.copy()
        result = EngineParamBindingV2ResponseBody.from_dict(d.pop("result"))

        expression_else_branch_v2_response_body = cls(
            result=result,
        )

        expression_else_branch_v2_response_body.additional_properties = d
        return expression_else_branch_v2_response_body

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
