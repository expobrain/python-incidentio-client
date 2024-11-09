from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_route_escalation_binding_v2 import AlertRouteEscalationBindingV2
    from ..models.alert_route_incident_template_v2 import AlertRouteIncidentTemplateV2
    from ..models.condition_group_v2 import ConditionGroupV2
    from ..models.expression_v2 import ExpressionV2
    from ..models.grouping_key_v2 import GroupingKeyV2


T = TypeVar("T", bound="AlertRouteV2")


@_attrs_define
class AlertRouteV2:
    """
    Example:
        {'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'defer_time_seconds': 1, 'escalation_bindings': [{'binding': {'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}}], 'expressions': [{'else_branch':
            {'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team
            Slack channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident
            Severity', 'reference': 'incident.severity'}}]}], 'result': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}]}, 'navigate': {'reference': '1235', 'reference_label': 'Teams'}, 'operation_type':
            'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}, 'returns': {'array': True, 'type': 'IncidentStatus'}}], 'reference':
            'abc123', 'returns': {'array': True, 'type': 'IncidentStatus'}, 'root_reference': 'incident.status'}],
            'grouping_keys': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0'}], 'grouping_window_seconds': 1, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Production incidents', 'template': {'custom_field_priorities': {'abc123':
            'first-wins'}, 'custom_fields': {'custom_field_10014': {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'incident_mode': {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'incident_type': {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'name': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'priority_severity': 'severity-first-wins', 'severity': {'array_value': [{'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}}, 'summary': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'workspace': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}}}

    Attributes:
        condition_groups (List['ConditionGroupV2']): What condition groups must be true for this alert route to fire?
            Example: [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}]}].
        defer_time_seconds (int): How long should the escalation defer time be? Example: 1.
        escalation_bindings (List['AlertRouteEscalationBindingV2']): Which escalation paths should this alert route
            escalate to? Example: [{'binding': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}].
        grouping_keys (List['GroupingKeyV2']): Which attributes should this alert route use to group alerts? Example:
            [{'id': '01FCNDV6P870EA6S7TK1DSYDG0'}].
        grouping_window_seconds (int): How large should the grouping window be? Example: 1.
        id (str): Unique identifier for this alert route config Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): The name of this alert route config, for the user's reference Example: Production incidents.
        expressions (Union[Unset, List['ExpressionV2']]): The expressions used in this template Example:
            [{'else_branch': {'result': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
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
            'type': 'IncidentStatus'}, 'root_reference': 'incident.status'}].
        template (Union[Unset, AlertRouteIncidentTemplateV2]):  Example: {'custom_field_priorities': {'abc123': 'first-
            wins'}, 'custom_fields': {'custom_field_10014': {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'incident_mode': {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'incident_type': {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}, 'name': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}, 'priority_severity': 'severity-first-wins', 'severity': {'array_value': [{'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}}, 'summary': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'workspace': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}}.
    """

    condition_groups: List["ConditionGroupV2"]
    defer_time_seconds: int
    escalation_bindings: List["AlertRouteEscalationBindingV2"]
    grouping_keys: List["GroupingKeyV2"]
    grouping_window_seconds: int
    id: str
    name: str
    expressions: Union[Unset, List["ExpressionV2"]] = UNSET
    template: Union[Unset, "AlertRouteIncidentTemplateV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        defer_time_seconds = self.defer_time_seconds

        escalation_bindings = []
        for escalation_bindings_item_data in self.escalation_bindings:
            escalation_bindings_item = escalation_bindings_item_data.to_dict()
            escalation_bindings.append(escalation_bindings_item)

        grouping_keys = []
        for grouping_keys_item_data in self.grouping_keys:
            grouping_keys_item = grouping_keys_item_data.to_dict()
            grouping_keys.append(grouping_keys_item)

        grouping_window_seconds = self.grouping_window_seconds

        id = self.id

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
                "condition_groups": condition_groups,
                "defer_time_seconds": defer_time_seconds,
                "escalation_bindings": escalation_bindings,
                "grouping_keys": grouping_keys,
                "grouping_window_seconds": grouping_window_seconds,
                "id": id,
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
        from ..models.alert_route_escalation_binding_v2 import (
            AlertRouteEscalationBindingV2,
        )
        from ..models.alert_route_incident_template_v2 import (
            AlertRouteIncidentTemplateV2,
        )
        from ..models.condition_group_v2 import ConditionGroupV2
        from ..models.expression_v2 import ExpressionV2
        from ..models.grouping_key_v2 import GroupingKeyV2

        d = src_dict.copy()
        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupV2.from_dict(condition_groups_item_data)

            condition_groups.append(condition_groups_item)

        defer_time_seconds = d.pop("defer_time_seconds")

        escalation_bindings = []
        _escalation_bindings = d.pop("escalation_bindings")
        for escalation_bindings_item_data in _escalation_bindings:
            escalation_bindings_item = AlertRouteEscalationBindingV2.from_dict(
                escalation_bindings_item_data
            )

            escalation_bindings.append(escalation_bindings_item)

        grouping_keys = []
        _grouping_keys = d.pop("grouping_keys")
        for grouping_keys_item_data in _grouping_keys:
            grouping_keys_item = GroupingKeyV2.from_dict(grouping_keys_item_data)

            grouping_keys.append(grouping_keys_item)

        grouping_window_seconds = d.pop("grouping_window_seconds")

        id = d.pop("id")

        name = d.pop("name")

        expressions = []
        _expressions = d.pop("expressions", UNSET)
        for expressions_item_data in _expressions or []:
            expressions_item = ExpressionV2.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        _template = d.pop("template", UNSET)
        template: Union[Unset, AlertRouteIncidentTemplateV2]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = AlertRouteIncidentTemplateV2.from_dict(_template)

        alert_route_v2 = cls(
            condition_groups=condition_groups,
            defer_time_seconds=defer_time_seconds,
            escalation_bindings=escalation_bindings,
            grouping_keys=grouping_keys,
            grouping_window_seconds=grouping_window_seconds,
            id=id,
            name=name,
            expressions=expressions,
            template=template,
        )

        alert_route_v2.additional_properties = d
        return alert_route_v2

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
