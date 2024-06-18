from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expression_else_branch_v2_response_body import (
        ExpressionElseBranchV2ResponseBody,
    )
    from ..models.expression_operation_v2_response_body import (
        ExpressionOperationV2ResponseBody,
    )
    from ..models.returns_meta_v2_response_body import ReturnsMetaV2ResponseBody


T = TypeVar("T", bound="ExpressionV2ResponseBody")


@_attrs_define
class ExpressionV2ResponseBody:
    """
    Example:
        {'else_branch': {'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}]}]},
            'navigate': {'reference': '1235', 'reference_label': 'Teams'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'},
            'returns': {'array': True, 'type': 'IncidentStatus'}}], 'reference': 'abc123', 'returns': {'array': True,
            'type': 'IncidentStatus'}, 'root_reference': 'incident.status'}

    Attributes:
        label (str): The human readable label of the expression Example: Team Slack channel.
        operations (List['ExpressionOperationV2ResponseBody']):  Example: [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}]}]},
            'navigate': {'reference': '1235', 'reference_label': 'Teams'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'},
            'returns': {'array': True, 'type': 'IncidentStatus'}}].
        reference (str): A short ID that can be used to reference the expression Example: abc123.
        returns (ReturnsMetaV2ResponseBody):  Example: {'array': True, 'type': 'IncidentStatus'}.
        root_reference (str): The root reference for this expression (i.e. where the expression starts) Example:
            incident.status.
        else_branch (Union[Unset, ExpressionElseBranchV2ResponseBody]):  Example: {'result': {'array_value': [{'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}}}.
    """

    label: str
    operations: List["ExpressionOperationV2ResponseBody"]
    reference: str
    returns: "ReturnsMetaV2ResponseBody"
    root_reference: str
    else_branch: Union[Unset, "ExpressionElseBranchV2ResponseBody"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.to_dict()
            operations.append(operations_item)

        reference = self.reference

        returns = self.returns.to_dict()

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
                "returns": returns,
                "root_reference": root_reference,
            }
        )
        if else_branch is not UNSET:
            field_dict["else_branch"] = else_branch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.expression_else_branch_v2_response_body import (
            ExpressionElseBranchV2ResponseBody,
        )
        from ..models.expression_operation_v2_response_body import (
            ExpressionOperationV2ResponseBody,
        )
        from ..models.returns_meta_v2_response_body import ReturnsMetaV2ResponseBody

        d = src_dict.copy()
        label = d.pop("label")

        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:
            operations_item = ExpressionOperationV2ResponseBody.from_dict(operations_item_data)

            operations.append(operations_item)

        reference = d.pop("reference")

        returns = ReturnsMetaV2ResponseBody.from_dict(d.pop("returns"))

        root_reference = d.pop("root_reference")

        _else_branch = d.pop("else_branch", UNSET)
        else_branch: Union[Unset, ExpressionElseBranchV2ResponseBody]
        if isinstance(_else_branch, Unset):
            else_branch = UNSET
        else:
            else_branch = ExpressionElseBranchV2ResponseBody.from_dict(_else_branch)

        expression_v2_response_body = cls(
            label=label,
            operations=operations,
            reference=reference,
            returns=returns,
            root_reference=root_reference,
            else_branch=else_branch,
        )

        expression_v2_response_body.additional_properties = d
        return expression_v2_response_body

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
