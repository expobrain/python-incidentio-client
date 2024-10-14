import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.incident_v2_mode import IncidentV2Mode
from ..models.incident_v2_visibility import IncidentV2Visibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.custom_field_entry_v2 import CustomFieldEntryV2
    from ..models.external_issue_reference_v2 import ExternalIssueReferenceV2
    from ..models.incident_duration_metric_with_value_v2 import (
        IncidentDurationMetricWithValueV2,
    )
    from ..models.incident_role_assignment_v2 import IncidentRoleAssignmentV2
    from ..models.incident_status_v2 import IncidentStatusV2
    from ..models.incident_timestamp_with_value_v2 import IncidentTimestampWithValueV2
    from ..models.incident_type_v2 import IncidentTypeV2
    from ..models.severity_v2 import SeverityV2


T = TypeVar("T", bound="IncidentV2")


@_attrs_define
class IncidentV2:
    """
    Example:
        {'call_url': 'https://zoom.us/foo', 'created_at': '2021-08-17T13:28:57.801578Z', 'creator': {'api_key': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}},
            'custom_field_entries': [{'custom_field': {'description': 'Which team is impacted by this issue', 'field_type':
            'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}]},
            'values': [{'value_catalog_entry': {'aliases': ['lawrence@incident.io', 'lawrence'], 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'},
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}]}], 'duration_metrics': [{'duration_metric': {'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Lasted'}, 'value_seconds': 1}], 'external_issue_reference':
            {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-
            write-up', 'provider': 'asana'}, 'has_debrief': False, 'id': '01FDAG4SAP5TYPT98WGR2N7W91',
            'incident_role_assignments': [{'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'name': 'Incident Lead', 'required': False, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}], 'incident_status': {'category': 'triage', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
            from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'incident_timestamp_values': [{'incident_timestamp': {'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1}, 'value': {'value':
            '2021-08-17T13:28:57.801578Z'}}], 'incident_type': {'create_in_triage': 'always', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'private_incidents_only': False,
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'mode': 'standard', 'name': 'Our database is sad', 'permalink':
            'https://app.incident.io/incidents/123', 'postmortem_document_url': 'https://docs.google.com/my_doc_id',
            'reference': 'INC-123', 'severity': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with
            **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'slack_channel_id': 'C02AW36C1M5', 'slack_channel_name': 'inc-165-green-parrot',
            'slack_team_id': 'T02A1FSLE8J', 'summary': "Our database is really really sad, and we don't know why yet.",
            'updated_at': '2021-08-17T13:28:57.801578Z', 'visibility': 'public', 'workload_minutes_late': 40.7,
            'workload_minutes_sleeping': 0, 'workload_minutes_total': 60.7, 'workload_minutes_working': 20}

    Attributes:
        created_at (datetime.datetime): When the incident was created Example: 2021-08-17T13:28:57.801578Z.
        creator (ActorV2):  Example: {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'},
            'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'viewer', 'slack_user_id': 'U02AYNF2XJM'}}.
        custom_field_entries (List['CustomFieldEntryV2']): Custom field entries for this incident Example:
            [{'custom_field': {'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}]},
            'values': [{'value_catalog_entry': {'aliases': ['lawrence@incident.io', 'lawrence'], 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'},
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}]}].
        id (str): Unique identifier for the incident Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        incident_role_assignments (List['IncidentRoleAssignmentV2']): A list of who is assigned to each role for this
            incident Example: [{'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
            Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'name': 'Incident Lead', 'required': False, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}].
        incident_status (IncidentStatusV2):  Example: {'category': 'triage', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
            from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
        mode (IncidentV2Mode): Whether the incident is real, a test, a tutorial, or importing as a retrospective
            incident Example: standard.
        name (str): Explanation of the incident Example: Our database is sad.
        reference (str): Reference to this incident, as displayed across the product Example: INC-123.
        slack_channel_id (str): ID of the Slack channel in the organisation Slack workspace. Note that the channel is
            sometimes created asynchronously, so may not be present when the incident is just created. Example: C02AW36C1M5.
        slack_team_id (str): ID of the Slack team / workspace. This is only required if you are using a Slack Enterprise
            Grid with multiple teams. Example: T02A1FSLE8J.
        updated_at (datetime.datetime): When the incident was last updated Example: 2021-08-17T13:28:57.801578Z.
        visibility (IncidentV2Visibility): Whether the incident should be open to anyone in your Slack workspace
            (public), or invite-only (private). For more information on Private Incidents see our [help
            centre](https://help.incident.io/en/articles/5947963-can-we-mark-incidents-as-sensitive-and-restrict-access).
            Example: public.
        call_url (Union[Unset, str]): The call URL attached to this incident Example: https://zoom.us/foo.
        duration_metrics (Union[Unset, List['IncidentDurationMetricWithValueV2']]): Incident duration metrics and their
            measurements for this incident Example: [{'duration_metric': {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name':
            'Lasted'}, 'value_seconds': 1}].
        external_issue_reference (Union[Unset, ExternalIssueReferenceV2]):  Example: {'issue_name': 'INC-123',
            'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-write-up', 'provider':
            'asana'}.
        has_debrief (Union[Unset, bool]): If this incident has a debrief attached
        incident_timestamp_values (Union[Unset, List['IncidentTimestampWithValueV2']]): Incident lifecycle events and
            when they occurred Example: [{'incident_timestamp': {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact
            started', 'rank': 1}, 'value': {'value': '2021-08-17T13:28:57.801578Z'}}].
        incident_type (Union[Unset, IncidentTypeV2]):  Example: {'create_in_triage': 'always', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'private_incidents_only': False,
            'updated_at': '2021-08-17T13:28:57.801578Z'}.
        permalink (Union[Unset, str]): A permanent link to the homepage for this incident Example:
            https://app.incident.io/incidents/123.
        postmortem_document_url (Union[Unset, str]): Description of the incident Example:
            https://docs.google.com/my_doc_id.
        severity (Union[Unset, SeverityV2]):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
        slack_channel_name (Union[Unset, str]): Name of the slack channel Example: inc-165-green-parrot.
        summary (Union[Unset, str]): Detailed description of the incident Example: Our database is really really sad,
            and we don't know why yet..
        workload_minutes_late (Union[Unset, float]): Amount of time spent on the incident in late hours Example: 40.7.
        workload_minutes_sleeping (Union[Unset, float]): Amount of time spent on the incident in sleeping hours
        workload_minutes_total (Union[Unset, float]): Amount of time spent on the incident in total Example: 60.7.
        workload_minutes_working (Union[Unset, float]): Amount of time spent on the incident in working hours Example:
            20.0.
    """

    created_at: datetime.datetime
    creator: "ActorV2"
    custom_field_entries: List["CustomFieldEntryV2"]
    id: str
    incident_role_assignments: List["IncidentRoleAssignmentV2"]
    incident_status: "IncidentStatusV2"
    mode: IncidentV2Mode
    name: str
    reference: str
    slack_channel_id: str
    slack_team_id: str
    updated_at: datetime.datetime
    visibility: IncidentV2Visibility
    call_url: Union[Unset, str] = UNSET
    duration_metrics: Union[Unset, List["IncidentDurationMetricWithValueV2"]] = UNSET
    external_issue_reference: Union[Unset, "ExternalIssueReferenceV2"] = UNSET
    has_debrief: Union[Unset, bool] = UNSET
    incident_timestamp_values: Union[Unset, List["IncidentTimestampWithValueV2"]] = UNSET
    incident_type: Union[Unset, "IncidentTypeV2"] = UNSET
    permalink: Union[Unset, str] = UNSET
    postmortem_document_url: Union[Unset, str] = UNSET
    severity: Union[Unset, "SeverityV2"] = UNSET
    slack_channel_name: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    workload_minutes_late: Union[Unset, float] = UNSET
    workload_minutes_sleeping: Union[Unset, float] = UNSET
    workload_minutes_total: Union[Unset, float] = UNSET
    workload_minutes_working: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        creator = self.creator.to_dict()

        custom_field_entries = []
        for custom_field_entries_item_data in self.custom_field_entries:
            custom_field_entries_item = custom_field_entries_item_data.to_dict()
            custom_field_entries.append(custom_field_entries_item)

        id = self.id

        incident_role_assignments = []
        for incident_role_assignments_item_data in self.incident_role_assignments:
            incident_role_assignments_item = incident_role_assignments_item_data.to_dict()
            incident_role_assignments.append(incident_role_assignments_item)

        incident_status = self.incident_status.to_dict()

        mode = self.mode.value

        name = self.name

        reference = self.reference

        slack_channel_id = self.slack_channel_id

        slack_team_id = self.slack_team_id

        updated_at = self.updated_at.isoformat()

        visibility = self.visibility.value

        call_url = self.call_url

        duration_metrics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.duration_metrics, Unset):
            duration_metrics = []
            for duration_metrics_item_data in self.duration_metrics:
                duration_metrics_item = duration_metrics_item_data.to_dict()
                duration_metrics.append(duration_metrics_item)

        external_issue_reference: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_issue_reference, Unset):
            external_issue_reference = self.external_issue_reference.to_dict()

        has_debrief = self.has_debrief

        incident_timestamp_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.incident_timestamp_values, Unset):
            incident_timestamp_values = []
            for incident_timestamp_values_item_data in self.incident_timestamp_values:
                incident_timestamp_values_item = incident_timestamp_values_item_data.to_dict()
                incident_timestamp_values.append(incident_timestamp_values_item)

        incident_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.incident_type, Unset):
            incident_type = self.incident_type.to_dict()

        permalink = self.permalink

        postmortem_document_url = self.postmortem_document_url

        severity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.to_dict()

        slack_channel_name = self.slack_channel_name

        summary = self.summary

        workload_minutes_late = self.workload_minutes_late

        workload_minutes_sleeping = self.workload_minutes_sleeping

        workload_minutes_total = self.workload_minutes_total

        workload_minutes_working = self.workload_minutes_working

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "creator": creator,
                "custom_field_entries": custom_field_entries,
                "id": id,
                "incident_role_assignments": incident_role_assignments,
                "incident_status": incident_status,
                "mode": mode,
                "name": name,
                "reference": reference,
                "slack_channel_id": slack_channel_id,
                "slack_team_id": slack_team_id,
                "updated_at": updated_at,
                "visibility": visibility,
            }
        )
        if call_url is not UNSET:
            field_dict["call_url"] = call_url
        if duration_metrics is not UNSET:
            field_dict["duration_metrics"] = duration_metrics
        if external_issue_reference is not UNSET:
            field_dict["external_issue_reference"] = external_issue_reference
        if has_debrief is not UNSET:
            field_dict["has_debrief"] = has_debrief
        if incident_timestamp_values is not UNSET:
            field_dict["incident_timestamp_values"] = incident_timestamp_values
        if incident_type is not UNSET:
            field_dict["incident_type"] = incident_type
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if postmortem_document_url is not UNSET:
            field_dict["postmortem_document_url"] = postmortem_document_url
        if severity is not UNSET:
            field_dict["severity"] = severity
        if slack_channel_name is not UNSET:
            field_dict["slack_channel_name"] = slack_channel_name
        if summary is not UNSET:
            field_dict["summary"] = summary
        if workload_minutes_late is not UNSET:
            field_dict["workload_minutes_late"] = workload_minutes_late
        if workload_minutes_sleeping is not UNSET:
            field_dict["workload_minutes_sleeping"] = workload_minutes_sleeping
        if workload_minutes_total is not UNSET:
            field_dict["workload_minutes_total"] = workload_minutes_total
        if workload_minutes_working is not UNSET:
            field_dict["workload_minutes_working"] = workload_minutes_working

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.actor_v2 import ActorV2
        from ..models.custom_field_entry_v2 import CustomFieldEntryV2
        from ..models.external_issue_reference_v2 import ExternalIssueReferenceV2
        from ..models.incident_duration_metric_with_value_v2 import (
            IncidentDurationMetricWithValueV2,
        )
        from ..models.incident_role_assignment_v2 import IncidentRoleAssignmentV2
        from ..models.incident_status_v2 import IncidentStatusV2
        from ..models.incident_timestamp_with_value_v2 import (
            IncidentTimestampWithValueV2,
        )
        from ..models.incident_type_v2 import IncidentTypeV2
        from ..models.severity_v2 import SeverityV2

        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        creator = ActorV2.from_dict(d.pop("creator"))

        custom_field_entries = []
        _custom_field_entries = d.pop("custom_field_entries")
        for custom_field_entries_item_data in _custom_field_entries:
            custom_field_entries_item = CustomFieldEntryV2.from_dict(
                custom_field_entries_item_data
            )

            custom_field_entries.append(custom_field_entries_item)

        id = d.pop("id")

        incident_role_assignments = []
        _incident_role_assignments = d.pop("incident_role_assignments")
        for incident_role_assignments_item_data in _incident_role_assignments:
            incident_role_assignments_item = IncidentRoleAssignmentV2.from_dict(
                incident_role_assignments_item_data
            )

            incident_role_assignments.append(incident_role_assignments_item)

        incident_status = IncidentStatusV2.from_dict(d.pop("incident_status"))

        mode = IncidentV2Mode(d.pop("mode"))

        name = d.pop("name")

        reference = d.pop("reference")

        slack_channel_id = d.pop("slack_channel_id")

        slack_team_id = d.pop("slack_team_id")

        updated_at = isoparse(d.pop("updated_at"))

        visibility = IncidentV2Visibility(d.pop("visibility"))

        call_url = d.pop("call_url", UNSET)

        duration_metrics = []
        _duration_metrics = d.pop("duration_metrics", UNSET)
        for duration_metrics_item_data in _duration_metrics or []:
            duration_metrics_item = IncidentDurationMetricWithValueV2.from_dict(
                duration_metrics_item_data
            )

            duration_metrics.append(duration_metrics_item)

        _external_issue_reference = d.pop("external_issue_reference", UNSET)
        external_issue_reference: Union[Unset, ExternalIssueReferenceV2]
        if isinstance(_external_issue_reference, Unset):
            external_issue_reference = UNSET
        else:
            external_issue_reference = ExternalIssueReferenceV2.from_dict(
                _external_issue_reference
            )

        has_debrief = d.pop("has_debrief", UNSET)

        incident_timestamp_values = []
        _incident_timestamp_values = d.pop("incident_timestamp_values", UNSET)
        for incident_timestamp_values_item_data in _incident_timestamp_values or []:
            incident_timestamp_values_item = IncidentTimestampWithValueV2.from_dict(
                incident_timestamp_values_item_data
            )

            incident_timestamp_values.append(incident_timestamp_values_item)

        _incident_type = d.pop("incident_type", UNSET)
        incident_type: Union[Unset, IncidentTypeV2]
        if isinstance(_incident_type, Unset):
            incident_type = UNSET
        else:
            incident_type = IncidentTypeV2.from_dict(_incident_type)

        permalink = d.pop("permalink", UNSET)

        postmortem_document_url = d.pop("postmortem_document_url", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, SeverityV2]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = SeverityV2.from_dict(_severity)

        slack_channel_name = d.pop("slack_channel_name", UNSET)

        summary = d.pop("summary", UNSET)

        workload_minutes_late = d.pop("workload_minutes_late", UNSET)

        workload_minutes_sleeping = d.pop("workload_minutes_sleeping", UNSET)

        workload_minutes_total = d.pop("workload_minutes_total", UNSET)

        workload_minutes_working = d.pop("workload_minutes_working", UNSET)

        incident_v2 = cls(
            created_at=created_at,
            creator=creator,
            custom_field_entries=custom_field_entries,
            id=id,
            incident_role_assignments=incident_role_assignments,
            incident_status=incident_status,
            mode=mode,
            name=name,
            reference=reference,
            slack_channel_id=slack_channel_id,
            slack_team_id=slack_team_id,
            updated_at=updated_at,
            visibility=visibility,
            call_url=call_url,
            duration_metrics=duration_metrics,
            external_issue_reference=external_issue_reference,
            has_debrief=has_debrief,
            incident_timestamp_values=incident_timestamp_values,
            incident_type=incident_type,
            permalink=permalink,
            postmortem_document_url=postmortem_document_url,
            severity=severity,
            slack_channel_name=slack_channel_name,
            summary=summary,
            workload_minutes_late=workload_minutes_late,
            workload_minutes_sleeping=workload_minutes_sleeping,
            workload_minutes_total=workload_minutes_total,
            workload_minutes_working=workload_minutes_working,
        )

        incident_v2.additional_properties = d
        return incident_v2

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
