from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incident_roles_v1_update_request_body import (
    IncidentRolesV1UpdateRequestBody,
)
from ...models.incident_roles_v1_update_response_body import (
    IncidentRolesV1UpdateResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: IncidentRolesV1UpdateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/incident_roles/{id}"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncidentRolesV1UpdateResponseBody]:
    if response.status_code == 200:
        response_200 = IncidentRolesV1UpdateResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentRolesV1UpdateResponseBody]:
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
    json_body: IncidentRolesV1UpdateRequestBody,
) -> Response[IncidentRolesV1UpdateResponseBody]:
    """Update Incident Roles V1

     Update an existing incident role

    Args:
        id (str):
        json_body (IncidentRolesV1UpdateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesV1UpdateResponseBody]
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
    json_body: IncidentRolesV1UpdateRequestBody,
) -> Optional[IncidentRolesV1UpdateResponseBody]:
    """Update Incident Roles V1

     Update an existing incident role

    Args:
        id (str):
        json_body (IncidentRolesV1UpdateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesV1UpdateResponseBody]
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
    json_body: IncidentRolesV1UpdateRequestBody,
) -> Response[IncidentRolesV1UpdateResponseBody]:
    """Update Incident Roles V1

     Update an existing incident role

    Args:
        id (str):
        json_body (IncidentRolesV1UpdateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesV1UpdateResponseBody]
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
    json_body: IncidentRolesV1UpdateRequestBody,
) -> Optional[IncidentRolesV1UpdateResponseBody]:
    """Update Incident Roles V1

     Update an existing incident role

    Args:
        id (str):
        json_body (IncidentRolesV1UpdateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True,
            'shortform': 'lead'}.

    Returns:
        Response[IncidentRolesV1UpdateResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
