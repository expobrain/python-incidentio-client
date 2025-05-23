from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_public_incident_incident_created_v2_response_body_event_type import (
    WebhooksPublicIncidentIncidentCreatedV2ResponseBodyEventType,
)

if TYPE_CHECKING:
    from ..models.webhook_incident_v2 import WebhookIncidentV2


T = TypeVar("T", bound="WebhooksPublicIncidentIncidentCreatedV2ResponseBody")


@_attrs_define
class WebhooksPublicIncidentIncidentCreatedV2ResponseBody:
    """
    Example:
        {'event_type': 'public_incident.incident_created_v2', 'public_incident.incident_created_v2': {'call_url':
            'https://zoom.us/foo', 'created_at': '2021-08-17T13:28:57.801578Z', 'creator': {'api_key': {'id':
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
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'mode': 'standard', 'most_recent_update_message': "We're working
            on a fix, hoping to ship in the next 30 minutes", 'name': 'Our database is sad', 'permalink':
            'https://app.incident.io/incidents/123', 'postmortem_document_url': 'https://docs.google.com/my_doc_id',
            'reference': 'INC-123', 'related_incidents': ['INC-237'], 'severity': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'slack_channel_id': 'C02AW36C1M5',
            'slack_channel_name': 'inc-165-green-parrot', 'slack_team_id': 'T02A1FSLE8J', 'summary': "Our database is really
            really sad, and we don't know why yet.", 'updated_at': '2021-08-17T13:28:57.801578Z', 'visibility': 'public',
            'workload_minutes_late': 40.7, 'workload_minutes_sleeping': 0, 'workload_minutes_total': 60.7,
            'workload_minutes_working': 20}}

    Attributes:
        event_type (WebhooksPublicIncidentIncidentCreatedV2ResponseBodyEventType): What type of event is this webhook
            for? Example: public_incident.incident_created_v2.
        public_incident_incident_created_v2 (WebhookIncidentV2):  Example: {'call_url': 'https://zoom.us/foo',
            'created_at': '2021-08-17T13:28:57.801578Z', 'creator': {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
            Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}}, 'custom_field_entries': [{'custom_field':
            {'description': 'Which team is impacted by this issue', 'field_type': 'single_select', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected Team', 'options': [{'custom_field_id':
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
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'mode': 'standard', 'most_recent_update_message': "We're working
            on a fix, hoping to ship in the next 30 minutes", 'name': 'Our database is sad', 'permalink':
            'https://app.incident.io/incidents/123', 'postmortem_document_url': 'https://docs.google.com/my_doc_id',
            'reference': 'INC-123', 'related_incidents': ['INC-237'], 'severity': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'slack_channel_id': 'C02AW36C1M5',
            'slack_channel_name': 'inc-165-green-parrot', 'slack_team_id': 'T02A1FSLE8J', 'summary': "Our database is really
            really sad, and we don't know why yet.", 'updated_at': '2021-08-17T13:28:57.801578Z', 'visibility': 'public',
            'workload_minutes_late': 40.7, 'workload_minutes_sleeping': 0, 'workload_minutes_total': 60.7,
            'workload_minutes_working': 20}.
    """

    event_type: WebhooksPublicIncidentIncidentCreatedV2ResponseBodyEventType
    public_incident_incident_created_v2: "WebhookIncidentV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type.value

        public_incident_incident_created_v2 = self.public_incident_incident_created_v2.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "public_incident.incident_created_v2": public_incident_incident_created_v2,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_incident_v2 import WebhookIncidentV2

        d = src_dict.copy()
        event_type = WebhooksPublicIncidentIncidentCreatedV2ResponseBodyEventType(
            d.pop("event_type")
        )

        public_incident_incident_created_v2 = WebhookIncidentV2.from_dict(
            d.pop("public_incident.incident_created_v2")
        )

        webhooks_public_incident_incident_created_v2_response_body = cls(
            event_type=event_type,
            public_incident_incident_created_v2=public_incident_incident_created_v2,
        )

        webhooks_public_incident_incident_created_v2_response_body.additional_properties = d
        return webhooks_public_incident_incident_created_v2_response_body

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
