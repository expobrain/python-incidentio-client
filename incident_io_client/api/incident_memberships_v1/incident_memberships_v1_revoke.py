from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_memberships_v1_revoke_request_body import (
    IncidentMembershipsV1RevokeRequestBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: IncidentMembershipsV1RevokeRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/incident_memberships/actions/revoke",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentMembershipsV1RevokeRequestBody,
) -> Response[Any]:
    """Revoke Incident Memberships V1

     Revoke a user's membership of a private incident

    Args:
        body (IncidentMembershipsV1RevokeRequestBody):  Example: {'incident_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'user_id': '01FCQSP07Z74QMMYPDDGQB9FTG'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentMembershipsV1RevokeRequestBody,
) -> Response[Any]:
    """Revoke Incident Memberships V1

     Revoke a user's membership of a private incident

    Args:
        body (IncidentMembershipsV1RevokeRequestBody):  Example: {'incident_id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'user_id': '01FCQSP07Z74QMMYPDDGQB9FTG'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
