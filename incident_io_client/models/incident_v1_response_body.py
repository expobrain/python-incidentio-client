import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.incident_v1_response_body_mode import IncidentV1ResponseBodyMode
from ..models.incident_v1_response_body_status import IncidentV1ResponseBodyStatus
from ..models.incident_v1_response_body_visibility import (
    IncidentV1ResponseBodyVisibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v1_response_body import ActorV1ResponseBody
    from ..models.custom_field_entry_v1_response_body import (
        CustomFieldEntryV1ResponseBody,
    )
    from ..models.incident_role_assignment_v1_response_body import (
        IncidentRoleAssignmentV1ResponseBody,
    )
    from ..models.incident_timestamp_v1_response_body import (
        IncidentTimestampV1ResponseBody,
    )
    from ..models.incident_type_v1_response_body import IncidentTypeV1ResponseBody
    from ..models.severity_v1_response_body import SeverityV1ResponseBody


T = TypeVar("T", bound="IncidentV1ResponseBody")


@_attrs_define
class IncidentV1ResponseBody:
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
            'value_text': 'This is my text field, I hope you like it'}]}], 'id': '01FDAG4SAP5TYPT98WGR2N7W91',
            'incident_role_assignments': [{'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'name': 'Incident Lead', 'required': False, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}], 'incident_type': {'create_in_triage': 'always', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'private_incidents_only': False,
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'mode': 'real', 'name': 'Our database is sad', 'permalink':
            'https://app.incident.io/incidents/123', 'postmortem_document_url': 'https://docs.google.com/my_doc_id',
            'reference': 'INC-123', 'severity': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with
            **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'slack_channel_id': 'C02AW36C1M5', 'slack_channel_name': 'inc-165-green-parrot',
            'slack_team_id': 'T02A1FSLE8J', 'status': 'triage', 'summary': "Our database is really really sad, and we don't
            know why yet.", 'timestamps': [{'last_occurred_at': '2021-08-17T13:28:57.801578Z', 'name': 'last_activity'}],
            'updated_at': '2021-08-17T13:28:57.801578Z', 'visibility': 'public'}

    Attributes:
        created_at (datetime.datetime): When the incident was created Example: 2021-08-17T13:28:57.801578Z.
        creator (ActorV1ResponseBody):  Example: {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API
            key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}}.
        custom_field_entries (List['CustomFieldEntryV1ResponseBody']): Custom field entries for this incident Example:
            [{'custom_field': {'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}]},
            'values': [{'value_catalog_entry': {'aliases': ['lawrence@incident.io', 'lawrence'], 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'},
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}]}].
        id (str): Unique identifier for the incident Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        incident_role_assignments (List['IncidentRoleAssignmentV1ResponseBody']): A list of who is assigned to each role
            for this incident Example: [{'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'name': 'Incident Lead', 'required': False, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}].
        mode (IncidentV1ResponseBodyMode): Whether the incident is real, a test, a tutorial, or importing as a
            retrospective incident Example: real.
        name (str): Explanation of the incident Example: Our database is sad.
        reference (str): Reference to this incident, as displayed across the product Example: INC-123.
        slack_channel_id (str): ID of the Slack channel in the organisation Slack workspace Example: C02AW36C1M5.
        slack_team_id (str): ID of the Slack team / workspace. This is only required if you are using a Slack Enterprise
            Grid with multiple teams. Example: T02A1FSLE8J.
        status (IncidentV1ResponseBodyStatus): Current status of the incident Example: triage.
        updated_at (datetime.datetime): When the incident was last updated Example: 2021-08-17T13:28:57.801578Z.
        visibility (IncidentV1ResponseBodyVisibility): Whether the incident should be open to anyone in your Slack
            workspace (public), or invite-only (private). For more information on Private Incidents see our [help
            centre](https://help.incident.io/en/articles/5947963-can-we-mark-incidents-as-sensitive-and-restrict-access).
            Example: public.
        call_url (Union[Unset, str]): The call URL attached to this incident Example: https://zoom.us/foo.
        incident_type (Union[Unset, IncidentTypeV1ResponseBody]):  Example: {'create_in_triage': 'always', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': False, 'name': 'Production Outage', 'private_incidents_only': False,
            'updated_at': '2021-08-17T13:28:57.801578Z'}.
        permalink (Union[Unset, str]): A permanent link to the homepage for this incident Example:
            https://app.incident.io/incidents/123.
        postmortem_document_url (Union[Unset, str]): Description of the incident Example:
            https://docs.google.com/my_doc_id.
        severity (Union[Unset, SeverityV1ResponseBody]):  Example: {'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1,
            'updated_at': '2021-08-17T13:28:57.801578Z'}.
        slack_channel_name (Union[Unset, str]): Name of the slack channel Example: inc-165-green-parrot.
        summary (Union[Unset, str]): Detailed description of the incident Example: Our database is really really sad,
            and we don't know why yet..
        timestamps (Union[Unset, List['IncidentTimestampV1ResponseBody']]): Incident lifecycle events and when they last
            occurred Example: [{'last_occurred_at': '2021-08-17T13:28:57.801578Z', 'name': 'last_activity'}].
    """

    created_at: datetime.datetime
    creator: "ActorV1ResponseBody"
    custom_field_entries: List["CustomFieldEntryV1ResponseBody"]
    id: str
    incident_role_assignments: List["IncidentRoleAssignmentV1ResponseBody"]
    mode: IncidentV1ResponseBodyMode
    name: str
    reference: str
    slack_channel_id: str
    slack_team_id: str
    status: IncidentV1ResponseBodyStatus
    updated_at: datetime.datetime
    visibility: IncidentV1ResponseBodyVisibility
    call_url: Union[Unset, str] = UNSET
    incident_type: Union[Unset, "IncidentTypeV1ResponseBody"] = UNSET
    permalink: Union[Unset, str] = UNSET
    postmortem_document_url: Union[Unset, str] = UNSET
    severity: Union[Unset, "SeverityV1ResponseBody"] = UNSET
    slack_channel_name: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    timestamps: Union[Unset, List["IncidentTimestampV1ResponseBody"]] = UNSET
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

        mode = self.mode.value

        name = self.name
        reference = self.reference
        slack_channel_id = self.slack_channel_id
        slack_team_id = self.slack_team_id
        status = self.status.value

        updated_at = self.updated_at.isoformat()

        visibility = self.visibility.value

        call_url = self.call_url
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
        timestamps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = []
            for timestamps_item_data in self.timestamps:
                timestamps_item = timestamps_item_data.to_dict()

                timestamps.append(timestamps_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "creator": creator,
                "custom_field_entries": custom_field_entries,
                "id": id,
                "incident_role_assignments": incident_role_assignments,
                "mode": mode,
                "name": name,
                "reference": reference,
                "slack_channel_id": slack_channel_id,
                "slack_team_id": slack_team_id,
                "status": status,
                "updated_at": updated_at,
                "visibility": visibility,
            }
        )
        if call_url is not UNSET:
            field_dict["call_url"] = call_url
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
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.actor_v1_response_body import ActorV1ResponseBody
        from ..models.custom_field_entry_v1_response_body import (
            CustomFieldEntryV1ResponseBody,
        )
        from ..models.incident_role_assignment_v1_response_body import (
            IncidentRoleAssignmentV1ResponseBody,
        )
        from ..models.incident_timestamp_v1_response_body import (
            IncidentTimestampV1ResponseBody,
        )
        from ..models.incident_type_v1_response_body import IncidentTypeV1ResponseBody
        from ..models.severity_v1_response_body import SeverityV1ResponseBody

        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        creator = ActorV1ResponseBody.from_dict(d.pop("creator"))

        custom_field_entries = []
        _custom_field_entries = d.pop("custom_field_entries")
        for custom_field_entries_item_data in _custom_field_entries:
            custom_field_entries_item = CustomFieldEntryV1ResponseBody.from_dict(
                custom_field_entries_item_data
            )

            custom_field_entries.append(custom_field_entries_item)

        id = d.pop("id")

        incident_role_assignments = []
        _incident_role_assignments = d.pop("incident_role_assignments")
        for incident_role_assignments_item_data in _incident_role_assignments:
            incident_role_assignments_item = IncidentRoleAssignmentV1ResponseBody.from_dict(
                incident_role_assignments_item_data
            )

            incident_role_assignments.append(incident_role_assignments_item)

        mode = IncidentV1ResponseBodyMode(d.pop("mode"))

        name = d.pop("name")

        reference = d.pop("reference")

        slack_channel_id = d.pop("slack_channel_id")

        slack_team_id = d.pop("slack_team_id")

        status = IncidentV1ResponseBodyStatus(d.pop("status"))

        updated_at = isoparse(d.pop("updated_at"))

        visibility = IncidentV1ResponseBodyVisibility(d.pop("visibility"))

        call_url = d.pop("call_url", UNSET)

        _incident_type = d.pop("incident_type", UNSET)
        incident_type: Union[Unset, IncidentTypeV1ResponseBody]
        if isinstance(_incident_type, Unset):
            incident_type = UNSET
        else:
            incident_type = IncidentTypeV1ResponseBody.from_dict(_incident_type)

        permalink = d.pop("permalink", UNSET)

        postmortem_document_url = d.pop("postmortem_document_url", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, SeverityV1ResponseBody]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = SeverityV1ResponseBody.from_dict(_severity)

        slack_channel_name = d.pop("slack_channel_name", UNSET)

        summary = d.pop("summary", UNSET)

        timestamps = []
        _timestamps = d.pop("timestamps", UNSET)
        for timestamps_item_data in _timestamps or []:
            timestamps_item = IncidentTimestampV1ResponseBody.from_dict(timestamps_item_data)

            timestamps.append(timestamps_item)

        incident_v1_response_body = cls(
            created_at=created_at,
            creator=creator,
            custom_field_entries=custom_field_entries,
            id=id,
            incident_role_assignments=incident_role_assignments,
            mode=mode,
            name=name,
            reference=reference,
            slack_channel_id=slack_channel_id,
            slack_team_id=slack_team_id,
            status=status,
            updated_at=updated_at,
            visibility=visibility,
            call_url=call_url,
            incident_type=incident_type,
            permalink=permalink,
            postmortem_document_url=postmortem_document_url,
            severity=severity,
            slack_channel_name=slack_channel_name,
            summary=summary,
            timestamps=timestamps,
        )

        incident_v1_response_body.additional_properties = d
        return incident_v1_response_body

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
