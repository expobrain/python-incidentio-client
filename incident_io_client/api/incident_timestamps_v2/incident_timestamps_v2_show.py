from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incident_timestamps_v2_show_response_body import (
    IncidentTimestampsV2ShowResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/incident_timestamps/{id}"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncidentTimestampsV2ShowResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentTimestampsV2ShowResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentTimestampsV2ShowResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
) -> Response[IncidentTimestampsV2ShowResponseBody]:
    """Show Incident Timestamps V2

     Get a single incident timestamp.

    Args:
        id (str):

    Returns:
        Response[IncidentTimestampsV2ShowResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
) -> Optional[IncidentTimestampsV2ShowResponseBody]:
    """Show Incident Timestamps V2

     Get a single incident timestamp.

    Args:
        id (str):

    Returns:
        Response[IncidentTimestampsV2ShowResponseBody]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[IncidentTimestampsV2ShowResponseBody]:
    """Show Incident Timestamps V2

     Get a single incident timestamp.

    Args:
        id (str):

    Returns:
        Response[IncidentTimestampsV2ShowResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
) -> Optional[IncidentTimestampsV2ShowResponseBody]:
    """Show Incident Timestamps V2

     Get a single incident timestamp.

    Args:
        id (str):

    Returns:
        Response[IncidentTimestampsV2ShowResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
