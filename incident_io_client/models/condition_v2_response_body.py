from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.condition_operation_v2_response_body import (
        ConditionOperationV2ResponseBody,
    )
    from ..models.condition_subject_v2_response_body import (
        ConditionSubjectV2ResponseBody,
    )
    from ..models.engine_param_binding_v2_response_body import (
        EngineParamBindingV2ResponseBody,
    )


T = TypeVar("T", bound="ConditionV2ResponseBody")


@_attrs_define
class ConditionV2ResponseBody:
    """
    Example:
        {'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Incident Severity', 'reference': 'incident.severity'}}

    Attributes:
        operation (ConditionOperationV2ResponseBody):  Example: {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}.
        param_bindings (List['EngineParamBindingV2ResponseBody']): Bindings for the operation parameters Example:
            [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}].
        subject (ConditionSubjectV2ResponseBody):  Example: {'label': 'Incident Severity', 'reference':
            'incident.severity'}.
    """

    operation: "ConditionOperationV2ResponseBody"
    param_bindings: List["EngineParamBindingV2ResponseBody"]
    subject: "ConditionSubjectV2ResponseBody"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation = self.operation.to_dict()

        param_bindings = []
        for param_bindings_item_data in self.param_bindings:
            param_bindings_item = param_bindings_item_data.to_dict()
            param_bindings.append(param_bindings_item)

        subject = self.subject.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
                "param_bindings": param_bindings,
                "subject": subject,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.condition_operation_v2_response_body import (
            ConditionOperationV2ResponseBody,
        )
        from ..models.condition_subject_v2_response_body import (
            ConditionSubjectV2ResponseBody,
        )
        from ..models.engine_param_binding_v2_response_body import (
            EngineParamBindingV2ResponseBody,
        )

        d = src_dict.copy()
        operation = ConditionOperationV2ResponseBody.from_dict(d.pop("operation"))

        param_bindings = []
        _param_bindings = d.pop("param_bindings")
        for param_bindings_item_data in _param_bindings:
            param_bindings_item = EngineParamBindingV2ResponseBody.from_dict(
                param_bindings_item_data
            )

            param_bindings.append(param_bindings_item)

        subject = ConditionSubjectV2ResponseBody.from_dict(d.pop("subject"))

        condition_v2_response_body = cls(
            operation=operation,
            param_bindings=param_bindings,
            subject=subject,
        )

        condition_v2_response_body.additional_properties = d
        return condition_v2_response_body

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
