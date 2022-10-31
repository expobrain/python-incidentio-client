from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.custom_field_entry_payload_v2_request_body import (
    CustomFieldEntryPayloadV2RequestBody,
)
from ..models.incident_role_assignment_payload_v2_request_body import (
    IncidentRoleAssignmentPayloadV2RequestBody,
)
from ..models.incident_timestamp_value_payload_v2_request_body import (
    IncidentTimestampValuePayloadV2RequestBody,
)
from ..models.incidents_v2_create_request_body_mode import (
    IncidentsV2CreateRequestBodyMode,
)
from ..models.incidents_v2_create_request_body_visibility import (
    IncidentsV2CreateRequestBodyVisibility,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentsV2CreateRequestBody")


@attr.s(auto_attribs=True)
class IncidentsV2CreateRequestBody:
    """
    Example:
        {'custom_field_entries': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it', 'value_timestamp': ''}]}, {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it', 'value_timestamp': ''}, {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}]}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it', 'value_timestamp': ''}]}], 'idempotency_key': 'alert-
            uuid', 'incident_role_assignments': [{'assignee': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'},
            {'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'incident_timestamp_values': [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}, {'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}, {'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}], 'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'standard', 'name':
            'Our database is sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'source_message_channel_id': 'C02AW36C1M5',
            'source_message_timestamp': '1653650280.526509', 'summary': "Our database is really really sad, and we don't
            know why yet.", 'visibility': 'public'}

    Attributes:
        idempotency_key (str): Unique string used to de-duplicate incident create requests Example: alert-uuid.
        severity_id (str): Severity to create incident as Example: 01FH5TZRWMNAFB0DZ23FD1TV96.
        visibility (IncidentsV2CreateRequestBodyVisibility): Whether the incident should be open to anyone in your Slack
            workspace (public), or invite-only (private). For more information on Private Incidents see our [help
            centre](https://help.incident.io/en/articles/5947963-can-we-mark-incidents-as-sensitive-and-restrict-access).
            Example: public.
        custom_field_entries (Union[Unset, List[CustomFieldEntryPayloadV2RequestBody]]): Set the incident's custom
            fields to these values Example: [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it', 'value_timestamp': ''}]}, {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it', 'value_timestamp': ''}, {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}]}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it', 'value_timestamp': ''}]}, {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it', 'value_timestamp': ''}, {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}]}].
        incident_role_assignments (Union[Unset, List[IncidentRoleAssignmentPayloadV2RequestBody]]): Assign incident
            roles to these people Example: [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee': {'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}].
        incident_status_id (Union[Unset, str]): Incident status to assign to the incident Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        incident_timestamp_values (Union[Unset, List[IncidentTimestampValuePayloadV2RequestBody]]): Assign the
            incident's timestamps to these values Example: [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}, {'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}].
        incident_type_id (Union[Unset, str]): Incident type to create this incident as Example:
            01FH5TZRWMNAFB0DZ23FD1TV96.
        mode (Union[Unset, IncidentsV2CreateRequestBodyMode]): Whether the incident is real, a test, or a tutorial
            Example: standard.
        name (Union[Unset, str]): Explanation of the incident Example: Our database is sad.
        source_message_channel_id (Union[Unset, str]): Channel ID of the source message, if this incident was created
            from one Example: C02AW36C1M5.
        source_message_timestamp (Union[Unset, str]): Timestamp of the source message, if this incident was created from
            one Example: 1653650280.526509.
        summary (Union[Unset, str]): Detailed description of the incident Example: Our database is really really sad,
            and we don't know why yet..
    """

    idempotency_key: str
    severity_id: str
    visibility: IncidentsV2CreateRequestBodyVisibility
    custom_field_entries: Union[Unset, List[CustomFieldEntryPayloadV2RequestBody]] = UNSET
    incident_role_assignments: Union[
        Unset, List[IncidentRoleAssignmentPayloadV2RequestBody]
    ] = UNSET
    incident_status_id: Union[Unset, str] = UNSET
    incident_timestamp_values: Union[
        Unset, List[IncidentTimestampValuePayloadV2RequestBody]
    ] = UNSET
    incident_type_id: Union[Unset, str] = UNSET
    mode: Union[Unset, IncidentsV2CreateRequestBodyMode] = UNSET
    name: Union[Unset, str] = UNSET
    source_message_channel_id: Union[Unset, str] = UNSET
    source_message_timestamp: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        idempotency_key = self.idempotency_key
        severity_id = self.severity_id
        visibility = self.visibility.value

        custom_field_entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_field_entries, Unset):
            custom_field_entries = []
            for custom_field_entries_item_data in self.custom_field_entries:
                custom_field_entries_item = custom_field_entries_item_data.to_dict()

                custom_field_entries.append(custom_field_entries_item)

        incident_role_assignments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.incident_role_assignments, Unset):
            incident_role_assignments = []
            for incident_role_assignments_item_data in self.incident_role_assignments:
                incident_role_assignments_item = incident_role_assignments_item_data.to_dict()

                incident_role_assignments.append(incident_role_assignments_item)

        incident_status_id = self.incident_status_id
        incident_timestamp_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.incident_timestamp_values, Unset):
            incident_timestamp_values = []
            for incident_timestamp_values_item_data in self.incident_timestamp_values:
                incident_timestamp_values_item = incident_timestamp_values_item_data.to_dict()

                incident_timestamp_values.append(incident_timestamp_values_item)

        incident_type_id = self.incident_type_id
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        name = self.name
        source_message_channel_id = self.source_message_channel_id
        source_message_timestamp = self.source_message_timestamp
        summary = self.summary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idempotency_key": idempotency_key,
                "severity_id": severity_id,
                "visibility": visibility,
            }
        )
        if custom_field_entries is not UNSET:
            field_dict["custom_field_entries"] = custom_field_entries
        if incident_role_assignments is not UNSET:
            field_dict["incident_role_assignments"] = incident_role_assignments
        if incident_status_id is not UNSET:
            field_dict["incident_status_id"] = incident_status_id
        if incident_timestamp_values is not UNSET:
            field_dict["incident_timestamp_values"] = incident_timestamp_values
        if incident_type_id is not UNSET:
            field_dict["incident_type_id"] = incident_type_id
        if mode is not UNSET:
            field_dict["mode"] = mode
        if name is not UNSET:
            field_dict["name"] = name
        if source_message_channel_id is not UNSET:
            field_dict["source_message_channel_id"] = source_message_channel_id
        if source_message_timestamp is not UNSET:
            field_dict["source_message_timestamp"] = source_message_timestamp
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        idempotency_key = d.pop("idempotency_key")

        severity_id = d.pop("severity_id")

        visibility = IncidentsV2CreateRequestBodyVisibility(d.pop("visibility"))

        custom_field_entries = []
        _custom_field_entries = d.pop("custom_field_entries", UNSET)
        for custom_field_entries_item_data in _custom_field_entries or []:
            custom_field_entries_item = CustomFieldEntryPayloadV2RequestBody.from_dict(
                custom_field_entries_item_data
            )

            custom_field_entries.append(custom_field_entries_item)

        incident_role_assignments = []
        _incident_role_assignments = d.pop("incident_role_assignments", UNSET)
        for incident_role_assignments_item_data in _incident_role_assignments or []:
            incident_role_assignments_item = IncidentRoleAssignmentPayloadV2RequestBody.from_dict(
                incident_role_assignments_item_data
            )

            incident_role_assignments.append(incident_role_assignments_item)

        incident_status_id = d.pop("incident_status_id", UNSET)

        incident_timestamp_values = []
        _incident_timestamp_values = d.pop("incident_timestamp_values", UNSET)
        for incident_timestamp_values_item_data in _incident_timestamp_values or []:
            incident_timestamp_values_item = IncidentTimestampValuePayloadV2RequestBody.from_dict(
                incident_timestamp_values_item_data
            )

            incident_timestamp_values.append(incident_timestamp_values_item)

        incident_type_id = d.pop("incident_type_id", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, IncidentsV2CreateRequestBodyMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = IncidentsV2CreateRequestBodyMode(_mode)

        name = d.pop("name", UNSET)

        source_message_channel_id = d.pop("source_message_channel_id", UNSET)

        source_message_timestamp = d.pop("source_message_timestamp", UNSET)

        summary = d.pop("summary", UNSET)

        incidents_v2_create_request_body = cls(
            idempotency_key=idempotency_key,
            severity_id=severity_id,
            visibility=visibility,
            custom_field_entries=custom_field_entries,
            incident_role_assignments=incident_role_assignments,
            incident_status_id=incident_status_id,
            incident_timestamp_values=incident_timestamp_values,
            incident_type_id=incident_type_id,
            mode=mode,
            name=name,
            source_message_channel_id=source_message_channel_id,
            source_message_timestamp=source_message_timestamp,
            summary=summary,
        )

        incidents_v2_create_request_body.additional_properties = d
        return incidents_v2_create_request_body

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
