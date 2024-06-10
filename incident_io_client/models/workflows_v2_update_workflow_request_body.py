from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflows_v2_update_workflow_request_body_runs_on_incident_modes_item import (
    WorkflowsV2UpdateWorkflowRequestBodyRunsOnIncidentModesItem,
)
from ..models.workflows_v2_update_workflow_request_body_runs_on_incidents import (
    WorkflowsV2UpdateWorkflowRequestBodyRunsOnIncidents,
)
from ..models.workflows_v2_update_workflow_request_body_state import (
    WorkflowsV2UpdateWorkflowRequestBodyState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_group_payload_v2_request_body import (
        ConditionGroupPayloadV2RequestBody,
    )
    from ..models.expression_payload_v2_request_body import (
        ExpressionPayloadV2RequestBody,
    )
    from ..models.step_config_payload_request_body import StepConfigPayloadRequestBody
    from ..models.workflow_delay_request_body import WorkflowDelayRequestBody
    from ..models.workflows_v2_update_workflow_request_body_annotations import (
        WorkflowsV2UpdateWorkflowRequestBodyAnnotations,
    )


T = TypeVar("T", bound="WorkflowsV2UpdateWorkflowRequestBody")


@_attrs_define
class WorkflowsV2UpdateWorkflowRequestBody:
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
            'runs_on_incidents': 'newly_created', 'state': 'active', 'steps': [{'for_each': 'abc123', 'id': 'abc123',
            'name': 'pagerduty.escalate', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}]}]}

    Attributes:
        condition_groups (List['ConditionGroupPayloadV2RequestBody']): List of conditions to apply to the workflow
            Example: [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}].
        continue_on_step_error (bool): Whether to continue executing the workflow if a step fails Example: True.
        expressions (List['ExpressionPayloadV2RequestBody']): The expressions used in the workflow Example:
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
        include_private_incidents (bool): Whether to include private incidents Example: True.
        name (str): The human-readable name of the workflow Example: My workflow.
        once_for (List[str]): Once For strategy to apply to this workflow Example: ['incident.url'].
        runs_on_incident_modes (List[WorkflowsV2UpdateWorkflowRequestBodyRunsOnIncidentModesItem]): Which modes of
            incident this should run on (defaults to just standard incidents) Example: ['standard', 'retrospective'].
        runs_on_incidents (WorkflowsV2UpdateWorkflowRequestBodyRunsOnIncidents): Which incidents should the workflow be
            applied to? (newly_created or newly_created_and_active) Example: newly_created.
        steps (List['StepConfigPayloadRequestBody']): List of step to execute as part of the workflow Example:
            [{'for_each': 'abc123', 'id': 'abc123', 'name': 'pagerduty.escalate', 'param_bindings': [{'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}]}].
        annotations (Union[Unset, WorkflowsV2UpdateWorkflowRequestBodyAnnotations]): Annotations that track metadata
            about this resource Example: {'incident.io/terraform/version': '3.0.0'}.
        delay (Union[Unset, WorkflowDelayRequestBody]):  Example: {'conditions_apply_over_delay': False, 'for_seconds':
            60}.
        folder (Union[Unset, str]): Folder to display the workflow in Example: My folder 01.
        state (Union[Unset, WorkflowsV2UpdateWorkflowRequestBodyState]): The state of the workflow (e.g. is it draft, or
            disabled) Example: active.
    """

    condition_groups: List["ConditionGroupPayloadV2RequestBody"]
    continue_on_step_error: bool
    expressions: List["ExpressionPayloadV2RequestBody"]
    include_private_incidents: bool
    name: str
    once_for: List[str]
    runs_on_incident_modes: List[WorkflowsV2UpdateWorkflowRequestBodyRunsOnIncidentModesItem]
    runs_on_incidents: WorkflowsV2UpdateWorkflowRequestBodyRunsOnIncidents
    steps: List["StepConfigPayloadRequestBody"]
    annotations: Union[Unset, "WorkflowsV2UpdateWorkflowRequestBodyAnnotations"] = UNSET
    delay: Union[Unset, "WorkflowDelayRequestBody"] = UNSET
    folder: Union[Unset, str] = UNSET
    state: Union[Unset, WorkflowsV2UpdateWorkflowRequestBodyState] = UNSET
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

        annotations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        delay: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delay, Unset):
            delay = self.delay.to_dict()

        folder = self.folder

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
            }
        )
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if delay is not UNSET:
            field_dict["delay"] = delay
        if folder is not UNSET:
            field_dict["folder"] = folder
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.condition_group_payload_v2_request_body import (
            ConditionGroupPayloadV2RequestBody,
        )
        from ..models.expression_payload_v2_request_body import (
            ExpressionPayloadV2RequestBody,
        )
        from ..models.step_config_payload_request_body import (
            StepConfigPayloadRequestBody,
        )
        from ..models.workflow_delay_request_body import WorkflowDelayRequestBody
        from ..models.workflows_v2_update_workflow_request_body_annotations import (
            WorkflowsV2UpdateWorkflowRequestBodyAnnotations,
        )

        d = src_dict.copy()
        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV2RequestBody.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        continue_on_step_error = d.pop("continue_on_step_error")

        expressions = []
        _expressions = d.pop("expressions")
        for expressions_item_data in _expressions:
            expressions_item = ExpressionPayloadV2RequestBody.from_dict(expressions_item_data)

            expressions.append(expressions_item)

        include_private_incidents = d.pop("include_private_incidents")

        name = d.pop("name")

        once_for = cast(List[str], d.pop("once_for"))

        runs_on_incident_modes = []
        _runs_on_incident_modes = d.pop("runs_on_incident_modes")
        for runs_on_incident_modes_item_data in _runs_on_incident_modes:
            runs_on_incident_modes_item = (
                WorkflowsV2UpdateWorkflowRequestBodyRunsOnIncidentModesItem(
                    runs_on_incident_modes_item_data
                )
            )

            runs_on_incident_modes.append(runs_on_incident_modes_item)

        runs_on_incidents = WorkflowsV2UpdateWorkflowRequestBodyRunsOnIncidents(
            d.pop("runs_on_incidents")
        )

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = StepConfigPayloadRequestBody.from_dict(steps_item_data)

            steps.append(steps_item)

        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, WorkflowsV2UpdateWorkflowRequestBodyAnnotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = WorkflowsV2UpdateWorkflowRequestBodyAnnotations.from_dict(_annotations)

        _delay = d.pop("delay", UNSET)
        delay: Union[Unset, WorkflowDelayRequestBody]
        if isinstance(_delay, Unset):
            delay = UNSET
        else:
            delay = WorkflowDelayRequestBody.from_dict(_delay)

        folder = d.pop("folder", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, WorkflowsV2UpdateWorkflowRequestBodyState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = WorkflowsV2UpdateWorkflowRequestBodyState(_state)

        workflows_v2_update_workflow_request_body = cls(
            condition_groups=condition_groups,
            continue_on_step_error=continue_on_step_error,
            expressions=expressions,
            include_private_incidents=include_private_incidents,
            name=name,
            once_for=once_for,
            runs_on_incident_modes=runs_on_incident_modes,
            runs_on_incidents=runs_on_incidents,
            steps=steps,
            annotations=annotations,
            delay=delay,
            folder=folder,
            state=state,
        )

        workflows_v2_update_workflow_request_body.additional_properties = d
        return workflows_v2_update_workflow_request_body

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
