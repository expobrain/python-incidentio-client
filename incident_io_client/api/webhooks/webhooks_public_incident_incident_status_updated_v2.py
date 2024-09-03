from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhooks_public_incident_incident_status_updated_v2_response_body import (
    WebhooksPublicIncidentIncidentStatusUpdatedV2ResponseBody,
)
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/x-webhooks/public_incident.incident_status_updated_v2",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[WebhooksPublicIncidentIncidentStatusUpdatedV2ResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WebhooksPublicIncidentIncidentStatusUpdatedV2ResponseBody.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[WebhooksPublicIncidentIncidentStatusUpdatedV2ResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[WebhooksPublicIncidentIncidentStatusUpdatedV2ResponseBody]:
    """PublicIncidentIncidentStatusUpdatedV2 Webhooks

     This webhook is emitted whenever an incident's status changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksPublicIncidentIncidentStatusUpdatedV2ResponseBody]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WebhooksPublicIncidentIncidentStatusUpdatedV2ResponseBody]:
    """PublicIncidentIncidentStatusUpdatedV2 Webhooks

     This webhook is emitted whenever an incident's status changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksPublicIncidentIncidentStatusUpdatedV2ResponseBody
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[WebhooksPublicIncidentIncidentStatusUpdatedV2ResponseBody]:
    """PublicIncidentIncidentStatusUpdatedV2 Webhooks

     This webhook is emitted whenever an incident's status changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksPublicIncidentIncidentStatusUpdatedV2ResponseBody]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WebhooksPublicIncidentIncidentStatusUpdatedV2ResponseBody]:
    """PublicIncidentIncidentStatusUpdatedV2 Webhooks

     This webhook is emitted whenever an incident's status changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksPublicIncidentIncidentStatusUpdatedV2ResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
