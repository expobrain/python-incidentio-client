from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incidents_v1_create_request_body import IncidentsV1CreateRequestBody
from ...models.incidents_v1_create_response_body import IncidentsV1CreateResponseBody
from ...types import Response


def _get_kwargs(
    *,
    json_body: IncidentsV1CreateRequestBody,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v1/incidents",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentsV1CreateResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentsV1CreateResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentsV1CreateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentsV1CreateRequestBody,
) -> Response[IncidentsV1CreateResponseBody]:
    """Create Incidents V1

     Create a new incident.

    Args:
        json_body (IncidentsV1CreateRequestBody):  Example: {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'real', 'name': 'Our database is
            sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'slack_team_id': 'T02A1FSLE8J',
            'source_message_channel_id': 'C02AW36C1M5', 'source_message_timestamp':
            '1653650280.526509', 'status': 'triage', 'summary': "Our database is really really sad,
            and we don't know why yet.", 'visibility': 'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentsV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentsV1CreateRequestBody,
) -> Optional[IncidentsV1CreateResponseBody]:
    """Create Incidents V1

     Create a new incident.

    Args:
        json_body (IncidentsV1CreateRequestBody):  Example: {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'real', 'name': 'Our database is
            sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'slack_team_id': 'T02A1FSLE8J',
            'source_message_channel_id': 'C02AW36C1M5', 'source_message_timestamp':
            '1653650280.526509', 'status': 'triage', 'summary': "Our database is really really sad,
            and we don't know why yet.", 'visibility': 'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentsV1CreateResponseBody
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentsV1CreateRequestBody,
) -> Response[IncidentsV1CreateResponseBody]:
    """Create Incidents V1

     Create a new incident.

    Args:
        json_body (IncidentsV1CreateRequestBody):  Example: {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'real', 'name': 'Our database is
            sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'slack_team_id': 'T02A1FSLE8J',
            'source_message_channel_id': 'C02AW36C1M5', 'source_message_timestamp':
            '1653650280.526509', 'status': 'triage', 'summary': "Our database is really really sad,
            and we don't know why yet.", 'visibility': 'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentsV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentsV1CreateRequestBody,
) -> Optional[IncidentsV1CreateResponseBody]:
    """Create Incidents V1

     Create a new incident.

    Args:
        json_body (IncidentsV1CreateRequestBody):  Example: {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments':
            [{'assignee': {'email': 'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'slack_user_id': 'USER123'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}],
            'incident_type_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'real', 'name': 'Our database is
            sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'slack_team_id': 'T02A1FSLE8J',
            'source_message_channel_id': 'C02AW36C1M5', 'source_message_timestamp':
            '1653650280.526509', 'status': 'triage', 'summary': "Our database is really really sad,
            and we don't know why yet.", 'visibility': 'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentsV1CreateResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
