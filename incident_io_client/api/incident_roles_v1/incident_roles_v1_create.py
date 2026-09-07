from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incident_roles_create_payload_v1 import IncidentRolesCreatePayloadV1
from ...models.incident_roles_create_result_v1 import IncidentRolesCreateResultV1
from ...types import Response


def _get_kwargs(
    *,
    body: IncidentRolesCreatePayloadV1,
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
) -> Optional[Union[ErrorResponse, IncidentRolesCreateResultV1]]:
    if response.status_code == 201:
        response_201 = IncidentRolesCreateResultV1.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 405:
        response_405 = ErrorResponse.from_dict(response.json())

        return response_405
    if response.status_code == 406:
        response_406 = ErrorResponse.from_dict(response.json())

        return response_406
    if response.status_code == 408:
        response_408 = ErrorResponse.from_dict(response.json())

        return response_408
    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409
    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412
    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413
    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422
    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, IncidentRolesCreateResultV1]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentRolesCreatePayloadV1,
) -> Response[Union[ErrorResponse, IncidentRolesCreateResultV1]]:
    """Create Incident Roles V1

     Create a new incident role

    Args:
        body (IncidentRolesCreatePayloadV1):  Example: {'description': 'The person currently
            coordinating the incident', 'instructions': 'Take point on the incident; Make sure people
            are clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'shortform':
            'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, IncidentRolesCreateResultV1]]
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
    body: IncidentRolesCreatePayloadV1,
) -> Optional[Union[ErrorResponse, IncidentRolesCreateResultV1]]:
    """Create Incident Roles V1

     Create a new incident role

    Args:
        body (IncidentRolesCreatePayloadV1):  Example: {'description': 'The person currently
            coordinating the incident', 'instructions': 'Take point on the incident; Make sure people
            are clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'shortform':
            'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, IncidentRolesCreateResultV1]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentRolesCreatePayloadV1,
) -> Response[Union[ErrorResponse, IncidentRolesCreateResultV1]]:
    """Create Incident Roles V1

     Create a new incident role

    Args:
        body (IncidentRolesCreatePayloadV1):  Example: {'description': 'The person currently
            coordinating the incident', 'instructions': 'Take point on the incident; Make sure people
            are clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'shortform':
            'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, IncidentRolesCreateResultV1]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentRolesCreatePayloadV1,
) -> Optional[Union[ErrorResponse, IncidentRolesCreateResultV1]]:
    """Create Incident Roles V1

     Create a new incident role

    Args:
        body (IncidentRolesCreatePayloadV1):  Example: {'description': 'The person currently
            coordinating the incident', 'instructions': 'Take point on the incident; Make sure people
            are clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'shortform':
            'lead'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, IncidentRolesCreateResultV1]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
