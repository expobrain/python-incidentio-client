from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_route_escalation_binding_payload_v2_request_body import (
        AlertRouteEscalationBindingPayloadV2RequestBody,
    )
    from ..models.alert_route_incident_template_payload_v2_request_body import (
        AlertRouteIncidentTemplatePayloadV2RequestBody,
    )
    from ..models.condition_group_payload_v2_request_body import (
        ConditionGroupPayloadV2RequestBody,
    )
    from ..models.expression_payload_v2_request_body import (
        ExpressionPayloadV2RequestBody,
    )
    from ..models.grouping_key_v2_request_body import GroupingKeyV2RequestBody


T = TypeVar("T", bound="AlertRoutesV2CreateRequestBody")


@_attrs_define
class AlertRoutesV2CreateRequestBody:
    """
    Example:
        {'alert_source_ids': ['02FCNDV6P870EA6S7TK1DSYDG2'], 'auto_decline_enabled': False, 'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'defer_time_seconds': 1, 'enabled': False, 'escalation_bindings': [{'binding':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'expressions': [{'else_branch': {'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches': {'branches':
            [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}],
            'grouping_keys': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0'}], 'grouping_window_seconds': 1,
            'incident_condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'incident_enabled': False, 'name': 'Production
            incidents', 'template': {'custom_field_priorities': {'abc123': 'abc123'}, 'custom_fields':
            {'custom_field_10014': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'incident_mode': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'incident_type': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'name': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'priority_severity':
            'severity-first-wins', 'severity': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'summary': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'workspace': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}}

    Attributes:
        alert_source_ids (Union[Unset, List[str]]): Legacy field - the alert sources that will match this alert route
            Example: ['02FCNDV6P870EA6S7TK1DSYDG2'].
        auto_decline_enabled (Union[Unset, bool]): Should triage incidents be declined when alerts are resolved?
        condition_groups (Union[Unset, List['ConditionGroupPayloadV2RequestBody']]): What condition groups must be true
            for this alert route to fire? Example: [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}].
        defer_time_seconds (Union[Unset, int]): How long should the escalation defer time be? Example: 1.
        enabled (Union[Unset, bool]): Whether this alert route is enabled or not
        escalation_bindings (Union[Unset, List['AlertRouteEscalationBindingPayloadV2RequestBody']]): Which escalation
            paths should this alert route escalate to? Example: [{'binding': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}].
        expressions (Union[Unset, List['ExpressionPayloadV2RequestBody']]): The expressions used in this template
            Example: [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter': {'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}].
        grouping_keys (Union[Unset, List['GroupingKeyV2RequestBody']]): Which attributes should this alert route use to
            group alerts? Example: [{'id': '01FCNDV6P870EA6S7TK1DSYDG0'}].
        grouping_window_seconds (Union[Unset, int]): How large should the grouping window be? Example: 1.
        incident_condition_groups (Union[Unset, List['ConditionGroupPayloadV2RequestBody']]): What condition groups must
            be true for this alert route to create an incident? Example: [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}].
        incident_enabled (Union[Unset, bool]): Whether this alert route will create incidents or not
        name (Union[Unset, str]): The name of this alert route config, for the user's reference Example: Production
            incidents.
        template (Union[Unset, AlertRouteIncidentTemplatePayloadV2RequestBody]):  Example: {'custom_field_priorities':
            {'abc123': 'abc123'}, 'custom_fields': {'custom_field_10014': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'incident_mode': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'incident_type': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'name':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'priority_severity': 'severity-first-wins', 'severity': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'summary': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'workspace': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}.
    """

    alert_source_ids: Union[Unset, List[str]] = UNSET
    auto_decline_enabled: Union[Unset, bool] = UNSET
    condition_groups: Union[Unset, List["ConditionGroupPayloadV2RequestBody"]] = UNSET
    defer_time_seconds: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    escalation_bindings: Union[Unset, List["AlertRouteEscalationBindingPayloadV2RequestBody"]] = (
        UNSET
    )
    expressions: Union[Unset, List["ExpressionPayloadV2RequestBody"]] = UNSET
    grouping_keys: Union[Unset, List["GroupingKeyV2RequestBody"]] = UNSET
    grouping_window_seconds: Union[Unset, int] = UNSET
    incident_condition_groups: Union[Unset, List["ConditionGroupPayloadV2RequestBody"]] = UNSET
    incident_enabled: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    template: Union[Unset, "AlertRouteIncidentTemplatePayloadV2RequestBody"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_source_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.alert_source_ids, Unset):
            alert_source_ids = self.alert_source_ids

        auto_decline_enabled = self.auto_decline_enabled

        condition_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.condition_groups, Unset):
            condition_groups = []
            for condition_groups_item_data in self.condition_groups:
                condition_groups_item = condition_groups_item_data.to_dict()
                condition_groups.append(condition_groups_item)

        defer_time_seconds = self.defer_time_seconds

        enabled = self.enabled

        escalation_bindings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.escalation_bindings, Unset):
            escalation_bindings = []
            for escalation_bindings_item_data in self.escalation_bindings:
                escalation_bindings_item = escalation_bindings_item_data.to_dict()
                escalation_bindings.append(escalation_bindings_item)

        expressions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.expressions, Unset):
            expressions = []
            for expressions_item_data in self.expressions:
                expressions_item = expressions_item_data.to_dict()
                expressions.append(expressions_item)

        grouping_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.grouping_keys, Unset):
            grouping_keys = []
            for grouping_keys_item_data in self.grouping_keys:
                grouping_keys_item = grouping_keys_item_data.to_dict()
                grouping_keys.append(grouping_keys_item)

        grouping_window_seconds = self.grouping_window_seconds

        incident_condition_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.incident_condition_groups, Unset):
            incident_condition_groups = []
            for incident_condition_groups_item_data in self.incident_condition_groups:
                incident_condition_groups_item = incident_condition_groups_item_data.to_dict()
                incident_condition_groups.append(incident_condition_groups_item)

        incident_enabled = self.incident_enabled

        name = self.name

        template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_source_ids is not UNSET:
            field_dict["alert_source_ids"] = alert_source_ids
        if auto_decline_enabled is not UNSET:
            field_dict["auto_decline_enabled"] = auto_decline_enabled
        if condition_groups is not UNSET:
            field_dict["condition_groups"] = condition_groups
        if defer_time_seconds is not UNSET:
            field_dict["defer_time_seconds"] = defer_time_seconds
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if escalation_bindings is not UNSET:
            field_dict["escalation_bindings"] = escalation_bindings
        if expressions is not UNSET:
            field_dict["expressions"] = expressions
        if grouping_keys is not UNSET:
            field_dict["grouping_keys"] = grouping_keys
        if grouping_window_seconds is not UNSET:
            field_dict["grouping_window_seconds"] = grouping_window_seconds
        if incident_condition_groups is not UNSET:
            field_dict["incident_condition_groups"] = incident_condition_groups
        if incident_enabled is not UNSET:
            field_dict["incident_enabled"] = incident_enabled
        if name is not UNSET:
            field_dict["name"] = name
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_route_escalation_binding_payload_v2_request_body import (
            AlertRouteEscalationBindingPayloadV2RequestBody,
        )
        from ..models.alert_route_incident_template_payload_v2_request_body import (
            AlertRouteIncidentTemplatePayloadV2RequestBody,
        )
        from ..models.condition_group_payload_v2_request_body import (
            ConditionGroupPayloadV2RequestBody,
        )
        from ..models.expression_payload_v2_request_body import (
            ExpressionPayloadV2RequestBody,
        )
        from ..models.grouping_key_v2_request_body import GroupingKeyV2RequestBody

        d = src_dict.copy()
        alert_source_ids = cast(List[str], d.pop("alert_source_ids", UNSET))

        auto_decline_enabled = d.pop("auto_decline_enabled", UNSET)

        condition_groups = []
        _condition_groups = d.pop("condition_groups", UNSET)
        for condition_groups_item_data in _condition_groups or []:
            condition_groups_item = ConditionGroupPayloadV2RequestBody.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        defer_time_seconds = d.pop("defer_time_seconds", UNSET)

        enabled = d.pop("enabled", UNSET)

        escalation_bindings = []
        _escalation_bindings = d.pop("escalation_bindings", UNSET)
        for escalation_bindings_item_data in _escalation_bindings or []:
            escalation_bindings_item = AlertRouteEscalationBindingPayloadV2RequestBody.from_dict(
                escalation_bindings_item_data
            )

            escalation_bindings.append(escalation_bindings_item)

        expressions = []
        _expressions = d.pop("expressions", UNSET)
        for expressions_item_data in _expressions or []:
            expressions_item = ExpressionPayloadV2RequestBody.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        grouping_keys = []
        _grouping_keys = d.pop("grouping_keys", UNSET)
        for grouping_keys_item_data in _grouping_keys or []:
            grouping_keys_item = GroupingKeyV2RequestBody.from_dict(grouping_keys_item_data)

            grouping_keys.append(grouping_keys_item)

        grouping_window_seconds = d.pop("grouping_window_seconds", UNSET)

        incident_condition_groups = []
        _incident_condition_groups = d.pop("incident_condition_groups", UNSET)
        for incident_condition_groups_item_data in _incident_condition_groups or []:
            incident_condition_groups_item = ConditionGroupPayloadV2RequestBody.from_dict(
                incident_condition_groups_item_data
            )

            incident_condition_groups.append(incident_condition_groups_item)

        incident_enabled = d.pop("incident_enabled", UNSET)

        name = d.pop("name", UNSET)

        _template = d.pop("template", UNSET)
        template: Union[Unset, AlertRouteIncidentTemplatePayloadV2RequestBody]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = AlertRouteIncidentTemplatePayloadV2RequestBody.from_dict(_template)

        alert_routes_v2_create_request_body = cls(
            alert_source_ids=alert_source_ids,
            auto_decline_enabled=auto_decline_enabled,
            condition_groups=condition_groups,
            defer_time_seconds=defer_time_seconds,
            enabled=enabled,
            escalation_bindings=escalation_bindings,
            expressions=expressions,
            grouping_keys=grouping_keys,
            grouping_window_seconds=grouping_window_seconds,
            incident_condition_groups=incident_condition_groups,
            incident_enabled=incident_enabled,
            name=name,
            template=template,
        )

        alert_routes_v2_create_request_body.additional_properties = d
        return alert_routes_v2_create_request_body

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
