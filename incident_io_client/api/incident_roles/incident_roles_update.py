from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incident_roles_update_request_body import IncidentRolesUpdateRequestBody
from ...models.incident_roles_update_response_body import (
    IncidentRolesUpdateResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: IncidentRolesUpdateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/incident_roles/{id}"

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncidentRolesUpdateResponseBody]:
    if response.status_code == 200:
        response_200 = IncidentRolesUpdateResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentRolesUpdateResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    json_body: IncidentRolesUpdateRequestBody,
) -> Response[IncidentRolesUpdateResponseBody]:
    """Update Incident Roles

     Update an existing incident role

    Args:
        id (str):
        json_body (IncidentRolesUpdateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesUpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.put(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: IncidentRolesUpdateRequestBody,
) -> Optional[IncidentRolesUpdateResponseBody]:
    """Update Incident Roles

     Update an existing incident role

    Args:
        id (str):
        json_body (IncidentRolesUpdateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesUpdateResponseBody]
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
    json_body: IncidentRolesUpdateRequestBody,
) -> Response[IncidentRolesUpdateResponseBody]:
    """Update Incident Roles

     Update an existing incident role

    Args:
        id (str):
        json_body (IncidentRolesUpdateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesUpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: IncidentRolesUpdateRequestBody,
) -> Optional[IncidentRolesUpdateResponseBody]:
    """Update Incident Roles

     Update an existing incident role

    Args:
        id (str):
        json_body (IncidentRolesUpdateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesUpdateResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
