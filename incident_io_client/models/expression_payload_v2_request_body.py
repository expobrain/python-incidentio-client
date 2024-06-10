from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expression_else_branch_payload_v2_request_body import (
        ExpressionElseBranchPayloadV2RequestBody,
    )
    from ..models.expression_operation_payload_v2_request_body import (
        ExpressionOperationPayloadV2RequestBody,
    )


T = TypeVar("T", bound="ExpressionPayloadV2RequestBody")


@_attrs_define
class ExpressionPayloadV2RequestBody:
    """
    Example:
        {'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}

    Attributes:
        label (str): The human readable label of the expression Example: Team Slack channel.
        operations (List['ExpressionOperationPayloadV2RequestBody']):  Example: [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}].
        reference (str): A short ID that can be used to reference the expression Example: abc123.
        root_reference (str): The root reference for this expression (i.e. where the expression starts) Example:
            incident.status.
        else_branch (Union[Unset, ExpressionElseBranchPayloadV2RequestBody]):  Example: {'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}.
    """

    label: str
    operations: List["ExpressionOperationPayloadV2RequestBody"]
    reference: str
    root_reference: str
    else_branch: Union[Unset, "ExpressionElseBranchPayloadV2RequestBody"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.to_dict()
            operations.append(operations_item)

        reference = self.reference

        root_reference = self.root_reference

        else_branch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.else_branch, Unset):
            else_branch = self.else_branch.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "operations": operations,
                "reference": reference,
                "root_reference": root_reference,
            }
        )
        if else_branch is not UNSET:
            field_dict["else_branch"] = else_branch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.expression_else_branch_payload_v2_request_body import (
            ExpressionElseBranchPayloadV2RequestBody,
        )
        from ..models.expression_operation_payload_v2_request_body import (
            ExpressionOperationPayloadV2RequestBody,
        )

        d = src_dict.copy()
        label = d.pop("label")

        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:
            operations_item = ExpressionOperationPayloadV2RequestBody.from_dict(
                operations_item_data
            )

            operations.append(operations_item)

        reference = d.pop("reference")

        root_reference = d.pop("root_reference")

        _else_branch = d.pop("else_branch", UNSET)
        else_branch: Union[Unset, ExpressionElseBranchPayloadV2RequestBody]
        if isinstance(_else_branch, Unset):
            else_branch = UNSET
        else:
            else_branch = ExpressionElseBranchPayloadV2RequestBody.from_dict(_else_branch)

        expression_payload_v2_request_body = cls(
            label=label,
            operations=operations,
            reference=reference,
            root_reference=root_reference,
            else_branch=else_branch,
        )

        expression_payload_v2_request_body.additional_properties = d
        return expression_payload_v2_request_body

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
