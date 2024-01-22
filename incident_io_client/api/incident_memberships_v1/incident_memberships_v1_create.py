from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_memberships_v1_create_request_body import (
    IncidentMembershipsV1CreateRequestBody,
)
from ...models.incident_memberships_v1_create_response_body import (
    IncidentMembershipsV1CreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: IncidentMembershipsV1CreateRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/incident_memberships",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentMembershipsV1CreateResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = IncidentMembershipsV1CreateResponseBody.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentMembershipsV1CreateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentMembershipsV1CreateRequestBody,
) -> Response[IncidentMembershipsV1CreateResponseBody]:
    """Create Incident Memberships V1

     Makes a user a member of a private incident

    Args:
        body (IncidentMembershipsV1CreateRequestBody):  Example: {'incident_id':
            '01ET65M7ZADYFCKD4K1AE2QNMC', 'user_id': '01FCQSP07Z74QMMYPDDGQB9FTG'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentMembershipsV1CreateResponseBody]
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
    body: IncidentMembershipsV1CreateRequestBody,
) -> Optional[IncidentMembershipsV1CreateResponseBody]:
    """Create Incident Memberships V1

     Makes a user a member of a private incident

    Args:
        body (IncidentMembershipsV1CreateRequestBody):  Example: {'incident_id':
            '01ET65M7ZADYFCKD4K1AE2QNMC', 'user_id': '01FCQSP07Z74QMMYPDDGQB9FTG'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentMembershipsV1CreateResponseBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentMembershipsV1CreateRequestBody,
) -> Response[IncidentMembershipsV1CreateResponseBody]:
    """Create Incident Memberships V1

     Makes a user a member of a private incident

    Args:
        body (IncidentMembershipsV1CreateRequestBody):  Example: {'incident_id':
            '01ET65M7ZADYFCKD4K1AE2QNMC', 'user_id': '01FCQSP07Z74QMMYPDDGQB9FTG'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentMembershipsV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentMembershipsV1CreateRequestBody,
) -> Optional[IncidentMembershipsV1CreateResponseBody]:
    """Create Incident Memberships V1

     Makes a user a member of a private incident

    Args:
        body (IncidentMembershipsV1CreateRequestBody):  Example: {'incident_id':
            '01ET65M7ZADYFCKD4K1AE2QNMC', 'user_id': '01FCQSP07Z74QMMYPDDGQB9FTG'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentMembershipsV1CreateResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
