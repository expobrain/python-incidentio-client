from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhooks_private_incident_membership_granted_v1_response_body import (
    WebhooksPrivateIncidentMembershipGrantedV1ResponseBody,
)
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/x-webhooks/private_incident.membership_granted_v1",
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[WebhooksPrivateIncidentMembershipGrantedV1ResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WebhooksPrivateIncidentMembershipGrantedV1ResponseBody.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[WebhooksPrivateIncidentMembershipGrantedV1ResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[WebhooksPrivateIncidentMembershipGrantedV1ResponseBody]:
    """PrivateIncidentMembershipGrantedV1 Webhooks

     This webhook is emitted whenever a user is given access to a private incident.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksPrivateIncidentMembershipGrantedV1ResponseBody]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WebhooksPrivateIncidentMembershipGrantedV1ResponseBody]:
    """PrivateIncidentMembershipGrantedV1 Webhooks

     This webhook is emitted whenever a user is given access to a private incident.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksPrivateIncidentMembershipGrantedV1ResponseBody
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[WebhooksPrivateIncidentMembershipGrantedV1ResponseBody]:
    """PrivateIncidentMembershipGrantedV1 Webhooks

     This webhook is emitted whenever a user is given access to a private incident.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksPrivateIncidentMembershipGrantedV1ResponseBody]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WebhooksPrivateIncidentMembershipGrantedV1ResponseBody]:
    """PrivateIncidentMembershipGrantedV1 Webhooks

     This webhook is emitted whenever a user is given access to a private incident.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksPrivateIncidentMembershipGrantedV1ResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
