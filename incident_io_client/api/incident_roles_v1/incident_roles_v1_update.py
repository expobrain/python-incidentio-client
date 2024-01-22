from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
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
    body: IncidentRolesV1UpdateRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/v1/incident_roles/{id}".format(
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
) -> Optional[IncidentRolesV1UpdateResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentRolesV1UpdateResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentRolesV1UpdateResponseBody]:
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
    body: IncidentRolesV1UpdateRequestBody,
) -> Response[IncidentRolesV1UpdateResponseBody]:
    """Update Incident Roles V1

     Update an existing incident role

    Args:
        id (str):
        body (IncidentRolesV1UpdateRequestBody):  Example: {'description': 'The person currently
            coordinating the incident', 'instructions': 'Take point on the incident; Make sure people
            are clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'shortform':
            'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentRolesV1UpdateResponseBody]
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
    body: IncidentRolesV1UpdateRequestBody,
) -> Optional[IncidentRolesV1UpdateResponseBody]:
    """Update Incident Roles V1

     Update an existing incident role

    Args:
        id (str):
        body (IncidentRolesV1UpdateRequestBody):  Example: {'description': 'The person currently
            coordinating the incident', 'instructions': 'Take point on the incident; Make sure people
            are clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'shortform':
            'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentRolesV1UpdateResponseBody
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
    body: IncidentRolesV1UpdateRequestBody,
) -> Response[IncidentRolesV1UpdateResponseBody]:
    """Update Incident Roles V1

     Update an existing incident role

    Args:
        id (str):
        body (IncidentRolesV1UpdateRequestBody):  Example: {'description': 'The person currently
            coordinating the incident', 'instructions': 'Take point on the incident; Make sure people
            are clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'shortform':
            'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentRolesV1UpdateResponseBody]
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
    body: IncidentRolesV1UpdateRequestBody,
) -> Optional[IncidentRolesV1UpdateResponseBody]:
    """Update Incident Roles V1

     Update an existing incident role

    Args:
        id (str):
        body (IncidentRolesV1UpdateRequestBody):  Example: {'description': 'The person currently
            coordinating the incident', 'instructions': 'Take point on the incident; Make sure people
            are clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'shortform':
            'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentRolesV1UpdateResponseBody
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
