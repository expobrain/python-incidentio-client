from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_entry_payload_v2_request_body import (
        CustomFieldEntryPayloadV2RequestBody,
    )
    from ..models.incident_role_assignment_payload_v2_request_body import (
        IncidentRoleAssignmentPayloadV2RequestBody,
    )
    from ..models.incident_timestamp_value_payload_v2_request_body import (
        IncidentTimestampValuePayloadV2RequestBody,
    )


T = TypeVar("T", bound="IncidentEditPayloadV2RequestBody")


@_attrs_define
class IncidentEditPayloadV2RequestBody:
    """
    Example:
        {'call_url': 'https://zoom.us/foo', 'custom_field_entries': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it', 'value_timestamp':
            ''}]}], 'incident_role_assignments': [{'assignee': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_timestamp_values': [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}], 'name': 'Our database is sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96',
            'summary': "Our database is really really sad, and we don't know why yet."}

    Attributes:
        call_url (Union[Unset, str]): The call URL attached to this incident Example: https://zoom.us/foo.
        custom_field_entries (Union[Unset, List['CustomFieldEntryPayloadV2RequestBody']]): Set the incident's custom
            fields to these values Example: [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it', 'value_timestamp': ''}]}].
        incident_role_assignments (Union[Unset, List['IncidentRoleAssignmentPayloadV2RequestBody']]): Assign incident
            roles to these people Example: [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}].
        incident_timestamp_values (Union[Unset, List['IncidentTimestampValuePayloadV2RequestBody']]): Assign the
            incident's timestamps to these values Example: [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'value':
            '2021-08-17T13:28:57.801578Z'}].
        name (Union[Unset, str]): Explanation of the incident Example: Our database is sad.
        severity_id (Union[Unset, str]): Severity to change incident to Example: 01FH5TZRWMNAFB0DZ23FD1TV96.
        summary (Union[Unset, str]): Detailed description of the incident Example: Our database is really really sad,
            and we don't know why yet..
    """

    call_url: Union[Unset, str] = UNSET
    custom_field_entries: Union[Unset, List["CustomFieldEntryPayloadV2RequestBody"]] = UNSET
    incident_role_assignments: Union[
        Unset, List["IncidentRoleAssignmentPayloadV2RequestBody"]
    ] = UNSET
    incident_timestamp_values: Union[
        Unset, List["IncidentTimestampValuePayloadV2RequestBody"]
    ] = UNSET
    name: Union[Unset, str] = UNSET
    severity_id: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        call_url = self.call_url
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

        incident_timestamp_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.incident_timestamp_values, Unset):
            incident_timestamp_values = []
            for incident_timestamp_values_item_data in self.incident_timestamp_values:
                incident_timestamp_values_item = incident_timestamp_values_item_data.to_dict()

                incident_timestamp_values.append(incident_timestamp_values_item)

        name = self.name
        severity_id = self.severity_id
        summary = self.summary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if call_url is not UNSET:
            field_dict["call_url"] = call_url
        if custom_field_entries is not UNSET:
            field_dict["custom_field_entries"] = custom_field_entries
        if incident_role_assignments is not UNSET:
            field_dict["incident_role_assignments"] = incident_role_assignments
        if incident_timestamp_values is not UNSET:
            field_dict["incident_timestamp_values"] = incident_timestamp_values
        if name is not UNSET:
            field_dict["name"] = name
        if severity_id is not UNSET:
            field_dict["severity_id"] = severity_id
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_entry_payload_v2_request_body import (
            CustomFieldEntryPayloadV2RequestBody,
        )
        from ..models.incident_role_assignment_payload_v2_request_body import (
            IncidentRoleAssignmentPayloadV2RequestBody,
        )
        from ..models.incident_timestamp_value_payload_v2_request_body import (
            IncidentTimestampValuePayloadV2RequestBody,
        )

        d = src_dict.copy()
        call_url = d.pop("call_url", UNSET)

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

        incident_timestamp_values = []
        _incident_timestamp_values = d.pop("incident_timestamp_values", UNSET)
        for incident_timestamp_values_item_data in _incident_timestamp_values or []:
            incident_timestamp_values_item = IncidentTimestampValuePayloadV2RequestBody.from_dict(
                incident_timestamp_values_item_data
            )

            incident_timestamp_values.append(incident_timestamp_values_item)

        name = d.pop("name", UNSET)

        severity_id = d.pop("severity_id", UNSET)

        summary = d.pop("summary", UNSET)

        incident_edit_payload_v2_request_body = cls(
            call_url=call_url,
            custom_field_entries=custom_field_entries,
            incident_role_assignments=incident_role_assignments,
            incident_timestamp_values=incident_timestamp_values,
            name=name,
            severity_id=severity_id,
            summary=summary,
        )

        incident_edit_payload_v2_request_body.additional_properties = d
        return incident_edit_payload_v2_request_body

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
