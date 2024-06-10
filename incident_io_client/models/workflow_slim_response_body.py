import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.workflow_slim_response_body_runs_on_incident_modes_item import (
    WorkflowSlimResponseBodyRunsOnIncidentModesItem,
)
from ..models.workflow_slim_response_body_runs_on_incidents import (
    WorkflowSlimResponseBodyRunsOnIncidents,
)
from ..models.workflow_slim_response_body_state import WorkflowSlimResponseBodyState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_group_v2_response_body import ConditionGroupV2ResponseBody
    from ..models.engine_reference_v2_response_body import EngineReferenceV2ResponseBody
    from ..models.expression_v2_response_body import ExpressionV2ResponseBody
    from ..models.step_config_slim_response_body import StepConfigSlimResponseBody
    from ..models.trigger_slim_response_body import TriggerSlimResponseBody
    from ..models.workflow_delay_response_body import WorkflowDelayResponseBody


T = TypeVar("T", bound="WorkflowSlimResponseBody")


@_attrs_define
class WorkflowSlimResponseBody:
    """
    Example:
        {'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}]}], 'continue_on_step_error': True, 'delay': {'conditions_apply_over_delay': False,
            'for_seconds': 60}, 'expressions': [{'else_branch': {'result': {'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches':
            {'branches': [{'condition_groups': [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
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
            'type': 'IncidentStatus'}, 'root_reference': 'incident.status'}], 'folder': 'My folder 01', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'include_private_incidents': True, 'name': 'My workflow', 'once_for': [{'array':
            False, 'key': 'incident.custom_field["01FCNDV6P870EA6S7TK1DSYDG0"]', 'label': 'Incident -> Affected Team',
            'type': 'IncidentSeverity'}], 'runs_from': '2021-08-17T13:28:57.801578Z', 'runs_on_incident_modes': ['standard',
            'retrospective'], 'runs_on_incidents': 'newly_created', 'state': 'active', 'steps': [{'label': 'PagerDuty
            Escalate', 'name': 'pagerduty.escalate'}], 'trigger': {'label': 'Incident Updated', 'name': 'incident.updated'},
            'version': 3}

    Attributes:
        condition_groups (List['ConditionGroupV2ResponseBody']): Conditions that apply to the workflow trigger Example:
            [{'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}]}].
        continue_on_step_error (bool): Whether to continue executing the workflow if a step fails Example: True.
        expressions (List['ExpressionV2ResponseBody']): Expressions that make variables available in the scope Example:
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
        id (str): Unique identifier for the workflow Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        include_private_incidents (bool): Whether to include private incidents Example: True.
        name (str): The human-readable name of the workflow Example: My workflow.
        once_for (List['EngineReferenceV2ResponseBody']): This workflow will run 'once for' a list of references
            Example: [{'array': False, 'key': 'incident.custom_field["01FCNDV6P870EA6S7TK1DSYDG0"]', 'label': 'Incident ->
            Affected Team', 'type': 'IncidentSeverity'}].
        runs_on_incident_modes (List[WorkflowSlimResponseBodyRunsOnIncidentModesItem]): Which modes of incident this
            should run on (defaults to just standard incidents) Example: ['standard', 'retrospective'].
        runs_on_incidents (WorkflowSlimResponseBodyRunsOnIncidents): Which incidents should the workflow be applied to?
            (newly_created or newly_created_and_active) Example: newly_created.
        state (WorkflowSlimResponseBodyState): The state of the workflow (e.g. is it draft, or disabled) Example:
            active.
        steps (List['StepConfigSlimResponseBody']): Steps that are executed as part of the workflow Example: [{'label':
            'PagerDuty Escalate', 'name': 'pagerduty.escalate'}].
        trigger (TriggerSlimResponseBody):  Example: {'label': 'Incident Updated', 'name': 'incident.updated'}.
        version (int): Revision of the workflow, uniquely identifying its version Example: 3.
        delay (Union[Unset, WorkflowDelayResponseBody]):  Example: {'conditions_apply_over_delay': False, 'for_seconds':
            60}.
        folder (Union[Unset, str]): Folder to display the workflow in Example: My folder 01.
        runs_from (Union[Unset, datetime.datetime]): The time from which this workflow will run on incidents Example:
            2021-08-17T13:28:57.801578Z.
    """

    condition_groups: List["ConditionGroupV2ResponseBody"]
    continue_on_step_error: bool
    expressions: List["ExpressionV2ResponseBody"]
    id: str
    include_private_incidents: bool
    name: str
    once_for: List["EngineReferenceV2ResponseBody"]
    runs_on_incident_modes: List[WorkflowSlimResponseBodyRunsOnIncidentModesItem]
    runs_on_incidents: WorkflowSlimResponseBodyRunsOnIncidents
    state: WorkflowSlimResponseBodyState
    steps: List["StepConfigSlimResponseBody"]
    trigger: "TriggerSlimResponseBody"
    version: int
    delay: Union[Unset, "WorkflowDelayResponseBody"] = UNSET
    folder: Union[Unset, str] = UNSET
    runs_from: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        continue_on_step_error = self.continue_on_step_error

        expressions = []
        for expressions_item_data in self.expressions:
            expressions_item = expressions_item_data.to_dict()
            expressions.append(expressions_item)

        id = self.id

        include_private_incidents = self.include_private_incidents

        name = self.name

        once_for = []
        for once_for_item_data in self.once_for:
            once_for_item = once_for_item_data.to_dict()
            once_for.append(once_for_item)

        runs_on_incident_modes = []
        for runs_on_incident_modes_item_data in self.runs_on_incident_modes:
            runs_on_incident_modes_item = runs_on_incident_modes_item_data.value
            runs_on_incident_modes.append(runs_on_incident_modes_item)

        runs_on_incidents = self.runs_on_incidents.value

        state = self.state.value

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        trigger = self.trigger.to_dict()

        version = self.version

        delay: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delay, Unset):
            delay = self.delay.to_dict()

        folder = self.folder

        runs_from: Union[Unset, str] = UNSET
        if not isinstance(self.runs_from, Unset):
            runs_from = self.runs_from.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition_groups": condition_groups,
                "continue_on_step_error": continue_on_step_error,
                "expressions": expressions,
                "id": id,
                "include_private_incidents": include_private_incidents,
                "name": name,
                "once_for": once_for,
                "runs_on_incident_modes": runs_on_incident_modes,
                "runs_on_incidents": runs_on_incidents,
                "state": state,
                "steps": steps,
                "trigger": trigger,
                "version": version,
            }
        )
        if delay is not UNSET:
            field_dict["delay"] = delay
        if folder is not UNSET:
            field_dict["folder"] = folder
        if runs_from is not UNSET:
            field_dict["runs_from"] = runs_from

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.condition_group_v2_response_body import (
            ConditionGroupV2ResponseBody,
        )
        from ..models.engine_reference_v2_response_body import (
            EngineReferenceV2ResponseBody,
        )
        from ..models.expression_v2_response_body import ExpressionV2ResponseBody
        from ..models.step_config_slim_response_body import StepConfigSlimResponseBody
        from ..models.trigger_slim_response_body import TriggerSlimResponseBody
        from ..models.workflow_delay_response_body import WorkflowDelayResponseBody

        d = src_dict.copy()
        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupV2ResponseBody.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        continue_on_step_error = d.pop("continue_on_step_error")

        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = ExpressionV2ResponseBody.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        id = d.pop("id")

        include_private_incidents = d.pop("include_private_incidents")

        name = d.pop("name")

        once_for = []
        _once_for = d.pop("once_for")
        for once_for_item_data in _once_for:
            once_for_item = EngineReferenceV2ResponseBody.from_dict(once_for_item_data)

            once_for.append(once_for_item)

        runs_on_incident_modes = []
        _runs_on_incident_modes = d.pop("runs_on_incident_modes")
        for runs_on_incident_modes_item_data in _runs_on_incident_modes:
            runs_on_incident_modes_item = WorkflowSlimResponseBodyRunsOnIncidentModesItem(
                runs_on_incident_modes_item_data
            )

            runs_on_incident_modes.append(runs_on_incident_modes_item)

        runs_on_incidents = WorkflowSlimResponseBodyRunsOnIncidents(d.pop("runs_on_incidents"))

        state = WorkflowSlimResponseBodyState(d.pop("state"))

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = StepConfigSlimResponseBody.from_dict(steps_item_data)

            steps.append(steps_item)

        trigger = TriggerSlimResponseBody.from_dict(d.pop("trigger"))

        version = d.pop("version")

        _delay = d.pop("delay", UNSET)
        delay: Union[Unset, WorkflowDelayResponseBody]
        if isinstance(_delay, Unset):
            delay = UNSET
        else:
            delay = WorkflowDelayResponseBody.from_dict(_delay)

        folder = d.pop("folder", UNSET)

        _runs_from = d.pop("runs_from", UNSET)
        runs_from: Union[Unset, datetime.datetime]
        if isinstance(_runs_from, Unset):
            runs_from = UNSET
        else:
            runs_from = isoparse(_runs_from)

        workflow_slim_response_body = cls(
            condition_groups=condition_groups,
            continue_on_step_error=continue_on_step_error,
            expressions=expressions,
            id=id,
            include_private_incidents=include_private_incidents,
            name=name,
            once_for=once_for,
            runs_on_incident_modes=runs_on_incident_modes,
            runs_on_incidents=runs_on_incidents,
            state=state,
            steps=steps,
            trigger=trigger,
            version=version,
            delay=delay,
            folder=folder,
            runs_from=runs_from,
        )

        workflow_slim_response_body.additional_properties = d
        return workflow_slim_response_body

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
