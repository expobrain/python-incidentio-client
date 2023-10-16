from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhooks_private_incident_incident_created_v2_response_body import (
    WebhooksPrivateIncidentIncidentCreatedV2ResponseBody,
)
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/x-webhooks/private_incident.incident_created_v2",
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[WebhooksPrivateIncidentIncidentCreatedV2ResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WebhooksPrivateIncidentIncidentCreatedV2ResponseBody.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[WebhooksPrivateIncidentIncidentCreatedV2ResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[WebhooksPrivateIncidentIncidentCreatedV2ResponseBody]:
    """PrivateIncidentIncidentCreatedV2 Webhooks

     This webhook is emitted whenever a new private incident is created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksPrivateIncidentIncidentCreatedV2ResponseBody]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WebhooksPrivateIncidentIncidentCreatedV2ResponseBody]:
    """PrivateIncidentIncidentCreatedV2 Webhooks

     This webhook is emitted whenever a new private incident is created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksPrivateIncidentIncidentCreatedV2ResponseBody
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[WebhooksPrivateIncidentIncidentCreatedV2ResponseBody]:
    """PrivateIncidentIncidentCreatedV2 Webhooks

     This webhook is emitted whenever a new private incident is created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksPrivateIncidentIncidentCreatedV2ResponseBody]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WebhooksPrivateIncidentIncidentCreatedV2ResponseBody]:
    """PrivateIncidentIncidentCreatedV2 Webhooks

     This webhook is emitted whenever a new private incident is created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksPrivateIncidentIncidentCreatedV2ResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
