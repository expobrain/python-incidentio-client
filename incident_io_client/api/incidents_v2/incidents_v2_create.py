from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_create_payload_v2 import IncidentCreatePayloadV2
from ...models.incidents_v2_create_response_body import IncidentsV2CreateResponseBody
from ...types import Response


def _get_kwargs(
    *,
    body: IncidentCreatePayloadV2,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/incidents",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentsV2CreateResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentsV2CreateResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentsV2CreateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentCreatePayloadV2,
) -> Response[IncidentsV2CreateResponseBody]:
    r"""Create Incidents V2

     Create a new incident.

    Note that if the incident mode is set to \"retrospective\" then the new incident
    will not be announced in Slack.

    Args:
        body (IncidentCreatePayloadV2):  Example: {'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'idempotency_key': 'alert-
            uuid', 'incident_role_assignments': [{'assignee': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'incident_timestamp_values': [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'value': '2021-08-17T13:28:57.801578Z'}], 'incident_type_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'standard', 'name': 'Our database is sad',
            'retrospective_incident_options': {'postmortem_document_url':
            'https://docs.google.com/my_doc_id', 'slack_channel_id': 'abc123'}, 'severity_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'slack_channel_name_override': 'inc-123-database-down',
            'slack_team_id': 'T02A1FSLE8J', 'summary': "Our database is really really sad, and we
            don't know why yet.", 'visibility': 'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentsV2CreateResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentCreatePayloadV2,
) -> Optional[IncidentsV2CreateResponseBody]:
    r"""Create Incidents V2

     Create a new incident.

    Note that if the incident mode is set to \"retrospective\" then the new incident
    will not be announced in Slack.

    Args:
        body (IncidentCreatePayloadV2):  Example: {'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'idempotency_key': 'alert-
            uuid', 'incident_role_assignments': [{'assignee': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'incident_timestamp_values': [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'value': '2021-08-17T13:28:57.801578Z'}], 'incident_type_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'standard', 'name': 'Our database is sad',
            'retrospective_incident_options': {'postmortem_document_url':
            'https://docs.google.com/my_doc_id', 'slack_channel_id': 'abc123'}, 'severity_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'slack_channel_name_override': 'inc-123-database-down',
            'slack_team_id': 'T02A1FSLE8J', 'summary': "Our database is really really sad, and we
            don't know why yet.", 'visibility': 'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentsV2CreateResponseBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentCreatePayloadV2,
) -> Response[IncidentsV2CreateResponseBody]:
    r"""Create Incidents V2

     Create a new incident.

    Note that if the incident mode is set to \"retrospective\" then the new incident
    will not be announced in Slack.

    Args:
        body (IncidentCreatePayloadV2):  Example: {'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'idempotency_key': 'alert-
            uuid', 'incident_role_assignments': [{'assignee': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'incident_timestamp_values': [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'value': '2021-08-17T13:28:57.801578Z'}], 'incident_type_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'standard', 'name': 'Our database is sad',
            'retrospective_incident_options': {'postmortem_document_url':
            'https://docs.google.com/my_doc_id', 'slack_channel_id': 'abc123'}, 'severity_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'slack_channel_name_override': 'inc-123-database-down',
            'slack_team_id': 'T02A1FSLE8J', 'summary': "Our database is really really sad, and we
            don't know why yet.", 'visibility': 'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentsV2CreateResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentCreatePayloadV2,
) -> Optional[IncidentsV2CreateResponseBody]:
    r"""Create Incidents V2

     Create a new incident.

    Note that if the incident mode is set to \"retrospective\" then the new incident
    will not be announced in Slack.

    Args:
        body (IncidentCreatePayloadV2):  Example: {'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'idempotency_key': 'alert-
            uuid', 'incident_role_assignments': [{'assignee': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'incident_timestamp_values': [{'incident_timestamp_id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'value': '2021-08-17T13:28:57.801578Z'}], 'incident_type_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'mode': 'standard', 'name': 'Our database is sad',
            'retrospective_incident_options': {'postmortem_document_url':
            'https://docs.google.com/my_doc_id', 'slack_channel_id': 'abc123'}, 'severity_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'slack_channel_name_override': 'inc-123-database-down',
            'slack_team_id': 'T02A1FSLE8J', 'summary': "Our database is really really sad, and we
            don't know why yet.", 'visibility': 'public'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentsV2CreateResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
