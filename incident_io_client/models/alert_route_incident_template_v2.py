from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_route_incident_template_v2_priority_severity import (
    AlertRouteIncidentTemplateV2PrioritySeverity,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_route_incident_template_v2_custom_field_priorities import (
        AlertRouteIncidentTemplateV2CustomFieldPriorities,
    )
    from ..models.alert_route_incident_template_v2_custom_fields import (
        AlertRouteIncidentTemplateV2CustomFields,
    )
    from ..models.engine_param_binding_v2 import EngineParamBindingV2


T = TypeVar("T", bound="AlertRouteIncidentTemplateV2")


@_attrs_define
class AlertRouteIncidentTemplateV2:
    """
    Example:
        {'custom_field_priorities': {'abc123': 'first-wins'}, 'custom_fields': {'custom_field_10014': {'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'incident_mode': {'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}, 'incident_type': {'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}, 'name': {'array_value': [{'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}}, 'priority_severity': 'severity-first-wins', 'severity':
            {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}, 'summary': {'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}, 'workspace': {'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}}

    Attributes:
        custom_field_priorities (AlertRouteIncidentTemplateV2CustomFieldPriorities): lookup of the priority options for
            each custom field in the template Example: {'abc123': 'first-wins'}.
        priority_severity (AlertRouteIncidentTemplateV2PrioritySeverity): binding to use to resolve the workspace to
            create an incident in Example: severity-first-wins.
        custom_fields (Union[Unset, AlertRouteIncidentTemplateV2CustomFields]): Custom field keys mapped to values
            Example: {'custom_field_10014': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}}.
        incident_mode (Union[Unset, EngineParamBindingV2]):  Example: {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}.
        incident_type (Union[Unset, EngineParamBindingV2]):  Example: {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}.
        name (Union[Unset, EngineParamBindingV2]):  Example: {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}.
        severity (Union[Unset, EngineParamBindingV2]):  Example: {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}.
        summary (Union[Unset, EngineParamBindingV2]):  Example: {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}.
        workspace (Union[Unset, EngineParamBindingV2]):  Example: {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}.
    """

    custom_field_priorities: "AlertRouteIncidentTemplateV2CustomFieldPriorities"
    priority_severity: AlertRouteIncidentTemplateV2PrioritySeverity
    custom_fields: Union[Unset, "AlertRouteIncidentTemplateV2CustomFields"] = UNSET
    incident_mode: Union[Unset, "EngineParamBindingV2"] = UNSET
    incident_type: Union[Unset, "EngineParamBindingV2"] = UNSET
    name: Union[Unset, "EngineParamBindingV2"] = UNSET
    severity: Union[Unset, "EngineParamBindingV2"] = UNSET
    summary: Union[Unset, "EngineParamBindingV2"] = UNSET
    workspace: Union[Unset, "EngineParamBindingV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_field_priorities = self.custom_field_priorities.to_dict()

        priority_severity = self.priority_severity.value

        custom_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        incident_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.incident_mode, Unset):
            incident_mode = self.incident_mode.to_dict()

        incident_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.incident_type, Unset):
            incident_type = self.incident_type.to_dict()

        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        severity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.to_dict()

        summary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        workspace: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workspace, Unset):
            workspace = self.workspace.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field_priorities": custom_field_priorities,
                "priority_severity": priority_severity,
            }
        )
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if incident_mode is not UNSET:
            field_dict["incident_mode"] = incident_mode
        if incident_type is not UNSET:
            field_dict["incident_type"] = incident_type
        if name is not UNSET:
            field_dict["name"] = name
        if severity is not UNSET:
            field_dict["severity"] = severity
        if summary is not UNSET:
            field_dict["summary"] = summary
        if workspace is not UNSET:
            field_dict["workspace"] = workspace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_route_incident_template_v2_custom_field_priorities import (
            AlertRouteIncidentTemplateV2CustomFieldPriorities,
        )
        from ..models.alert_route_incident_template_v2_custom_fields import (
            AlertRouteIncidentTemplateV2CustomFields,
        )
        from ..models.engine_param_binding_v2 import EngineParamBindingV2

        d = src_dict.copy()
        custom_field_priorities = AlertRouteIncidentTemplateV2CustomFieldPriorities.from_dict(
            d.pop("custom_field_priorities")
        )

        priority_severity = AlertRouteIncidentTemplateV2PrioritySeverity(
            d.pop("priority_severity")
        )

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, AlertRouteIncidentTemplateV2CustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = AlertRouteIncidentTemplateV2CustomFields.from_dict(_custom_fields)

        _incident_mode = d.pop("incident_mode", UNSET)
        incident_mode: Union[Unset, EngineParamBindingV2]
        if isinstance(_incident_mode, Unset):
            incident_mode = UNSET
        else:
            incident_mode = EngineParamBindingV2.from_dict(_incident_mode)

        _incident_type = d.pop("incident_type", UNSET)
        incident_type: Union[Unset, EngineParamBindingV2]
        if isinstance(_incident_type, Unset):
            incident_type = UNSET
        else:
            incident_type = EngineParamBindingV2.from_dict(_incident_type)

        _name = d.pop("name", UNSET)
        name: Union[Unset, EngineParamBindingV2]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = EngineParamBindingV2.from_dict(_name)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, EngineParamBindingV2]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = EngineParamBindingV2.from_dict(_severity)

        _summary = d.pop("summary", UNSET)
        summary: Union[Unset, EngineParamBindingV2]
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = EngineParamBindingV2.from_dict(_summary)

        _workspace = d.pop("workspace", UNSET)
        workspace: Union[Unset, EngineParamBindingV2]
        if isinstance(_workspace, Unset):
            workspace = UNSET
        else:
            workspace = EngineParamBindingV2.from_dict(_workspace)

        alert_route_incident_template_v2 = cls(
            custom_field_priorities=custom_field_priorities,
            priority_severity=priority_severity,
            custom_fields=custom_fields,
            incident_mode=incident_mode,
            incident_type=incident_type,
            name=name,
            severity=severity,
            summary=summary,
            workspace=workspace,
        )

        alert_route_incident_template_v2.additional_properties = d
        return alert_route_incident_template_v2

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
