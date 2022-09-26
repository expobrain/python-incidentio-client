from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incident_roles_v1_create_request_body import (
    IncidentRolesV1CreateRequestBody,
)
from ...models.incident_roles_v1_create_response_body import (
    IncidentRolesV1CreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: IncidentRolesV1CreateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/incident_roles"

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


def _parse_response(*, response: httpx.Response) -> Optional[IncidentRolesV1CreateResponseBody]:
    if response.status_code == 201:
        response_201 = IncidentRolesV1CreateResponseBody.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentRolesV1CreateResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: IncidentRolesV1CreateRequestBody,
) -> Response[IncidentRolesV1CreateResponseBody]:
    """Create Incident Roles V1

     Create a new incident role

    Args:
        json_body (IncidentRolesV1CreateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesV1CreateResponseBody]
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
    json_body: IncidentRolesV1CreateRequestBody,
) -> Optional[IncidentRolesV1CreateResponseBody]:
    """Create Incident Roles V1

     Create a new incident role

    Args:
        json_body (IncidentRolesV1CreateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesV1CreateResponseBody]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: IncidentRolesV1CreateRequestBody,
) -> Response[IncidentRolesV1CreateResponseBody]:
    """Create Incident Roles V1

     Create a new incident role

    Args:
        json_body (IncidentRolesV1CreateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesV1CreateResponseBody]
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
    json_body: IncidentRolesV1CreateRequestBody,
) -> Optional[IncidentRolesV1CreateResponseBody]:
    """Create Incident Roles V1

     Create a new incident role

    Args:
        json_body (IncidentRolesV1CreateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesV1CreateResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
