from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incident_roles_create_request_body import IncidentRolesCreateRequestBody
from ...models.incident_roles_create_response_body import (
    IncidentRolesCreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: IncidentRolesCreateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/incident_roles"

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


def _parse_response(*, response: httpx.Response) -> Optional[IncidentRolesCreateResponseBody]:
    if response.status_code == 201:
        response_201 = IncidentRolesCreateResponseBody.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentRolesCreateResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: IncidentRolesCreateRequestBody,
) -> Response[IncidentRolesCreateResponseBody]:
    """Create Incident Roles

     Create a new incident role

    Args:
        json_body (IncidentRolesCreateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesCreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: IncidentRolesCreateRequestBody,
) -> Optional[IncidentRolesCreateResponseBody]:
    """Create Incident Roles

     Create a new incident role

    Args:
        json_body (IncidentRolesCreateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesCreateResponseBody]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: IncidentRolesCreateRequestBody,
) -> Response[IncidentRolesCreateResponseBody]:
    """Create Incident Roles

     Create a new incident role

    Args:
        json_body (IncidentRolesCreateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesCreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: IncidentRolesCreateRequestBody,
) -> Optional[IncidentRolesCreateResponseBody]:
    """Create Incident Roles

     Create a new incident role

    Args:
        json_body (IncidentRolesCreateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesCreateResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
