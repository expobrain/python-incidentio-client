from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_route_alert_source_payload_v2 import (
        AlertRouteAlertSourcePayloadV2,
    )
    from ..models.alert_route_escalation_binding_payload_v2 import (
        AlertRouteEscalationBindingPayloadV2,
    )
    from ..models.alert_route_incident_template_payload_v2 import (
        AlertRouteIncidentTemplatePayloadV2,
    )
    from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2
    from ..models.expression_payload_v2 import ExpressionPayloadV2
    from ..models.grouping_key_v2 import GroupingKeyV2


T = TypeVar("T", bound="AlertRoutesV2UpdateRequestBody")


@_attrs_define
class AlertRoutesV2UpdateRequestBody:
    """
    Example:
        {'alert_sources': [{'alert_source_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}], 'auto_decline_enabled': False, 'condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}],
            'defer_time_seconds': 1, 'enabled': False, 'escalation_bindings': [{'binding': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'expressions': [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label':
            'Team Slack channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type':
            'IncidentStatus'}}, 'filter': {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123',
            'root_reference': 'incident.status'}], 'grouping_keys': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0'}],
            'grouping_window_seconds': 1, 'incident_condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}],
            'incident_enabled': False, 'name': 'Production incidents', 'template': {'custom_field_priorities': {'abc123':
            'abc123'}, 'custom_fields': {'custom_field_10014': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'incident_mode':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'incident_type': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'name':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'priority_severity': 'severity-first-wins', 'severity': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'summary': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'workspace': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}}

    Attributes:
        alert_sources (List['AlertRouteAlertSourcePayloadV2']): Which alert sources should this alert route match?
            Example: [{'alert_source_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}]}].
        auto_decline_enabled (bool): Should triage incidents be declined when alerts are resolved?
        condition_groups (List['ConditionGroupPayloadV2']): What condition groups must be true for this alert route to
            fire? Example: [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}].
        defer_time_seconds (int): How long should the escalation defer time be? Example: 1.
        enabled (bool): Whether this alert route is enabled or not
        escalation_bindings (List['AlertRouteEscalationBindingPayloadV2']): Which escalation paths should this alert
            route escalate to? Example: [{'binding': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}].
        grouping_keys (List['GroupingKeyV2']): Which attributes should this alert route use to group alerts? Example:
            [{'id': '01FCNDV6P870EA6S7TK1DSYDG0'}].
        grouping_window_seconds (int): How large should the grouping window be? Example: 1.
        incident_condition_groups (List['ConditionGroupPayloadV2']): What condition groups must be true for this alert
            route to create an incident? Example: [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}].
        incident_enabled (bool): Whether this alert route will create incidents or not
        name (str): The name of this alert route config, for the user's reference Example: Production incidents.
        expressions (Union[Unset, List['ExpressionPayloadV2']]): The expressions used in this template Example:
            [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
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
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}].
        template (Union[Unset, AlertRouteIncidentTemplatePayloadV2]):  Example: {'custom_field_priorities': {'abc123':
            'abc123'}, 'custom_fields': {'custom_field_10014': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'incident_mode':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'incident_type': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'name':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'priority_severity': 'severity-first-wins', 'severity': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'summary': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'workspace': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}.
    """

    alert_sources: List["AlertRouteAlertSourcePayloadV2"]
    auto_decline_enabled: bool
    condition_groups: List["ConditionGroupPayloadV2"]
    defer_time_seconds: int
    enabled: bool
    escalation_bindings: List["AlertRouteEscalationBindingPayloadV2"]
    grouping_keys: List["GroupingKeyV2"]
    grouping_window_seconds: int
    incident_condition_groups: List["ConditionGroupPayloadV2"]
    incident_enabled: bool
    name: str
    expressions: Union[Unset, List["ExpressionPayloadV2"]] = UNSET
    template: Union[Unset, "AlertRouteIncidentTemplatePayloadV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_sources = []
        for alert_sources_item_data in self.alert_sources:
            alert_sources_item = alert_sources_item_data.to_dict()
            alert_sources.append(alert_sources_item)

        auto_decline_enabled = self.auto_decline_enabled

        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        defer_time_seconds = self.defer_time_seconds

        enabled = self.enabled

        escalation_bindings = []
        for escalation_bindings_item_data in self.escalation_bindings:
            escalation_bindings_item = escalation_bindings_item_data.to_dict()
            escalation_bindings.append(escalation_bindings_item)

        grouping_keys = []
        for grouping_keys_item_data in self.grouping_keys:
            grouping_keys_item = grouping_keys_item_data.to_dict()
            grouping_keys.append(grouping_keys_item)

        grouping_window_seconds = self.grouping_window_seconds

        incident_condition_groups = []
        for incident_condition_groups_item_data in self.incident_condition_groups:
            incident_condition_groups_item = incident_condition_groups_item_data.to_dict()
            incident_condition_groups.append(incident_condition_groups_item)

        incident_enabled = self.incident_enabled

        name = self.name

        expressions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.expressions, Unset):
            expressions = []
            for expressions_item_data in self.expressions:
                expressions_item = expressions_item_data.to_dict()
                expressions.append(expressions_item)

        template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_sources": alert_sources,
                "auto_decline_enabled": auto_decline_enabled,
                "condition_groups": condition_groups,
                "defer_time_seconds": defer_time_seconds,
                "enabled": enabled,
                "escalation_bindings": escalation_bindings,
                "grouping_keys": grouping_keys,
                "grouping_window_seconds": grouping_window_seconds,
                "incident_condition_groups": incident_condition_groups,
                "incident_enabled": incident_enabled,
                "name": name,
            }
        )
        if expressions is not UNSET:
            field_dict["expressions"] = expressions
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_route_alert_source_payload_v2 import (
            AlertRouteAlertSourcePayloadV2,
        )
        from ..models.alert_route_escalation_binding_payload_v2 import (
            AlertRouteEscalationBindingPayloadV2,
        )
        from ..models.alert_route_incident_template_payload_v2 import (
            AlertRouteIncidentTemplatePayloadV2,
        )
        from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2
        from ..models.expression_payload_v2 import ExpressionPayloadV2
        from ..models.grouping_key_v2 import GroupingKeyV2

        d = src_dict.copy()
        alert_sources = []
        _alert_sources = d.pop("alert_sources")
        for alert_sources_item_data in _alert_sources:
            alert_sources_item = AlertRouteAlertSourcePayloadV2.from_dict(alert_sources_item_data)

            alert_sources.append(alert_sources_item)

        auto_decline_enabled = d.pop("auto_decline_enabled")

        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV2.from_dict(condition_groups_item_data)

            condition_groups.append(condition_groups_item)

        defer_time_seconds = d.pop("defer_time_seconds")

        enabled = d.pop("enabled")

        escalation_bindings = []
        _escalation_bindings = d.pop("escalation_bindings")
        for escalation_bindings_item_data in _escalation_bindings:
            escalation_bindings_item = AlertRouteEscalationBindingPayloadV2.from_dict(
                escalation_bindings_item_data
            )

            escalation_bindings.append(escalation_bindings_item)

        grouping_keys = []
        _grouping_keys = d.pop("grouping_keys")
        for grouping_keys_item_data in _grouping_keys:
            grouping_keys_item = GroupingKeyV2.from_dict(grouping_keys_item_data)

            grouping_keys.append(grouping_keys_item)

        grouping_window_seconds = d.pop("grouping_window_seconds")

        incident_condition_groups = []
        _incident_condition_groups = d.pop("incident_condition_groups")
        for incident_condition_groups_item_data in _incident_condition_groups:
            incident_condition_groups_item = ConditionGroupPayloadV2.from_dict(
                incident_condition_groups_item_data
            )

            incident_condition_groups.append(incident_condition_groups_item)

        incident_enabled = d.pop("incident_enabled")

        name = d.pop("name")

        expressions = []
        _expressions = d.pop("expressions", UNSET)
        for expressions_item_data in _expressions or []:
            expressions_item = ExpressionPayloadV2.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        _template = d.pop("template", UNSET)
        template: Union[Unset, AlertRouteIncidentTemplatePayloadV2]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = AlertRouteIncidentTemplatePayloadV2.from_dict(_template)

        alert_routes_v2_update_request_body = cls(
            alert_sources=alert_sources,
            auto_decline_enabled=auto_decline_enabled,
            condition_groups=condition_groups,
            defer_time_seconds=defer_time_seconds,
            enabled=enabled,
            escalation_bindings=escalation_bindings,
            grouping_keys=grouping_keys,
            grouping_window_seconds=grouping_window_seconds,
            incident_condition_groups=incident_condition_groups,
            incident_enabled=incident_enabled,
            name=name,
            expressions=expressions,
            template=template,
        )

        alert_routes_v2_update_request_body.additional_properties = d
        return alert_routes_v2_update_request_body

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
