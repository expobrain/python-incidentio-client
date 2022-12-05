from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incidents_v2_create_request_body import IncidentsV2CreateRequestBody
from ...models.incidents_v2_create_response_body import IncidentsV2CreateResponseBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: IncidentsV2CreateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/incidents"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncidentsV2CreateResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentsV2CreateResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentsV2CreateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: IncidentsV2CreateRequestBody,
) -> Response[IncidentsV2CreateResponseBody]:
    """Create Incidents V2

     Create a new incident.

    Note that if the incident mode is set to \"retrospective\" then the new incident
    will not be announced in Slack.

    Args:
        json_body (IncidentsV2CreateRequestBody):  Example: {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid',
            'incident_role_assignments': [{'assignee': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'incident_timestamp_values': [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'value': '2021-08-17T13:28:57.801578Z'}], 'incident_type_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'standard', 'name': 'Our database is sad',
            'retrospective_incident_options': {'slack_channel_id': 'abc123'}, 'severity_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'summary': "Our database is really really sad, and we don't
            know why yet.", 'visibility': 'public'}.

    Returns:
        Response[IncidentsV2CreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: IncidentsV2CreateRequestBody,
) -> Optional[IncidentsV2CreateResponseBody]:
    """Create Incidents V2

     Create a new incident.

    Note that if the incident mode is set to \"retrospective\" then the new incident
    will not be announced in Slack.

    Args:
        json_body (IncidentsV2CreateRequestBody):  Example: {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid',
            'incident_role_assignments': [{'assignee': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'incident_timestamp_values': [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'value': '2021-08-17T13:28:57.801578Z'}], 'incident_type_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'standard', 'name': 'Our database is sad',
            'retrospective_incident_options': {'slack_channel_id': 'abc123'}, 'severity_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'summary': "Our database is really really sad, and we don't
            know why yet.", 'visibility': 'public'}.

    Returns:
        Response[IncidentsV2CreateResponseBody]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: IncidentsV2CreateRequestBody,
) -> Response[IncidentsV2CreateResponseBody]:
    """Create Incidents V2

     Create a new incident.

    Note that if the incident mode is set to \"retrospective\" then the new incident
    will not be announced in Slack.

    Args:
        json_body (IncidentsV2CreateRequestBody):  Example: {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid',
            'incident_role_assignments': [{'assignee': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'incident_timestamp_values': [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'value': '2021-08-17T13:28:57.801578Z'}], 'incident_type_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'standard', 'name': 'Our database is sad',
            'retrospective_incident_options': {'slack_channel_id': 'abc123'}, 'severity_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'summary': "Our database is really really sad, and we don't
            know why yet.", 'visibility': 'public'}.

    Returns:
        Response[IncidentsV2CreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: IncidentsV2CreateRequestBody,
) -> Optional[IncidentsV2CreateResponseBody]:
    """Create Incidents V2

     Create a new incident.

    Note that if the incident mode is set to \"retrospective\" then the new incident
    will not be announced in Slack.

    Args:
        json_body (IncidentsV2CreateRequestBody):  Example: {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it', 'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid',
            'incident_role_assignments': [{'assignee': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'incident_timestamp_values': [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'value': '2021-08-17T13:28:57.801578Z'}], 'incident_type_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'standard', 'name': 'Our database is sad',
            'retrospective_incident_options': {'slack_channel_id': 'abc123'}, 'severity_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'summary': "Our database is really really sad, and we don't
            know why yet.", 'visibility': 'public'}.

    Returns:
        Response[IncidentsV2CreateResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
