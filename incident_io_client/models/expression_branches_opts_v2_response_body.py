from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.expression_branch_v2_response_body import (
        ExpressionBranchV2ResponseBody,
    )
    from ..models.returns_meta_v2_response_body import ReturnsMetaV2ResponseBody


T = TypeVar("T", bound="ExpressionBranchesOptsV2ResponseBody")


@_attrs_define
class ExpressionBranchesOptsV2ResponseBody:
    """
    Example:
        {'branches': [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}

    Attributes:
        branches (List['ExpressionBranchV2ResponseBody']): The branches to apply for this operation Example:
            [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}].
        returns (ReturnsMetaV2ResponseBody):  Example: {'array': True, 'type': 'IncidentStatus'}.
    """

    branches: List["ExpressionBranchV2ResponseBody"]
    returns: "ReturnsMetaV2ResponseBody"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        branches = []
        for branches_item_data in self.branches:
            branches_item = branches_item_data.to_dict()
            branches.append(branches_item)

        returns = self.returns.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branches": branches,
                "returns": returns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.expression_branch_v2_response_body import (
            ExpressionBranchV2ResponseBody,
        )
        from ..models.returns_meta_v2_response_body import ReturnsMetaV2ResponseBody

        d = src_dict.copy()
        branches = []
        _branches = d.pop("branches")
        for branches_item_data in _branches:
            branches_item = ExpressionBranchV2ResponseBody.from_dict(branches_item_data)

            branches.append(branches_item)

        returns = ReturnsMetaV2ResponseBody.from_dict(d.pop("returns"))

        expression_branches_opts_v2_response_body = cls(
            branches=branches,
            returns=returns,
        )

        expression_branches_opts_v2_response_body.additional_properties = d
        return expression_branches_opts_v2_response_body

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
