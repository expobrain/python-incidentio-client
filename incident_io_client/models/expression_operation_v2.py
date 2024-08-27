from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expression_operation_v2_operation_type import (
    ExpressionOperationV2OperationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expression_branches_opts_v2 import ExpressionBranchesOptsV2
    from ..models.expression_filter_opts_v2 import ExpressionFilterOptsV2
    from ..models.expression_navigate_opts_v2 import ExpressionNavigateOptsV2
    from ..models.expression_parse_opts_v2 import ExpressionParseOptsV2
    from ..models.returns_meta_v2 import ReturnsMetaV2


T = TypeVar("T", bound="ExpressionOperationV2")


@_attrs_define
class ExpressionOperationV2:
    """
    Example:
        {'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones',
            'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}]}]},
            'navigate': {'reference': '1235', 'reference_label': 'Teams'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'},
            'returns': {'array': True, 'type': 'IncidentStatus'}}

    Attributes:
        operation_type (ExpressionOperationV2OperationType): The type of the operation Example: navigate.
        returns (ReturnsMetaV2):  Example: {'array': True, 'type': 'IncidentStatus'}.
        branches (Union[Unset, ExpressionBranchesOptsV2]):  Example: {'branches': [{'condition_groups': [{'conditions':
            [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Incident Severity', 'reference': 'incident.severity'}}]}], 'result': {'array_value': [{'label': 'Lawrence
            Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}.
        filter_ (Union[Unset, ExpressionFilterOptsV2]):  Example: {'condition_groups': [{'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident
            Severity', 'reference': 'incident.severity'}}]}]}.
        navigate (Union[Unset, ExpressionNavigateOptsV2]):  Example: {'reference': '1235', 'reference_label': 'Teams'}.
        parse (Union[Unset, ExpressionParseOptsV2]):  Example: {'returns': {'array': True, 'type': 'IncidentStatus'},
            'source': 'metadata.annotations["github.com/repo"]'}.
    """

    operation_type: ExpressionOperationV2OperationType
    returns: "ReturnsMetaV2"
    branches: Union[Unset, "ExpressionBranchesOptsV2"] = UNSET
    filter_: Union[Unset, "ExpressionFilterOptsV2"] = UNSET
    navigate: Union[Unset, "ExpressionNavigateOptsV2"] = UNSET
    parse: Union[Unset, "ExpressionParseOptsV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type.value

        returns = self.returns.to_dict()

        branches: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branches, Unset):
            branches = self.branches.to_dict()

        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        navigate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.navigate, Unset):
            navigate = self.navigate.to_dict()

        parse: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parse, Unset):
            parse = self.parse.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation_type": operation_type,
                "returns": returns,
            }
        )
        if branches is not UNSET:
            field_dict["branches"] = branches
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if navigate is not UNSET:
            field_dict["navigate"] = navigate
        if parse is not UNSET:
            field_dict["parse"] = parse

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.expression_branches_opts_v2 import ExpressionBranchesOptsV2
        from ..models.expression_filter_opts_v2 import ExpressionFilterOptsV2
        from ..models.expression_navigate_opts_v2 import ExpressionNavigateOptsV2
        from ..models.expression_parse_opts_v2 import ExpressionParseOptsV2
        from ..models.returns_meta_v2 import ReturnsMetaV2

        d = src_dict.copy()
        operation_type = ExpressionOperationV2OperationType(d.pop("operation_type"))

        returns = ReturnsMetaV2.from_dict(d.pop("returns"))

        _branches = d.pop("branches", UNSET)
        branches: Union[Unset, ExpressionBranchesOptsV2]
        if isinstance(_branches, Unset):
            branches = UNSET
        else:
            branches = ExpressionBranchesOptsV2.from_dict(_branches)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, ExpressionFilterOptsV2]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ExpressionFilterOptsV2.from_dict(_filter_)

        _navigate = d.pop("navigate", UNSET)
        navigate: Union[Unset, ExpressionNavigateOptsV2]
        if isinstance(_navigate, Unset):
            navigate = UNSET
        else:
            navigate = ExpressionNavigateOptsV2.from_dict(_navigate)

        _parse = d.pop("parse", UNSET)
        parse: Union[Unset, ExpressionParseOptsV2]
        if isinstance(_parse, Unset):
            parse = UNSET
        else:
            parse = ExpressionParseOptsV2.from_dict(_parse)

        expression_operation_v2 = cls(
            operation_type=operation_type,
            returns=returns,
            branches=branches,
            filter_=filter_,
            navigate=navigate,
            parse=parse,
        )

        expression_operation_v2.additional_properties = d
        return expression_operation_v2

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
