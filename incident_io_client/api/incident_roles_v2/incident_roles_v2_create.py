from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_roles_v2_create_request_body import (
    IncidentRolesV2CreateRequestBody,
)
from ...models.incident_roles_v2_create_response_body import (
    IncidentRolesV2CreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    json_body: IncidentRolesV2CreateRequestBody,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v2/incident_roles",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentRolesV2CreateResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = IncidentRolesV2CreateResponseBody.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentRolesV2CreateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentRolesV2CreateRequestBody,
) -> Response[IncidentRolesV2CreateResponseBody]:
    """Create Incident Roles V2

     Create a new incident role

    Args:
        json_body (IncidentRolesV2CreateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'shortform': 'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentRolesV2CreateResponseBody]
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
    json_body: IncidentRolesV2CreateRequestBody,
) -> Optional[IncidentRolesV2CreateResponseBody]:
    """Create Incident Roles V2

     Create a new incident role

    Args:
        json_body (IncidentRolesV2CreateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'shortform': 'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentRolesV2CreateResponseBody
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentRolesV2CreateRequestBody,
) -> Response[IncidentRolesV2CreateResponseBody]:
    """Create Incident Roles V2

     Create a new incident role

    Args:
        json_body (IncidentRolesV2CreateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'shortform': 'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentRolesV2CreateResponseBody]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentRolesV2CreateRequestBody,
) -> Optional[IncidentRolesV2CreateResponseBody]:
    """Create Incident Roles V2

     Create a new incident role

    Args:
        json_body (IncidentRolesV2CreateRequestBody):  Example: {'description': 'The person
            currently coordinating the incident', 'instructions': 'Take point on the incident; Make
            sure people are clear on responsibilities', 'name': 'Incident Lead', 'shortform': 'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentRolesV2CreateResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
