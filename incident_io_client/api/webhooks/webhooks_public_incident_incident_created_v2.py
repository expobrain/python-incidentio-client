from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhooks_public_incident_incident_created_v2_response_body import (
    WebhooksPublicIncidentIncidentCreatedV2ResponseBody,
)
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/x-webhooks/public_incident.incident_created_v2",
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[WebhooksPublicIncidentIncidentCreatedV2ResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WebhooksPublicIncidentIncidentCreatedV2ResponseBody.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[WebhooksPublicIncidentIncidentCreatedV2ResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[WebhooksPublicIncidentIncidentCreatedV2ResponseBody]:
    """PublicIncidentIncidentCreatedV2 Webhooks

     This webhook is emitted whenever a new incident is created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksPublicIncidentIncidentCreatedV2ResponseBody]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WebhooksPublicIncidentIncidentCreatedV2ResponseBody]:
    """PublicIncidentIncidentCreatedV2 Webhooks

     This webhook is emitted whenever a new incident is created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksPublicIncidentIncidentCreatedV2ResponseBody
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[WebhooksPublicIncidentIncidentCreatedV2ResponseBody]:
    """PublicIncidentIncidentCreatedV2 Webhooks

     This webhook is emitted whenever a new incident is created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksPublicIncidentIncidentCreatedV2ResponseBody]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WebhooksPublicIncidentIncidentCreatedV2ResponseBody]:
    """PublicIncidentIncidentCreatedV2 Webhooks

     This webhook is emitted whenever a new incident is created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksPublicIncidentIncidentCreatedV2ResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
