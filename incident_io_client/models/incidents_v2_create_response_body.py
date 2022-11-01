from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.incident_v2_response_body import IncidentV2ResponseBody

T = TypeVar("T", bound="IncidentsV2CreateResponseBody")


@attr.s(auto_attribs=True)
class IncidentsV2CreateResponseBody:
    """
    Example:
        {'incident': {'call_url': 'https://zoom.us/foo', 'created_at': '2021-08-17T13:28:57.801578Z', 'creator':
            {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}}, 'custom_field_entries': [{'custom_field': {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Affected
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
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}, {'value_link': 'https://google.com/',
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
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}, {'value_link': 'https://google.com/',
            'value_numeric': '123.456', 'value_option': {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}, 'value_text': 'This is my text field, I hope
            you like it'}]}], 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'incident_role_assignments': [{'assignee': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The
            person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on
            the incident; Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'role_type': 'lead', 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The
            person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on
            the incident; Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'role_type': 'lead', 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The
            person currently coordinating the incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on
            the incident; Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'role_type': 'lead', 'shortform': 'lead', 'updated_at': '2021-08-17T13:28:57.801578Z'}}], 'incident_status':
            {'category': 'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully
            mitigated**, and we're ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name':
            'Closed', 'rank': 4, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'incident_timestamp_values': [{'timestamp':
            {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'When this incident started impacting customers.',
            'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1, 'required': 'never', 'set_on_creation':
            True, 'set_on_status_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'set_on_transition': 'enter', 'set_on_visit': 'first',
            'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post': True, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'value': {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}}, {'timestamp': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'When this incident started impacting customers.', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1, 'required': 'never', 'set_on_creation': True,
            'set_on_status_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'set_on_transition': 'enter', 'set_on_visit': 'first',
            'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post': True, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'value': {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}}, {'timestamp': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'When this incident started impacting customers.', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1, 'required': 'never', 'set_on_creation': True,
            'set_on_status_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'set_on_transition': 'enter', 'set_on_visit': 'first',
            'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post': True, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'value': {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}}, {'timestamp': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'When this incident started impacting customers.', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1, 'required': 'never', 'set_on_creation': True,
            'set_on_status_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'set_on_transition': 'enter', 'set_on_visit': 'first',
            'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post': True, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'value': {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}}], 'incident_type': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': True, 'name': 'Production Outage', 'private_incidents_only': True,
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'mode': 'standard', 'name': 'Our database is sad', 'permalink':
            'https://app.incident.io/incidents/123', 'postmortem_document_url': 'https://docs.google.com/my_doc_id',
            'reference': 'INC-123', 'severity': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': "It's not
            really that bad, everyone chill", 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'slack_channel_id': 'C02AW36C1M5', 'slack_channel_name': 'inc-165-green-parrot',
            'summary': "Our database is really really sad, and we don't know why yet.", 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'visibility': 'public'}}

    Attributes:
        incident (IncidentV2ResponseBody):  Example: {'call_url': 'https://zoom.us/foo', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'creator': {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API
            key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}}, 'custom_field_entries': [{'custom_field': {'description':
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
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}, {'value_link': 'https://google.com/',
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
            you like it'}, {'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option':
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value':
            'Product'}, 'value_text': 'This is my text field, I hope you like it'}]}], 'id': '01FDAG4SAP5TYPT98WGR2N7W91',
            'incident_role_assignments': [{'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}, 'role': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'name': 'Incident Lead', 'required': True, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'},
            'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the
            incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are
            clear on responsibilities', 'name': 'Incident Lead', 'required': True, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'},
            'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the
            incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are
            clear on responsibilities', 'name': 'Incident Lead', 'required': True, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}, {'assignee': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'},
            'role': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the
            incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are
            clear on responsibilities', 'name': 'Incident Lead', 'required': True, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}], 'incident_status': {'category': 'triage', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
            from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'incident_timestamp_values': [{'timestamp': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'When this incident started impacting customers.', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1, 'required': 'never', 'set_on_creation': True,
            'set_on_status_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'set_on_transition': 'enter', 'set_on_visit': 'first',
            'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post': True, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'value': {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}}, {'timestamp': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'When this incident started impacting customers.', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1, 'required': 'never', 'set_on_creation': True,
            'set_on_status_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'set_on_transition': 'enter', 'set_on_visit': 'first',
            'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post': True, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'value': {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}}, {'timestamp': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'When this incident started impacting customers.', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1, 'required': 'never', 'set_on_creation': True,
            'set_on_status_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'set_on_transition': 'enter', 'set_on_visit': 'first',
            'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post': True, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'value': {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}}, {'timestamp': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'When this incident started impacting customers.', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1, 'required': 'never', 'set_on_creation': True,
            'set_on_status_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'set_on_transition': 'enter', 'set_on_visit': 'first',
            'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post': True, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'value': {'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}}], 'incident_type': {'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': True, 'name': 'Production Outage', 'private_incidents_only': True,
            'updated_at': '2021-08-17T13:28:57.801578Z'}, 'mode': 'standard', 'name': 'Our database is sad', 'permalink':
            'https://app.incident.io/incidents/123', 'postmortem_document_url': 'https://docs.google.com/my_doc_id',
            'reference': 'INC-123', 'severity': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': "It's not
            really that bad, everyone chill", 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'slack_channel_id': 'C02AW36C1M5', 'slack_channel_name': 'inc-165-green-parrot',
            'summary': "Our database is really really sad, and we don't know why yet.", 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'visibility': 'public'}.
    """

    incident: IncidentV2ResponseBody
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident = self.incident.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident": incident,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        incident = IncidentV2ResponseBody.from_dict(d.pop("incident"))

        incidents_v2_create_response_body = cls(
            incident=incident,
        )

        incidents_v2_create_response_body.additional_properties = d
        return incidents_v2_create_response_body

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
