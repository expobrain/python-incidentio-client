from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_roles_v1_create_request_body import (
    IncidentRolesV1CreateRequestBody,
)
from ...models.incident_roles_v1_create_response_body import (
    IncidentRolesV1CreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: IncidentRolesV1CreateRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/incident_roles",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentRolesV1CreateResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = IncidentRolesV1CreateResponseBody.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentRolesV1CreateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentRolesV1CreateRequestBody,
) -> Response[IncidentRolesV1CreateResponseBody]:
    """Create Incident Roles V1

     Create a new incident role

    Args:
        body (IncidentRolesV1CreateRequestBody):  Example: {'description': 'The person currently
            coordinating the incident', 'instructions': 'Take point on the incident; Make sure people
            are clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'shortform':
            'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentRolesV1CreateResponseBody]
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
    body: IncidentRolesV1CreateRequestBody,
) -> Optional[IncidentRolesV1CreateResponseBody]:
    """Create Incident Roles V1

     Create a new incident role

    Args:
        body (IncidentRolesV1CreateRequestBody):  Example: {'description': 'The person currently
            coordinating the incident', 'instructions': 'Take point on the incident; Make sure people
            are clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'shortform':
            'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentRolesV1CreateResponseBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentRolesV1CreateRequestBody,
) -> Response[IncidentRolesV1CreateResponseBody]:
    """Create Incident Roles V1

     Create a new incident role

    Args:
        body (IncidentRolesV1CreateRequestBody):  Example: {'description': 'The person currently
            coordinating the incident', 'instructions': 'Take point on the incident; Make sure people
            are clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'shortform':
            'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentRolesV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentRolesV1CreateRequestBody,
) -> Optional[IncidentRolesV1CreateResponseBody]:
    """Create Incident Roles V1

     Create a new incident role

    Args:
        body (IncidentRolesV1CreateRequestBody):  Example: {'description': 'The person currently
            coordinating the incident', 'instructions': 'Take point on the incident; Make sure people
            are clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'shortform':
            'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentRolesV1CreateResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
