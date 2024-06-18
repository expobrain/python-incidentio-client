from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.engine_param_binding_payload_v2_request_body import (
        EngineParamBindingPayloadV2RequestBody,
    )


T = TypeVar("T", bound="ConditionPayloadV2RequestBody")


@_attrs_define
class ConditionPayloadV2RequestBody:
    """
    Example:
        {'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}

    Attributes:
        operation (str): The name of the operation on the subject Example: one_of.
        param_bindings (List['EngineParamBindingPayloadV2RequestBody']): List of parameter bindings Example:
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}].
        subject (str): The reference of the subject in the trigger scope Example: incident.severity.
    """

    operation: str
    param_bindings: List["EngineParamBindingPayloadV2RequestBody"]
    subject: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation = self.operation

        param_bindings = []
        for param_bindings_item_data in self.param_bindings:
            param_bindings_item = param_bindings_item_data.to_dict()
            param_bindings.append(param_bindings_item)

        subject = self.subject

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
        from ..models.engine_param_binding_payload_v2_request_body import (
            EngineParamBindingPayloadV2RequestBody,
        )

        d = src_dict.copy()
        operation = d.pop("operation")

        param_bindings = []
        _param_bindings = d.pop("param_bindings")
        for param_bindings_item_data in _param_bindings:
            param_bindings_item = EngineParamBindingPayloadV2RequestBody.from_dict(
                param_bindings_item_data
            )

            param_bindings.append(param_bindings_item)

        subject = d.pop("subject")

        condition_payload_v2_request_body = cls(
            operation=operation,
            param_bindings=param_bindings,
            subject=subject,
        )

        condition_payload_v2_request_body.additional_properties = d
        return condition_payload_v2_request_body

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
