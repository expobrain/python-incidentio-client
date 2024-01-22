from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhooks_private_incident_action_updated_v1_response_body import (
    WebhooksPrivateIncidentActionUpdatedV1ResponseBody,
)
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/x-webhooks/private_incident.action_updated_v1",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[WebhooksPrivateIncidentActionUpdatedV1ResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WebhooksPrivateIncidentActionUpdatedV1ResponseBody.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[WebhooksPrivateIncidentActionUpdatedV1ResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[WebhooksPrivateIncidentActionUpdatedV1ResponseBody]:
    """PrivateIncidentActionUpdatedV1 Webhooks

     This webhook is emitted whenever a follow-up for a private incident is updated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksPrivateIncidentActionUpdatedV1ResponseBody]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WebhooksPrivateIncidentActionUpdatedV1ResponseBody]:
    """PrivateIncidentActionUpdatedV1 Webhooks

     This webhook is emitted whenever a follow-up for a private incident is updated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksPrivateIncidentActionUpdatedV1ResponseBody
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[WebhooksPrivateIncidentActionUpdatedV1ResponseBody]:
    """PrivateIncidentActionUpdatedV1 Webhooks

     This webhook is emitted whenever a follow-up for a private incident is updated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksPrivateIncidentActionUpdatedV1ResponseBody]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WebhooksPrivateIncidentActionUpdatedV1ResponseBody]:
    """PrivateIncidentActionUpdatedV1 Webhooks

     This webhook is emitted whenever a follow-up for a private incident is updated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksPrivateIncidentActionUpdatedV1ResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
