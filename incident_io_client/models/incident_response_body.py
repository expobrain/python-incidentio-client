import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.actor_response_body import ActorResponseBody
from ..models.custom_field_entry_response_body import CustomFieldEntryResponseBody
from ..models.incident_response_body_status import IncidentResponseBodyStatus
from ..models.incident_response_body_type import IncidentResponseBodyType
from ..models.incident_response_body_visibility import IncidentResponseBodyVisibility
from ..models.incident_role_assignment_response_body import (
    IncidentRoleAssignmentResponseBody,
)
from ..models.incident_timestamp_response_body import IncidentTimestampResponseBody
from ..models.severity_response_body import SeverityResponseBody
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentResponseBody")


@attr.s(auto_attribs=True)
class IncidentResponseBody:
    """
    Example:
        {'call_url': 'https://zoom.us/foo', 'created_at': '2021-08-17T13:28:57.801578Z', 'creator': {'api_key': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'viewer'}}, 'custom_field_entries': [{'custom_field': {'description': 'Which team
            is impacted by this issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected
            Team', 'options': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'sort_key': 10, 'value': 'Product'}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}, {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}]},
            'values': [{'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}, {'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope
            you like it'}, {'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}]}, {'custom_field': {'description':
            'Which team is impacted by this issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Affected Team', 'options': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}, {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}]}, 'values': [{'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}, {'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope
            you like it'}, {'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}]}], 'id': '01FDAG4SAP5TYPT98WGR2N7W91',
            'incident_role_assignments': [{'assignee': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'viewer'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently
            coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident;
            Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True, 'role_type': 'lead',
            'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer'}, 'role': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'name': 'Incident Lead', 'required': True, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
            Karlin Curtis', 'role': 'viewer'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The
            person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on
            the incident; Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'role_type': 'lead', 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer'}, 'role': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'name': 'Incident Lead', 'required': True, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}], 'name': 'Our database is sad', 'postmortem_document_url':
            'https://docs.google.com/my_doc_id', 'reference': 'INC-123', 'severity': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': "It's not really that bad, everyone chill", 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'slack_channel_id': 'C02AW36C1M5', 'slack_channel_name': 'inc-165-green-parrot', 'status': 'triage', 'summary':
            "Our database is really really sad, and we don't know why yet.", 'timestamps': [{'last_occurred_at':
            '2021-08-17T13:28:57.801578Z', 'name': 'last_activity'}, {'last_occurred_at': '2021-08-17T13:28:57.801578Z',
            'name': 'last_activity'}, {'last_occurred_at': '2021-08-17T13:28:57.801578Z', 'name': 'last_activity'},
            {'last_occurred_at': '2021-08-17T13:28:57.801578Z', 'name': 'last_activity'}], 'type': 'real', 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'visibility': 'public'}

    Attributes:
        created_at (datetime.datetime): When the incident was created Example: 2021-08-17T13:28:57.801578Z.
        creator (ActorResponseBody):  Example: {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API
            key'}, 'user': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer'}}.
        custom_field_entries (List[CustomFieldEntryResponseBody]): Custom field entries for this incident Example:
            [{'custom_field': {'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key':
            10, 'value': 'Product'}]}, 'values': [{'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope you like it'}, {'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}, {'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope
            you like it'}]}, {'custom_field': {'description': 'Which team is impacted by this issue', 'field_type':
            'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key':
            10, 'value': 'Product'}]}, 'values': [{'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope you like it'}, {'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}, {'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope
            you like it'}]}].
        id (str): Unique identifier for the incident Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        incident_role_assignments (List[IncidentRoleAssignmentResponseBody]): A list of who is assigned to each role for
            this incident Example: [{'assignee': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'viewer'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently
            coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident;
            Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True, 'role_type': 'lead',
            'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer'}, 'role': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'name': 'Incident Lead', 'required': True, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
            Karlin Curtis', 'role': 'viewer'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The
            person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on
            the incident; Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'role_type': 'lead', 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer'}, 'role': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'name': 'Incident Lead', 'required': True, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}].
        name (str): Explanation of the incident Example: Our database is sad.
        reference (str): Reference to this incident, as displayed across the product Example: INC-123.
        severity (SeverityResponseBody):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description': "It's
            not really that bad, everyone chill", 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1,
            'updated_at': '2021-08-17T13:28:57.801578Z'}.
        slack_channel_id (str): ID of the Slack channel in the organisation Slack workspace Example: C02AW36C1M5.
        status (IncidentResponseBodyStatus): Current status of the incident Example: triage.
        type (IncidentResponseBodyType): Whether the incident is real, a test, or a tutorial Example: real.
        updated_at (datetime.datetime): When the incident was last updated Example: 2021-08-17T13:28:57.801578Z.
        visibility (IncidentResponseBodyVisibility): Whether the incident is public or private Example: public.
        call_url (Union[Unset, str]): The call URL attached to this incident Example: https://zoom.us/foo.
        postmortem_document_url (Union[Unset, str]): Description of the incident Example:
            https://docs.google.com/my_doc_id.
        slack_channel_name (Union[Unset, str]): Name of the slack channel Example: inc-165-green-parrot.
        summary (Union[Unset, str]): Detailed description of the incident Example: Our database is really really sad,
            and we don't know why yet..
        timestamps (Union[Unset, List[IncidentTimestampResponseBody]]): Incident lifecycle events and when they last
            occurred Example: [{'last_occurred_at': '2021-08-17T13:28:57.801578Z', 'name': 'last_activity'},
            {'last_occurred_at': '2021-08-17T13:28:57.801578Z', 'name': 'last_activity'}].
    """

    created_at: datetime.datetime
    creator: ActorResponseBody
    custom_field_entries: List[CustomFieldEntryResponseBody]
    id: str
    incident_role_assignments: List[IncidentRoleAssignmentResponseBody]
    name: str
    reference: str
    severity: SeverityResponseBody
    slack_channel_id: str
    status: IncidentResponseBodyStatus
    type: IncidentResponseBodyType
    updated_at: datetime.datetime
    visibility: IncidentResponseBodyVisibility
    call_url: Union[Unset, str] = UNSET
    postmortem_document_url: Union[Unset, str] = UNSET
    slack_channel_name: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    timestamps: Union[Unset, List[IncidentTimestampResponseBody]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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

        name = self.name
        reference = self.reference
        severity = self.severity.to_dict()

        slack_channel_id = self.slack_channel_id
        status = self.status.value

        type = self.type.value

        updated_at = self.updated_at.isoformat()

        visibility = self.visibility.value

        call_url = self.call_url
        postmortem_document_url = self.postmortem_document_url
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
                "name": name,
                "reference": reference,
                "severity": severity,
                "slack_channel_id": slack_channel_id,
                "status": status,
                "type": type,
                "updated_at": updated_at,
                "visibility": visibility,
            }
        )
        if call_url is not UNSET:
            field_dict["call_url"] = call_url
        if postmortem_document_url is not UNSET:
            field_dict["postmortem_document_url"] = postmortem_document_url
        if slack_channel_name is not UNSET:
            field_dict["slack_channel_name"] = slack_channel_name
        if summary is not UNSET:
            field_dict["summary"] = summary
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        creator = ActorResponseBody.from_dict(d.pop("creator"))

        custom_field_entries = []
        _custom_field_entries = d.pop("custom_field_entries")
        for custom_field_entries_item_data in _custom_field_entries:
            custom_field_entries_item = CustomFieldEntryResponseBody.from_dict(
                custom_field_entries_item_data
            )

            custom_field_entries.append(custom_field_entries_item)

        id = d.pop("id")

        incident_role_assignments = []
        _incident_role_assignments = d.pop("incident_role_assignments")
        for incident_role_assignments_item_data in _incident_role_assignments:
            incident_role_assignments_item = IncidentRoleAssignmentResponseBody.from_dict(
                incident_role_assignments_item_data
            )

            incident_role_assignments.append(incident_role_assignments_item)

        name = d.pop("name")

        reference = d.pop("reference")

        severity = SeverityResponseBody.from_dict(d.pop("severity"))

        slack_channel_id = d.pop("slack_channel_id")

        status = IncidentResponseBodyStatus(d.pop("status"))

        type = IncidentResponseBodyType(d.pop("type"))

        updated_at = isoparse(d.pop("updated_at"))

        visibility = IncidentResponseBodyVisibility(d.pop("visibility"))

        call_url = d.pop("call_url", UNSET)

        postmortem_document_url = d.pop("postmortem_document_url", UNSET)

        slack_channel_name = d.pop("slack_channel_name", UNSET)

        summary = d.pop("summary", UNSET)

        timestamps = []
        _timestamps = d.pop("timestamps", UNSET)
        for timestamps_item_data in _timestamps or []:
            timestamps_item = IncidentTimestampResponseBody.from_dict(timestamps_item_data)

            timestamps.append(timestamps_item)

        incident_response_body = cls(
            created_at=created_at,
            creator=creator,
            custom_field_entries=custom_field_entries,
            id=id,
            incident_role_assignments=incident_role_assignments,
            name=name,
            reference=reference,
            severity=severity,
            slack_channel_id=slack_channel_id,
            status=status,
            type=type,
            updated_at=updated_at,
            visibility=visibility,
            call_url=call_url,
            postmortem_document_url=postmortem_document_url,
            slack_channel_name=slack_channel_name,
            summary=summary,
            timestamps=timestamps,
        )

        incident_response_body.additional_properties = d
        return incident_response_body

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
