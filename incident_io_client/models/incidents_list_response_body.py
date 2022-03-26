from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.incident_response_body import IncidentResponseBody
from ..models.pagination_meta_response_body import PaginationMetaResponseBody
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentsListResponseBody")


@attr.s(auto_attribs=True)
class IncidentsListResponseBody:
    """
    Example:
        {'incidents': [{'call_url': 'https://zoom.us/foo', 'closed_at': '2021-08-17T13:28:57.801578Z', 'created_at':
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
            'updated_at': '2021-08-17T13:28:57.801578Z', 'visibility': 'public'}, {'call_url': 'https://zoom.us/foo',
            'closed_at': '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z', 'custom_field_entries':
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
            'updated_at': '2021-08-17T13:28:57.801578Z', 'visibility': 'public'}], 'pagination_meta': {'after':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25, 'total_record_count': 238}}

    Attributes:
        incidents (List[IncidentResponseBody]):  Example: [{'call_url': 'https://zoom.us/foo', 'closed_at':
            '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z', 'custom_field_entries':
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
            'updated_at': '2021-08-17T13:28:57.801578Z', 'visibility': 'public'}, {'call_url': 'https://zoom.us/foo',
            'closed_at': '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z', 'custom_field_entries':
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
            'updated_at': '2021-08-17T13:28:57.801578Z', 'visibility': 'public'}].
        pagination_meta (Union[Unset, PaginationMetaResponseBody]):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0',
            'page_size': 25, 'total_record_count': 238}.
    """

    incidents: List[IncidentResponseBody]
    pagination_meta: Union[Unset, PaginationMetaResponseBody] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incidents = []
        for incidents_item_data in self.incidents:
            incidents_item = incidents_item_data.to_dict()

            incidents.append(incidents_item)

        pagination_meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination_meta, Unset):
            pagination_meta = self.pagination_meta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incidents": incidents,
            }
        )
        if pagination_meta is not UNSET:
            field_dict["pagination_meta"] = pagination_meta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        incidents = []
        _incidents = d.pop("incidents")
        for incidents_item_data in _incidents:
            incidents_item = IncidentResponseBody.from_dict(incidents_item_data)

            incidents.append(incidents_item)

        _pagination_meta = d.pop("pagination_meta", UNSET)
        pagination_meta: Union[Unset, PaginationMetaResponseBody]
        if isinstance(_pagination_meta, Unset):
            pagination_meta = UNSET
        else:
            pagination_meta = PaginationMetaResponseBody.from_dict(_pagination_meta)

        incidents_list_response_body = cls(
            incidents=incidents,
            pagination_meta=pagination_meta,
        )

        incidents_list_response_body.additional_properties = d
        return incidents_list_response_body

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
