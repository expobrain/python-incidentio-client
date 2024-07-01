from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incidents_v2_edit_request_body import IncidentsV2EditRequestBody
from ...models.incidents_v2_edit_response_body import IncidentsV2EditResponseBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: IncidentsV2EditRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/incidents/{id}/actions/edit".format(
            id=id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentsV2EditResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentsV2EditResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentsV2EditResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentsV2EditRequestBody,
) -> Response[IncidentsV2EditResponseBody]:
    """Edit Incidents V2

     Edit an existing incident.

    This endpoint allows you to edit the properties of an existing incident: e.g. set the severity or
    update custom fields.

    When using this endpoint, only fields that are provided will be edited (omitted fields
    will be ignored).

    Args:
        id (str):
        body (IncidentsV2EditRequestBody):  Example: {'incident': {'call_url':
            'https://zoom.us/foo', 'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'incident_role_assignments': [{'assignee': {'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our
            database is sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96',
            'slack_channel_name_override': 'inc-123-database-down', 'summary': "Our database is really
            really sad, and we don't know why yet."}, 'notify_incident_channel': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentsV2EditResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentsV2EditRequestBody,
) -> Optional[IncidentsV2EditResponseBody]:
    """Edit Incidents V2

     Edit an existing incident.

    This endpoint allows you to edit the properties of an existing incident: e.g. set the severity or
    update custom fields.

    When using this endpoint, only fields that are provided will be edited (omitted fields
    will be ignored).

    Args:
        id (str):
        body (IncidentsV2EditRequestBody):  Example: {'incident': {'call_url':
            'https://zoom.us/foo', 'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'incident_role_assignments': [{'assignee': {'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our
            database is sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96',
            'slack_channel_name_override': 'inc-123-database-down', 'summary': "Our database is really
            really sad, and we don't know why yet."}, 'notify_incident_channel': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentsV2EditResponseBody
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentsV2EditRequestBody,
) -> Response[IncidentsV2EditResponseBody]:
    """Edit Incidents V2

     Edit an existing incident.

    This endpoint allows you to edit the properties of an existing incident: e.g. set the severity or
    update custom fields.

    When using this endpoint, only fields that are provided will be edited (omitted fields
    will be ignored).

    Args:
        id (str):
        body (IncidentsV2EditRequestBody):  Example: {'incident': {'call_url':
            'https://zoom.us/foo', 'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'incident_role_assignments': [{'assignee': {'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our
            database is sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96',
            'slack_channel_name_override': 'inc-123-database-down', 'summary': "Our database is really
            really sad, and we don't know why yet."}, 'notify_incident_channel': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentsV2EditResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentsV2EditRequestBody,
) -> Optional[IncidentsV2EditResponseBody]:
    """Edit Incidents V2

     Edit an existing incident.

    This endpoint allows you to edit the properties of an existing incident: e.g. set the severity or
    update custom fields.

    When using this endpoint, only fields that are provided will be edited (omitted fields
    will be ignored).

    Args:
        id (str):
        body (IncidentsV2EditRequestBody):  Example: {'incident': {'call_url':
            'https://zoom.us/foo', 'custom_field_entries': [{'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'incident_role_assignments': [{'assignee': {'email':
            'bob@example.com', 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_status_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96', 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our
            database is sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96',
            'slack_channel_name_override': 'inc-123-database-down', 'summary': "Our database is really
            really sad, and we don't know why yet."}, 'notify_incident_channel': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentsV2EditResponseBody
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
