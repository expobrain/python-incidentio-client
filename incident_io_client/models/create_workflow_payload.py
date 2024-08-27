from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_workflow_payload_runs_on_incident_modes_item import (
    CreateWorkflowPayloadRunsOnIncidentModesItem,
)
from ..models.create_workflow_payload_runs_on_incidents import (
    CreateWorkflowPayloadRunsOnIncidents,
)
from ..models.create_workflow_payload_state import CreateWorkflowPayloadState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2
    from ..models.create_workflow_payload_annotations import (
        CreateWorkflowPayloadAnnotations,
    )
    from ..models.expression_payload_v2 import ExpressionPayloadV2
    from ..models.step_config_payload import StepConfigPayload
    from ..models.workflow_delay import WorkflowDelay


T = TypeVar("T", bound="CreateWorkflowPayload")


@_attrs_define
class CreateWorkflowPayload:
    """
    Example:
        {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}],
            'continue_on_step_error': True, 'delay': {'conditions_apply_over_delay': False, 'for_seconds': 60},
            'expressions': [{'else_branch': {'result': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack
            channel', 'operations': [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse': {'returns': {'array':
            True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123',
            'root_reference': 'incident.status'}], 'folder': 'My folder 01', 'include_private_incidents': True, 'name': 'My
            workflow', 'once_for': ['incident.url'], 'runs_on_incident_modes': ['standard', 'retrospective'],
            'runs_on_incidents': 'newly_created', 'shortform': 'abc123', 'state': 'active', 'steps': [{'for_each': 'abc123',
            'id': 'abc123', 'name': 'pagerduty.escalate', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}]}],
            'trigger': 'incident.updated'}

    Attributes:
        condition_groups (List['ConditionGroupPayloadV2']): List of conditions to apply to the workflow Example:
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}].
        continue_on_step_error (bool): Whether to continue executing the workflow if a step fails Example: True.
        expressions (List['ExpressionPayloadV2']): The expressions used in the workflow Example: [{'else_branch':
            {'result': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations': [{'branches':
            {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}}],
            'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter': {'condition_groups': [{'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'},
            'operation_type': 'navigate', 'parse': {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference': 'incident.status'}].
        include_private_incidents (bool): Whether to include private incidents Example: True.
        name (str): The human-readable name of the workflow Example: My workflow.
        once_for (List[str]): Once For strategy to apply to this workflow Example: ['incident.url'].
        runs_on_incident_modes (List[CreateWorkflowPayloadRunsOnIncidentModesItem]): Which modes of incident this should
            run on (defaults to just standard incidents) Example: ['standard', 'retrospective'].
        runs_on_incidents (CreateWorkflowPayloadRunsOnIncidents): Which incidents should the workflow be applied to?
            (newly_created or newly_created_and_active) Example: newly_created.
        steps (List['StepConfigPayload']): List of step to execute as part of the workflow Example: [{'for_each':
            'abc123', 'id': 'abc123', 'name': 'pagerduty.escalate', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}]}].
        trigger (str): Trigger to set on the workflow Example: incident.updated.
        annotations (Union[Unset, CreateWorkflowPayloadAnnotations]): Annotations that track metadata about this
            resource Example: {'incident.io/terraform/version': '3.0.0'}.
        delay (Union[Unset, WorkflowDelay]):  Example: {'conditions_apply_over_delay': False, 'for_seconds': 60}.
        folder (Union[Unset, str]): Folder to display the workflow in Example: My folder 01.
        shortform (Union[Unset, str]): Shortform used to trigger manual workflows in Slack - e.g. `/inc workflows page-
            ceo` Example: abc123.
        state (Union[Unset, CreateWorkflowPayloadState]): The state of the workflow (e.g. is it draft, or disabled)
            Example: active.
    """

    condition_groups: List["ConditionGroupPayloadV2"]
    continue_on_step_error: bool
    expressions: List["ExpressionPayloadV2"]
    include_private_incidents: bool
    name: str
    once_for: List[str]
    runs_on_incident_modes: List[CreateWorkflowPayloadRunsOnIncidentModesItem]
    runs_on_incidents: CreateWorkflowPayloadRunsOnIncidents
    steps: List["StepConfigPayload"]
    trigger: str
    annotations: Union[Unset, "CreateWorkflowPayloadAnnotations"] = UNSET
    delay: Union[Unset, "WorkflowDelay"] = UNSET
    folder: Union[Unset, str] = UNSET
    shortform: Union[Unset, str] = UNSET
    state: Union[Unset, CreateWorkflowPayloadState] = UNSET
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

        include_private_incidents = self.include_private_incidents

        name = self.name

        once_for = self.once_for

        runs_on_incident_modes = []
        for runs_on_incident_modes_item_data in self.runs_on_incident_modes:
            runs_on_incident_modes_item = runs_on_incident_modes_item_data.value
            runs_on_incident_modes.append(runs_on_incident_modes_item)

        runs_on_incidents = self.runs_on_incidents.value

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        trigger = self.trigger

        annotations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        delay: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delay, Unset):
            delay = self.delay.to_dict()

        folder = self.folder

        shortform = self.shortform

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition_groups": condition_groups,
                "continue_on_step_error": continue_on_step_error,
                "expressions": expressions,
                "include_private_incidents": include_private_incidents,
                "name": name,
                "once_for": once_for,
                "runs_on_incident_modes": runs_on_incident_modes,
                "runs_on_incidents": runs_on_incidents,
                "steps": steps,
                "trigger": trigger,
            }
        )
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if delay is not UNSET:
            field_dict["delay"] = delay
        if folder is not UNSET:
            field_dict["folder"] = folder
        if shortform is not UNSET:
            field_dict["shortform"] = shortform
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.condition_group_payload_v2 import ConditionGroupPayloadV2
        from ..models.create_workflow_payload_annotations import (
            CreateWorkflowPayloadAnnotations,
        )
        from ..models.expression_payload_v2 import ExpressionPayloadV2
        from ..models.step_config_payload import StepConfigPayload
        from ..models.workflow_delay import WorkflowDelay

        d = src_dict.copy()
        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV2.from_dict(condition_groups_item_data)

            condition_groups.append(condition_groups_item)

        continue_on_step_error = d.pop("continue_on_step_error")

        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = ExpressionPayloadV2.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        include_private_incidents = d.pop("include_private_incidents")

        name = d.pop("name")

        once_for = cast(List[str], d.pop("once_for"))

        runs_on_incident_modes = []
        _runs_on_incident_modes = d.pop("runs_on_incident_modes")
        for runs_on_incident_modes_item_data in _runs_on_incident_modes:
            runs_on_incident_modes_item = CreateWorkflowPayloadRunsOnIncidentModesItem(
                runs_on_incident_modes_item_data
            )

            runs_on_incident_modes.append(runs_on_incident_modes_item)

        runs_on_incidents = CreateWorkflowPayloadRunsOnIncidents(d.pop("runs_on_incidents"))

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = StepConfigPayload.from_dict(steps_item_data)

            steps.append(steps_item)

        trigger = d.pop("trigger")

        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, CreateWorkflowPayloadAnnotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = CreateWorkflowPayloadAnnotations.from_dict(_annotations)

        _delay = d.pop("delay", UNSET)
        delay: Union[Unset, WorkflowDelay]
        if isinstance(_delay, Unset):
            delay = UNSET
        else:
            delay = WorkflowDelay.from_dict(_delay)

        folder = d.pop("folder", UNSET)

        shortform = d.pop("shortform", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, CreateWorkflowPayloadState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CreateWorkflowPayloadState(_state)

        create_workflow_payload = cls(
            condition_groups=condition_groups,
            continue_on_step_error=continue_on_step_error,
            expressions=expressions,
            include_private_incidents=include_private_incidents,
            name=name,
            once_for=once_for,
            runs_on_incident_modes=runs_on_incident_modes,
            runs_on_incidents=runs_on_incidents,
            steps=steps,
            trigger=trigger,
            annotations=annotations,
            delay=delay,
            folder=folder,
            shortform=shortform,
            state=state,
        )

        create_workflow_payload.additional_properties = d
        return create_workflow_payload

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
