from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_create_payload_v2_mode import IncidentCreatePayloadV2Mode
from ..models.incident_create_payload_v2_visibility import (
    IncidentCreatePayloadV2Visibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_entry_payload_v2 import CustomFieldEntryPayloadV2
    from ..models.incident_role_assignment_payload_v2 import (
        IncidentRoleAssignmentPayloadV2,
    )
    from ..models.incident_timestamp_value_payload_v2 import (
        IncidentTimestampValuePayloadV2,
    )
    from ..models.retrospective_incident_options_v2 import (
        RetrospectiveIncidentOptionsV2,
    )


T = TypeVar("T", bound="IncidentCreatePayloadV2")


@_attrs_define
class IncidentCreatePayloadV2:
    """
    Example:
        {'custom_field_entries': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it', 'value_timestamp': ''}]}], 'id':
            '01FDAG4SAP5TYPT98WGR2N7W91', 'idempotency_key': 'alert-uuid', 'incident_role_assignments': [{'assignee':
            {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'incident_timestamp_values': [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}], 'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'standard', 'name':
            'Our database is sad', 'retrospective_incident_options': {'postmortem_document_url':
            'https://docs.google.com/my_doc_id', 'slack_channel_id': 'abc123'}, 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96',
            'slack_channel_name_override': 'inc-123-database-down', 'slack_team_id': 'T02A1FSLE8J', 'summary': "Our database
            is really really sad, and we don't know why yet.", 'visibility': 'public'}

    Attributes:
        idempotency_key (str): Unique string used to de-duplicate incident create requests Example: alert-uuid.
        visibility (IncidentCreatePayloadV2Visibility): Whether the incident should be open to anyone in your Slack
            workspace (public), or invite-only (private). For more information on Private Incidents see our [help
            centre](https://help.incident.io/en/articles/5947963-can-we-mark-incidents-as-sensitive-and-restrict-access).
            Example: public.
        custom_field_entries (Union[Unset, List['CustomFieldEntryPayloadV2']]): Set the incident's custom fields to
            these values Example: [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it', 'value_timestamp': ''}]}].
        id (Union[Unset, str]): Unique identifier for the incident Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        incident_role_assignments (Union[Unset, List['IncidentRoleAssignmentPayloadV2']]): Assign incident roles to
            these people Example: [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}].
        incident_status_id (Union[Unset, str]): Incident status to assign to the incident Example:
            01G0J1EXE7AXZ2C93K61WBPYEH.
        incident_timestamp_values (Union[Unset, List['IncidentTimestampValuePayloadV2']]): Assign the incident's
            timestamps to these values Example: [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}].
        incident_type_id (Union[Unset, str]): Incident type to create this incident as Example:
            01FH5TZRWMNAFB0DZ23FD1TV96.
        mode (Union[Unset, IncidentCreatePayloadV2Mode]): Whether the incident is real, a test, a tutorial, or importing
            as a retrospective incident Example: standard.
        name (Union[Unset, str]): Explanation of the incident Example: Our database is sad.
        retrospective_incident_options (Union[Unset, RetrospectiveIncidentOptionsV2]):  Example:
            {'postmortem_document_url': 'https://docs.google.com/my_doc_id', 'slack_channel_id': 'abc123'}.
        severity_id (Union[Unset, str]): Severity to create incident as Example: 01FH5TZRWMNAFB0DZ23FD1TV96.
        slack_channel_name_override (Union[Unset, str]): Name of the Slack channel to create for this incident Example:
            inc-123-database-down.
        slack_team_id (Union[Unset, str]): Slack Team to create the incident in Example: T02A1FSLE8J.
        summary (Union[Unset, str]): Detailed description of the incident Example: Our database is really really sad,
            and we don't know why yet..
    """

    idempotency_key: str
    visibility: IncidentCreatePayloadV2Visibility
    custom_field_entries: Union[Unset, List["CustomFieldEntryPayloadV2"]] = UNSET
    id: Union[Unset, str] = UNSET
    incident_role_assignments: Union[Unset, List["IncidentRoleAssignmentPayloadV2"]] = UNSET
    incident_status_id: Union[Unset, str] = UNSET
    incident_timestamp_values: Union[Unset, List["IncidentTimestampValuePayloadV2"]] = UNSET
    incident_type_id: Union[Unset, str] = UNSET
    mode: Union[Unset, IncidentCreatePayloadV2Mode] = UNSET
    name: Union[Unset, str] = UNSET
    retrospective_incident_options: Union[Unset, "RetrospectiveIncidentOptionsV2"] = UNSET
    severity_id: Union[Unset, str] = UNSET
    slack_channel_name_override: Union[Unset, str] = UNSET
    slack_team_id: Union[Unset, str] = UNSET
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

        id = self.id

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

        retrospective_incident_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retrospective_incident_options, Unset):
            retrospective_incident_options = self.retrospective_incident_options.to_dict()

        severity_id = self.severity_id

        slack_channel_name_override = self.slack_channel_name_override

        slack_team_id = self.slack_team_id

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
        if id is not UNSET:
            field_dict["id"] = id
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
        if retrospective_incident_options is not UNSET:
            field_dict["retrospective_incident_options"] = retrospective_incident_options
        if severity_id is not UNSET:
            field_dict["severity_id"] = severity_id
        if slack_channel_name_override is not UNSET:
            field_dict["slack_channel_name_override"] = slack_channel_name_override
        if slack_team_id is not UNSET:
            field_dict["slack_team_id"] = slack_team_id
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_entry_payload_v2 import CustomFieldEntryPayloadV2
        from ..models.incident_role_assignment_payload_v2 import (
            IncidentRoleAssignmentPayloadV2,
        )
        from ..models.incident_timestamp_value_payload_v2 import (
            IncidentTimestampValuePayloadV2,
        )
        from ..models.retrospective_incident_options_v2 import (
            RetrospectiveIncidentOptionsV2,
        )

        d = src_dict.copy()
        idempotency_key = d.pop("idempotency_key")

        visibility = IncidentCreatePayloadV2Visibility(d.pop("visibility"))

        custom_field_entries = []
        _custom_field_entries = d.pop("custom_field_entries", UNSET)
        for custom_field_entries_item_data in _custom_field_entries or []:
            custom_field_entries_item = CustomFieldEntryPayloadV2.from_dict(
                custom_field_entries_item_data
            )

            custom_field_entries.append(custom_field_entries_item)

        id = d.pop("id", UNSET)

        incident_role_assignments = []
        _incident_role_assignments = d.pop("incident_role_assignments", UNSET)
        for incident_role_assignments_item_data in _incident_role_assignments or []:
            incident_role_assignments_item = IncidentRoleAssignmentPayloadV2.from_dict(
                incident_role_assignments_item_data
            )

            incident_role_assignments.append(incident_role_assignments_item)

        incident_status_id = d.pop("incident_status_id", UNSET)

        incident_timestamp_values = []
        _incident_timestamp_values = d.pop("incident_timestamp_values", UNSET)
        for incident_timestamp_values_item_data in _incident_timestamp_values or []:
            incident_timestamp_values_item = IncidentTimestampValuePayloadV2.from_dict(
                incident_timestamp_values_item_data
            )

            incident_timestamp_values.append(incident_timestamp_values_item)

        incident_type_id = d.pop("incident_type_id", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, IncidentCreatePayloadV2Mode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = IncidentCreatePayloadV2Mode(_mode)

        name = d.pop("name", UNSET)

        _retrospective_incident_options = d.pop("retrospective_incident_options", UNSET)
        retrospective_incident_options: Union[Unset, RetrospectiveIncidentOptionsV2]
        if isinstance(_retrospective_incident_options, Unset):
            retrospective_incident_options = UNSET
        else:
            retrospective_incident_options = RetrospectiveIncidentOptionsV2.from_dict(
                _retrospective_incident_options
            )

        severity_id = d.pop("severity_id", UNSET)

        slack_channel_name_override = d.pop("slack_channel_name_override", UNSET)

        slack_team_id = d.pop("slack_team_id", UNSET)

        summary = d.pop("summary", UNSET)

        incident_create_payload_v2 = cls(
            idempotency_key=idempotency_key,
            visibility=visibility,
            custom_field_entries=custom_field_entries,
            id=id,
            incident_role_assignments=incident_role_assignments,
            incident_status_id=incident_status_id,
            incident_timestamp_values=incident_timestamp_values,
            incident_type_id=incident_type_id,
            mode=mode,
            name=name,
            retrospective_incident_options=retrospective_incident_options,
            severity_id=severity_id,
            slack_channel_name_override=slack_channel_name_override,
            slack_team_id=slack_team_id,
            summary=summary,
        )

        incident_create_payload_v2.additional_properties = d
        return incident_create_payload_v2

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
