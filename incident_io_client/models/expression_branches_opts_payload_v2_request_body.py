from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.expression_branch_payload_v2_request_body import (
        ExpressionBranchPayloadV2RequestBody,
    )
    from ..models.returns_meta_v2_request_body import ReturnsMetaV2RequestBody


T = TypeVar("T", bound="ExpressionBranchesOptsPayloadV2RequestBody")


@_attrs_define
class ExpressionBranchesOptsPayloadV2RequestBody:
    """
    Example:
        {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}

    Attributes:
        branches (List['ExpressionBranchPayloadV2RequestBody']): The branches to apply for this operation Example:
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}].
        returns (ReturnsMetaV2RequestBody):  Example: {'array': True, 'type': 'IncidentStatus'}.
    """

    branches: List["ExpressionBranchPayloadV2RequestBody"]
    returns: "ReturnsMetaV2RequestBody"
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
        from ..models.expression_branch_payload_v2_request_body import (
            ExpressionBranchPayloadV2RequestBody,
        )
        from ..models.returns_meta_v2_request_body import ReturnsMetaV2RequestBody

        d = src_dict.copy()
        branches = []
        _branches = d.pop("branches")
        for branches_item_data in _branches:
            branches_item = ExpressionBranchPayloadV2RequestBody.from_dict(branches_item_data)

            branches.append(branches_item)

        returns = ReturnsMetaV2RequestBody.from_dict(d.pop("returns"))

        expression_branches_opts_payload_v2_request_body = cls(
            branches=branches,
            returns=returns,
        )

        expression_branches_opts_payload_v2_request_body.additional_properties = d
        return expression_branches_opts_payload_v2_request_body

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
