from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expression_operation_payload_v2_request_body_operation_type import (
    ExpressionOperationPayloadV2RequestBodyOperationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expression_branches_opts_payload_v2_request_body import (
        ExpressionBranchesOptsPayloadV2RequestBody,
    )
    from ..models.expression_filter_opts_payload_v2_request_body import (
        ExpressionFilterOptsPayloadV2RequestBody,
    )
    from ..models.expression_navigate_opts_payload_v2_request_body import (
        ExpressionNavigateOptsPayloadV2RequestBody,
    )
    from ..models.expression_parse_opts_payload_v2_request_body import (
        ExpressionParseOptsPayloadV2RequestBody,
    )


T = TypeVar("T", bound="ExpressionOperationPayloadV2RequestBody")


@_attrs_define
class ExpressionOperationPayloadV2RequestBody:
    """
    Example:
        {'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}

    Attributes:
        operation_type (ExpressionOperationPayloadV2RequestBodyOperationType): The type of the operation Example:
            navigate.
        branches (Union[Unset, ExpressionBranchesOptsPayloadV2RequestBody]):  Example: {'branches':
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}.
        filter_ (Union[Unset, ExpressionFilterOptsPayloadV2RequestBody]):  Example: {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}.
        navigate (Union[Unset, ExpressionNavigateOptsPayloadV2RequestBody]):  Example: {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}.
        parse (Union[Unset, ExpressionParseOptsPayloadV2RequestBody]):  Example: {'returns': {'array': True, 'type':
            'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}.
    """

    operation_type: ExpressionOperationPayloadV2RequestBodyOperationType
    branches: Union[Unset, "ExpressionBranchesOptsPayloadV2RequestBody"] = UNSET
    filter_: Union[Unset, "ExpressionFilterOptsPayloadV2RequestBody"] = UNSET
    navigate: Union[Unset, "ExpressionNavigateOptsPayloadV2RequestBody"] = UNSET
    parse: Union[Unset, "ExpressionParseOptsPayloadV2RequestBody"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type = self.operation_type.value

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
        from ..models.expression_branches_opts_payload_v2_request_body import (
            ExpressionBranchesOptsPayloadV2RequestBody,
        )
        from ..models.expression_filter_opts_payload_v2_request_body import (
            ExpressionFilterOptsPayloadV2RequestBody,
        )
        from ..models.expression_navigate_opts_payload_v2_request_body import (
            ExpressionNavigateOptsPayloadV2RequestBody,
        )
        from ..models.expression_parse_opts_payload_v2_request_body import (
            ExpressionParseOptsPayloadV2RequestBody,
        )

        d = src_dict.copy()
        operation_type = ExpressionOperationPayloadV2RequestBodyOperationType(
            d.pop("operation_type")
        )

        _branches = d.pop("branches", UNSET)
        branches: Union[Unset, ExpressionBranchesOptsPayloadV2RequestBody]
        if isinstance(_branches, Unset):
            branches = UNSET
        else:
            branches = ExpressionBranchesOptsPayloadV2RequestBody.from_dict(_branches)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, ExpressionFilterOptsPayloadV2RequestBody]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ExpressionFilterOptsPayloadV2RequestBody.from_dict(_filter_)

        _navigate = d.pop("navigate", UNSET)
        navigate: Union[Unset, ExpressionNavigateOptsPayloadV2RequestBody]
        if isinstance(_navigate, Unset):
            navigate = UNSET
        else:
            navigate = ExpressionNavigateOptsPayloadV2RequestBody.from_dict(_navigate)

        _parse = d.pop("parse", UNSET)
        parse: Union[Unset, ExpressionParseOptsPayloadV2RequestBody]
        if isinstance(_parse, Unset):
            parse = UNSET
        else:
            parse = ExpressionParseOptsPayloadV2RequestBody.from_dict(_parse)

        expression_operation_payload_v2_request_body = cls(
            operation_type=operation_type,
            branches=branches,
            filter_=filter_,
            navigate=navigate,
            parse=parse,
        )

        expression_operation_payload_v2_request_body.additional_properties = d
        return expression_operation_payload_v2_request_body

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
