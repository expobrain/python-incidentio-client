from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incidents_v1_create_request_body_mode import (
    IncidentsV1CreateRequestBodyMode,
)
from ..models.incidents_v1_create_request_body_status import (
    IncidentsV1CreateRequestBodyStatus,
)
from ..models.incidents_v1_create_request_body_visibility import (
    IncidentsV1CreateRequestBodyVisibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_entry_payload_v1 import CustomFieldEntryPayloadV1
    from ..models.incident_role_assignment_payload_v1 import (
        IncidentRoleAssignmentPayloadV1,
    )


T = TypeVar("T", bound="IncidentsV1CreateRequestBody")


@_attrs_define
class IncidentsV1CreateRequestBody:
    """
    Example:
        {'custom_field_entries': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it', 'value_timestamp': ''}]}], 'idempotency_key': 'alert-
            uuid', 'incident_role_assignments': [{'assignee': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'real', 'name': 'Our database is sad', 'severity_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'slack_team_id': 'T02A1FSLE8J', 'source_message_channel_id': 'C02AW36C1M5',
            'source_message_timestamp': '1653650280.526509', 'status': 'triage', 'summary': "Our database is really really
            sad, and we don't know why yet.", 'visibility': 'public'}

    Attributes:
        idempotency_key (str): Unique string used to de-duplicate incident create requests Example: alert-uuid.
        visibility (IncidentsV1CreateRequestBodyVisibility): Whether the incident should be open to anyone in your Slack
            workspace (public), or invite-only (private). For more information on Private Incidents see our [help
            centre](https://help.incident.io/en/articles/5947963-can-we-mark-incidents-as-sensitive-and-restrict-access).
            Example: public.
        custom_field_entries (Union[Unset, List['CustomFieldEntryPayloadV1']]): Set the incident's custom fields to
            these values Example: [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it', 'value_timestamp': ''}]}].
        incident_role_assignments (Union[Unset, List['IncidentRoleAssignmentPayloadV1']]): Assign incident roles to
            these people Example: [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}].
        incident_type_id (Union[Unset, str]): Incident type to create this incident as Example:
            01FH5TZRWMNAFB0DZ23FD1TV96.
        mode (Union[Unset, IncidentsV1CreateRequestBodyMode]): Whether the incident is real or test Example: real.
        name (Union[Unset, str]): Explanation of the incident Example: Our database is sad.
        severity_id (Union[Unset, str]): Severity to create incident as Example: 01FH5TZRWMNAFB0DZ23FD1TV96.
        slack_team_id (Union[Unset, str]): ID of the Slack team / workspace. This is only required if you are using a
            Slack Enterprise Grid with multiple teams. Example: T02A1FSLE8J.
        source_message_channel_id (Union[Unset, str]): Channel ID of the source message, if this incident was created
            from one Example: C02AW36C1M5.
        source_message_timestamp (Union[Unset, str]): Timestamp of the source message, if this incident was created from
            one Example: 1653650280.526509.
        status (Union[Unset, IncidentsV1CreateRequestBodyStatus]): Current status of the incident Example: triage.
        summary (Union[Unset, str]): Detailed description of the incident Example: Our database is really really sad,
            and we don't know why yet..
    """

    idempotency_key: str
    visibility: IncidentsV1CreateRequestBodyVisibility
    custom_field_entries: Union[Unset, List["CustomFieldEntryPayloadV1"]] = UNSET
    incident_role_assignments: Union[Unset, List["IncidentRoleAssignmentPayloadV1"]] = UNSET
    incident_type_id: Union[Unset, str] = UNSET
    mode: Union[Unset, IncidentsV1CreateRequestBodyMode] = UNSET
    name: Union[Unset, str] = UNSET
    severity_id: Union[Unset, str] = UNSET
    slack_team_id: Union[Unset, str] = UNSET
    source_message_channel_id: Union[Unset, str] = UNSET
    source_message_timestamp: Union[Unset, str] = UNSET
    status: Union[Unset, IncidentsV1CreateRequestBodyStatus] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        idempotency_key = self.idempotency_key

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

        incident_type_id = self.incident_type_id

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        name = self.name

        severity_id = self.severity_id

        slack_team_id = self.slack_team_id

        source_message_channel_id = self.source_message_channel_id

        source_message_timestamp = self.source_message_timestamp

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        summary = self.summary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idempotency_key": idempotency_key,
                "visibility": visibility,
            }
        )
        if custom_field_entries is not UNSET:
            field_dict["custom_field_entries"] = custom_field_entries
        if incident_role_assignments is not UNSET:
            field_dict["incident_role_assignments"] = incident_role_assignments
        if incident_type_id is not UNSET:
            field_dict["incident_type_id"] = incident_type_id
        if mode is not UNSET:
            field_dict["mode"] = mode
        if name is not UNSET:
            field_dict["name"] = name
        if severity_id is not UNSET:
            field_dict["severity_id"] = severity_id
        if slack_team_id is not UNSET:
            field_dict["slack_team_id"] = slack_team_id
        if source_message_channel_id is not UNSET:
            field_dict["source_message_channel_id"] = source_message_channel_id
        if source_message_timestamp is not UNSET:
            field_dict["source_message_timestamp"] = source_message_timestamp
        if status is not UNSET:
            field_dict["status"] = status
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_entry_payload_v1 import CustomFieldEntryPayloadV1
        from ..models.incident_role_assignment_payload_v1 import (
            IncidentRoleAssignmentPayloadV1,
        )

        d = src_dict.copy()
        idempotency_key = d.pop("idempotency_key")

        visibility = IncidentsV1CreateRequestBodyVisibility(d.pop("visibility"))

        custom_field_entries = []
        _custom_field_entries = d.pop("custom_field_entries", UNSET)
        for custom_field_entries_item_data in _custom_field_entries or []:
            custom_field_entries_item = CustomFieldEntryPayloadV1.from_dict(
                custom_field_entries_item_data
            )

            custom_field_entries.append(custom_field_entries_item)

        incident_role_assignments = []
        _incident_role_assignments = d.pop("incident_role_assignments", UNSET)
        for incident_role_assignments_item_data in _incident_role_assignments or []:
            incident_role_assignments_item = IncidentRoleAssignmentPayloadV1.from_dict(
                incident_role_assignments_item_data
            )

            incident_role_assignments.append(incident_role_assignments_item)

        incident_type_id = d.pop("incident_type_id", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, IncidentsV1CreateRequestBodyMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = IncidentsV1CreateRequestBodyMode(_mode)

        name = d.pop("name", UNSET)

        severity_id = d.pop("severity_id", UNSET)

        slack_team_id = d.pop("slack_team_id", UNSET)

        source_message_channel_id = d.pop("source_message_channel_id", UNSET)

        source_message_timestamp = d.pop("source_message_timestamp", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, IncidentsV1CreateRequestBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IncidentsV1CreateRequestBodyStatus(_status)

        summary = d.pop("summary", UNSET)

        incidents_v1_create_request_body = cls(
            idempotency_key=idempotency_key,
            visibility=visibility,
            custom_field_entries=custom_field_entries,
            incident_role_assignments=incident_role_assignments,
            incident_type_id=incident_type_id,
            mode=mode,
            name=name,
            severity_id=severity_id,
            slack_team_id=slack_team_id,
            source_message_channel_id=source_message_channel_id,
            source_message_timestamp=source_message_timestamp,
            status=status,
            summary=summary,
        )

        incidents_v1_create_request_body.additional_properties = d
        return incidents_v1_create_request_body

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
