from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expression_operation_v3_operation_type import (
    ExpressionOperationV3OperationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expression_branches_opts_v3 import ExpressionBranchesOptsV3
    from ..models.expression_cast_opts_v3 import ExpressionCastOptsV3
    from ..models.expression_concatenate_opts_v3 import ExpressionConcatenateOptsV3
    from ..models.expression_filter_opts_v3 import ExpressionFilterOptsV3
    from ..models.expression_navigate_opts_v3 import ExpressionNavigateOptsV3
    from ..models.expression_parse_opts_v3 import ExpressionParseOptsV3
    from ..models.returns_meta_v3 import ReturnsMetaV3


T = TypeVar("T", bound="ExpressionOperationV3")


@_attrs_define
class ExpressionOperationV3:
    """
    Example:
        {'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones',
            'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Priority', 'reference': 'alert.priority'}}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array':
            True, 'type': 'IncidentStatus'}}, 'cast': {'returns': {'array': True, 'type': 'IncidentStatus'}}, 'concatenate':
            {'reference': '1235', 'reference_label': 'Teams'}, 'filter': {'condition_groups': [{'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}]}, 'navigate':
            {'reference': '1235', 'reference_label': 'Teams'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}, 'returns': {'array':
            True, 'type': 'IncidentStatus'}}

    Attributes:
        operation_type (ExpressionOperationV3OperationType): The type of the operation Example: navigate.
        returns (ReturnsMetaV3):  Example: {'array': True, 'type': 'IncidentStatus'}.
        branches (Union[Unset, ExpressionBranchesOptsV3]):  Example: {'branches': [{'condition_groups': [{'conditions':
            [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}],
            'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}.
        cast (Union[Unset, ExpressionCastOptsV3]):  Example: {'returns': {'array': True, 'type': 'IncidentStatus'}}.
        concatenate (Union[Unset, ExpressionConcatenateOptsV3]):  Example: {'reference': '1235', 'reference_label':
            'Teams'}.
        filter_ (Union[Unset, ExpressionFilterOptsV3]):  Example: {'condition_groups': [{'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Priority', 'reference': 'alert.priority'}}]}]}.
        navigate (Union[Unset, ExpressionNavigateOptsV3]):  Example: {'reference': '1235', 'reference_label': 'Teams'}.
        parse (Union[Unset, ExpressionParseOptsV3]):  Example: {'returns': {'array': True, 'type': 'IncidentStatus'},
            'source': 'metadata.annotations["github.com/repo"]'}.
    """

    operation_type: ExpressionOperationV3OperationType
    returns: "ReturnsMetaV3"
    branches: Union[Unset, "ExpressionBranchesOptsV3"] = UNSET
    cast: Union[Unset, "ExpressionCastOptsV3"] = UNSET
    concatenate: Union[Unset, "ExpressionConcatenateOptsV3"] = UNSET
    filter_: Union[Unset, "ExpressionFilterOptsV3"] = UNSET
    navigate: Union[Unset, "ExpressionNavigateOptsV3"] = UNSET
    parse: Union[Unset, "ExpressionParseOptsV3"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type.value

        returns = self.returns.to_dict()

        branches: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branches, Unset):
            branches = self.branches.to_dict()

        cast: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cast, Unset):
            cast = self.cast.to_dict()

        concatenate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.concatenate, Unset):
            concatenate = self.concatenate.to_dict()

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
        if cast is not UNSET:
            field_dict["cast"] = cast
        if concatenate is not UNSET:
            field_dict["concatenate"] = concatenate
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if navigate is not UNSET:
            field_dict["navigate"] = navigate
        if parse is not UNSET:
            field_dict["parse"] = parse

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.expression_branches_opts_v3 import ExpressionBranchesOptsV3
        from ..models.expression_cast_opts_v3 import ExpressionCastOptsV3
        from ..models.expression_concatenate_opts_v3 import ExpressionConcatenateOptsV3
        from ..models.expression_filter_opts_v3 import ExpressionFilterOptsV3
        from ..models.expression_navigate_opts_v3 import ExpressionNavigateOptsV3
        from ..models.expression_parse_opts_v3 import ExpressionParseOptsV3
        from ..models.returns_meta_v3 import ReturnsMetaV3

        d = src_dict.copy()
        operation_type = ExpressionOperationV3OperationType(d.pop("operation_type"))

        returns = ReturnsMetaV3.from_dict(d.pop("returns"))

        _branches = d.pop("branches", UNSET)
        branches: Union[Unset, ExpressionBranchesOptsV3]
        if isinstance(_branches, Unset):
            branches = UNSET
        else:
            branches = ExpressionBranchesOptsV3.from_dict(_branches)

        _cast = d.pop("cast", UNSET)
        cast: Union[Unset, ExpressionCastOptsV3]
        if isinstance(_cast, Unset):
            cast = UNSET
        else:
            cast = ExpressionCastOptsV3.from_dict(_cast)

        _concatenate = d.pop("concatenate", UNSET)
        concatenate: Union[Unset, ExpressionConcatenateOptsV3]
        if isinstance(_concatenate, Unset):
            concatenate = UNSET
        else:
            concatenate = ExpressionConcatenateOptsV3.from_dict(_concatenate)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, ExpressionFilterOptsV3]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ExpressionFilterOptsV3.from_dict(_filter_)

        _navigate = d.pop("navigate", UNSET)
        navigate: Union[Unset, ExpressionNavigateOptsV3]
        if isinstance(_navigate, Unset):
            navigate = UNSET
        else:
            navigate = ExpressionNavigateOptsV3.from_dict(_navigate)

        _parse = d.pop("parse", UNSET)
        parse: Union[Unset, ExpressionParseOptsV3]
        if isinstance(_parse, Unset):
            parse = UNSET
        else:
            parse = ExpressionParseOptsV3.from_dict(_parse)

        expression_operation_v3 = cls(
            operation_type=operation_type,
            returns=returns,
            branches=branches,
            cast=cast,
            concatenate=concatenate,
            filter_=filter_,
            navigate=navigate,
            parse=parse,
        )

        expression_operation_v3.additional_properties = d
        return expression_operation_v3

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
