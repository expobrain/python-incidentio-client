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
from ..models.severity_response_body import SeverityResponseBody
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentResponseBody")


@attr.s(auto_attribs=True)
class IncidentResponseBody:
    """
    Example:
        {'call_url': 'https://zoom.us/foo', 'closed_at': '2021-08-17T13:28:57.801578Z', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'custom_field_entries': [{'custom_field': {'description': 'Which team is impacted
            by this issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team',
            'options': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key':
            10, 'value': 'Product'}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'sort_key': 10, 'value': 'Product'}]}, 'values': [{'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
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
            'Product'}]}, 'values': [{'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}, {'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope
            you like it'}, {'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}]}, {'custom_field': {'description':
            'Which team is impacted by this issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Affected Team', 'options': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
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
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}]},
            'values': [{'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}, {'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope
            you like it'}, {'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}]}], 'external_id': 123, 'fixed_at':
            '2021-08-17T13:28:57.801578Z', 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'identified_at':
            '2021-08-17T13:28:57.801578Z', 'name': 'Our database is sad', 'postmortem_document_url':
            'https://docs.google.com/my_doc_id', 'reported_at': '2021-08-17T13:28:57.801578Z', 'reporter': {'api_key':
            {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'viewer'}}, 'roles': [{'assignee': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'viewer'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'The person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'instructions': 'Take point on the incident; Make sure people are clear on responsibilities', 'lead_role': True,
            'name': 'Incident Lead', 'required': True, 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}},
            {'assignee': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer'}, 'role':
            {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'lead_role': True, 'name': 'Incident Lead', 'required': True, 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
            Karlin Curtis', 'role': 'viewer'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The
            person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on
            the incident; Make sure people are clear on responsibilities', 'lead_role': True, 'name': 'Incident Lead',
            'required': True, 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}}], 'severity':
            {'created_at': '2021-08-17T13:28:57.801578Z', 'description': "It's not really that bad, everyone chill", 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'slack_channel_name': 'inc-165-green-parrot', 'status': 'investigating', 'summary': "Our database is really
            really sad, and we don't know why yet.", 'summary_updated_at': '2021-08-17T13:28:57.801578Z', 'type': 'real',
            'updated_at': '2021-08-17T13:28:57.801578Z', 'visibility': 'public'}

    Attributes:
        created_at (datetime.datetime): When the incident was created Example: 2021-08-17T13:28:57.801578Z.
        custom_field_entries (List[CustomFieldEntryResponseBody]): Custom field entries for this incident Example:
            [{'custom_field': {'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}]}, 'values': [{'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}, {'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope
            you like it'}, {'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}]}, {'custom_field': {'description':
            'Which team is impacted by this issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Affected Team', 'options': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}, {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}]},
            'values': [{'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}, {'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope
            you like it'}, {'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}]}].
        external_id (int): External identifier for the incident - often displayed with an INC- prefix Example: 123.
        id (str): Unique identifier for the incident Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        name (str): Explanation of the incident Example: Our database is sad.
        reported_at (datetime.datetime): When the incident was reported Example: 2021-08-17T13:28:57.801578Z.
        reporter (ActorResponseBody):  Example: {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API
            key'}, 'user': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer'}}.
        roles (List[IncidentRoleAssignmentResponseBody]): A list of who is assigned to each role for this incident
            Example: [{'assignee': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer'},
            'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the
            incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are
            clear on responsibilities', 'lead_role': True, 'name': 'Incident Lead', 'required': True, 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
            Karlin Curtis', 'role': 'viewer'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The
            person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on
            the incident; Make sure people are clear on responsibilities', 'lead_role': True, 'name': 'Incident Lead',
            'required': True, 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer'}, 'role': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'lead_role': True, 'name': 'Incident Lead', 'required': True, 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}].
        severity (SeverityResponseBody):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description': "It's
            not really that bad, everyone chill", 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1,
            'updated_at': '2021-08-17T13:28:57.801578Z'}.
        status (IncidentResponseBodyStatus): Current status of the incident Example: investigating.
        type (IncidentResponseBodyType): Whether the incident is real, a test, or a tutorial Example: real.
        updated_at (datetime.datetime): When the incident was last updated Example: 2021-08-17T13:28:57.801578Z.
        visibility (IncidentResponseBodyVisibility): Whether the incident is public or private Example: public.
        call_url (Union[Unset, str]): The call URL attached to this incident Example: https://zoom.us/foo.
        closed_at (Union[Unset, datetime.datetime]): When the incident was closed Example: 2021-08-17T13:28:57.801578Z.
        fixed_at (Union[Unset, datetime.datetime]): When the incident was fixed Example: 2021-08-17T13:28:57.801578Z.
        identified_at (Union[Unset, datetime.datetime]): When the incident was identified Example:
            2021-08-17T13:28:57.801578Z.
        postmortem_document_url (Union[Unset, str]): Description of the incident Example:
            https://docs.google.com/my_doc_id.
        slack_channel_name (Union[Unset, str]): Name of the slack channel Example: inc-165-green-parrot.
        summary (Union[Unset, str]): Detailed description of the incident Example: Our database is really really sad,
            and we don't know why yet..
        summary_updated_at (Union[Unset, str]): When the summary was last updated Example: 2021-08-17T13:28:57.801578Z.
    """

    created_at: datetime.datetime
    custom_field_entries: List[CustomFieldEntryResponseBody]
    external_id: int
    id: str
    name: str
    reported_at: datetime.datetime
    reporter: ActorResponseBody
    roles: List[IncidentRoleAssignmentResponseBody]
    severity: SeverityResponseBody
    status: IncidentResponseBodyStatus
    type: IncidentResponseBodyType
    updated_at: datetime.datetime
    visibility: IncidentResponseBodyVisibility
    call_url: Union[Unset, str] = UNSET
    closed_at: Union[Unset, datetime.datetime] = UNSET
    fixed_at: Union[Unset, datetime.datetime] = UNSET
    identified_at: Union[Unset, datetime.datetime] = UNSET
    postmortem_document_url: Union[Unset, str] = UNSET
    slack_channel_name: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    summary_updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        custom_field_entries = []
        for custom_field_entries_item_data in self.custom_field_entries:
            custom_field_entries_item = custom_field_entries_item_data.to_dict()

            custom_field_entries.append(custom_field_entries_item)

        external_id = self.external_id
        id = self.id
        name = self.name
        reported_at = self.reported_at.isoformat()

        reporter = self.reporter.to_dict()

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()

            roles.append(roles_item)

        severity = self.severity.to_dict()

        status = self.status.value

        type = self.type.value

        updated_at = self.updated_at.isoformat()

        visibility = self.visibility.value

        call_url = self.call_url
        closed_at: Union[Unset, str] = UNSET
        if not isinstance(self.closed_at, Unset):
            closed_at = self.closed_at.isoformat()

        fixed_at: Union[Unset, str] = UNSET
        if not isinstance(self.fixed_at, Unset):
            fixed_at = self.fixed_at.isoformat()

        identified_at: Union[Unset, str] = UNSET
        if not isinstance(self.identified_at, Unset):
            identified_at = self.identified_at.isoformat()

        postmortem_document_url = self.postmortem_document_url
        slack_channel_name = self.slack_channel_name
        summary = self.summary
        summary_updated_at = self.summary_updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "custom_field_entries": custom_field_entries,
                "external_id": external_id,
                "id": id,
                "name": name,
                "reported_at": reported_at,
                "reporter": reporter,
                "roles": roles,
                "severity": severity,
                "status": status,
                "type": type,
                "updated_at": updated_at,
                "visibility": visibility,
            }
        )
        if call_url is not UNSET:
            field_dict["call_url"] = call_url
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if fixed_at is not UNSET:
            field_dict["fixed_at"] = fixed_at
        if identified_at is not UNSET:
            field_dict["identified_at"] = identified_at
        if postmortem_document_url is not UNSET:
            field_dict["postmortem_document_url"] = postmortem_document_url
        if slack_channel_name is not UNSET:
            field_dict["slack_channel_name"] = slack_channel_name
        if summary is not UNSET:
            field_dict["summary"] = summary
        if summary_updated_at is not UNSET:
            field_dict["summary_updated_at"] = summary_updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        custom_field_entries = []
        _custom_field_entries = d.pop("custom_field_entries")
        for custom_field_entries_item_data in _custom_field_entries:
            custom_field_entries_item = CustomFieldEntryResponseBody.from_dict(
                custom_field_entries_item_data
            )

            custom_field_entries.append(custom_field_entries_item)

        external_id = d.pop("external_id")

        id = d.pop("id")

        name = d.pop("name")

        reported_at = isoparse(d.pop("reported_at"))

        reporter = ActorResponseBody.from_dict(d.pop("reporter"))

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = IncidentRoleAssignmentResponseBody.from_dict(roles_item_data)

            roles.append(roles_item)

        severity = SeverityResponseBody.from_dict(d.pop("severity"))

        status = IncidentResponseBodyStatus(d.pop("status"))

        type = IncidentResponseBodyType(d.pop("type"))

        updated_at = isoparse(d.pop("updated_at"))

        visibility = IncidentResponseBodyVisibility(d.pop("visibility"))

        call_url = d.pop("call_url", UNSET)

        _closed_at = d.pop("closed_at", UNSET)
        closed_at: Union[Unset, datetime.datetime]
        if isinstance(_closed_at, Unset):
            closed_at = UNSET
        else:
            closed_at = isoparse(_closed_at)

        _fixed_at = d.pop("fixed_at", UNSET)
        fixed_at: Union[Unset, datetime.datetime]
        if isinstance(_fixed_at, Unset):
            fixed_at = UNSET
        else:
            fixed_at = isoparse(_fixed_at)

        _identified_at = d.pop("identified_at", UNSET)
        identified_at: Union[Unset, datetime.datetime]
        if isinstance(_identified_at, Unset):
            identified_at = UNSET
        else:
            identified_at = isoparse(_identified_at)

        postmortem_document_url = d.pop("postmortem_document_url", UNSET)

        slack_channel_name = d.pop("slack_channel_name", UNSET)

        summary = d.pop("summary", UNSET)

        summary_updated_at = d.pop("summary_updated_at", UNSET)

        incident_response_body = cls(
            created_at=created_at,
            custom_field_entries=custom_field_entries,
            external_id=external_id,
            id=id,
            name=name,
            reported_at=reported_at,
            reporter=reporter,
            roles=roles,
            severity=severity,
            status=status,
            type=type,
            updated_at=updated_at,
            visibility=visibility,
            call_url=call_url,
            closed_at=closed_at,
            fixed_at=fixed_at,
            identified_at=identified_at,
            postmortem_document_url=postmortem_document_url,
            slack_channel_name=slack_channel_name,
            summary=summary,
            summary_updated_at=summary_updated_at,
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
