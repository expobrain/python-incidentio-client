from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incidents_v2_edit_request_body import IncidentsV2EditRequestBody
from ...models.incidents_v2_edit_response_body import IncidentsV2EditResponseBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: IncidentsV2EditRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/incidents/{id}/actions/edit"

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


def _parse_response(*, response: httpx.Response) -> Optional[IncidentsV2EditResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentsV2EditResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentsV2EditResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    json_body: IncidentsV2EditRequestBody,
) -> Response[IncidentsV2EditResponseBody]:
    """Edit Incidents V2

     Edit an existing incident.

    This endpoint allows you to edit the properties of an existing incident: e.g. set the severity or
    update custom fields.

    When using this endpoint, only fields that are provided will be edited (omitted fields
    will be ignored).

    Args:
        id (str):
        json_body (IncidentsV2EditRequestBody):  Example: {'incident': {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our
            database is sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'summary': "Our database is
            really really sad, and we don't know why yet."}, 'notify_incident_channel': True}.

    Returns:
        Response[IncidentsV2EditResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: IncidentsV2EditRequestBody,
) -> Optional[IncidentsV2EditResponseBody]:
    """Edit Incidents V2

     Edit an existing incident.

    This endpoint allows you to edit the properties of an existing incident: e.g. set the severity or
    update custom fields.

    When using this endpoint, only fields that are provided will be edited (omitted fields
    will be ignored).

    Args:
        id (str):
        json_body (IncidentsV2EditRequestBody):  Example: {'incident': {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our
            database is sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'summary': "Our database is
            really really sad, and we don't know why yet."}, 'notify_incident_channel': True}.

    Returns:
        Response[IncidentsV2EditResponseBody]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: IncidentsV2EditRequestBody,
) -> Response[IncidentsV2EditResponseBody]:
    """Edit Incidents V2

     Edit an existing incident.

    This endpoint allows you to edit the properties of an existing incident: e.g. set the severity or
    update custom fields.

    When using this endpoint, only fields that are provided will be edited (omitted fields
    will be ignored).

    Args:
        id (str):
        json_body (IncidentsV2EditRequestBody):  Example: {'incident': {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our
            database is sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'summary': "Our database is
            really really sad, and we don't know why yet."}, 'notify_incident_channel': True}.

    Returns:
        Response[IncidentsV2EditResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: IncidentsV2EditRequestBody,
) -> Optional[IncidentsV2EditResponseBody]:
    """Edit Incidents V2

     Edit an existing incident.

    This endpoint allows you to edit the properties of an existing incident: e.g. set the severity or
    update custom fields.

    When using this endpoint, only fields that are provided will be edited (omitted fields
    will be ignored).

    Args:
        id (str):
        json_body (IncidentsV2EditRequestBody):  Example: {'incident': {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it',
            'value_timestamp': ''}]}], 'incident_timestamp_values': [{'incident_timestamp_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'value': '2021-08-17T13:28:57.801578Z'}], 'name': 'Our
            database is sad', 'severity_id': '01FH5TZRWMNAFB0DZ23FD1TV96', 'summary': "Our database is
            really really sad, and we don't know why yet."}, 'notify_incident_channel': True}.

    Returns:
        Response[IncidentsV2EditResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
