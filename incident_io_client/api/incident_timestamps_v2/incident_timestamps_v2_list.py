from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incident_timestamps_v2_list_response_body import (
    IncidentTimestampsV2ListResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/incident_timestamps"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncidentTimestampsV2ListResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentTimestampsV2ListResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentTimestampsV2ListResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[IncidentTimestampsV2ListResponseBody]:
    """List Incident Timestamps V2

     List all incident timestamps for an organisation.

    Returns:
        Response[IncidentTimestampsV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[IncidentTimestampsV2ListResponseBody]:
    """List Incident Timestamps V2

     List all incident timestamps for an organisation.

    Returns:
        Response[IncidentTimestampsV2ListResponseBody]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[IncidentTimestampsV2ListResponseBody]:
    """List Incident Timestamps V2

     List all incident timestamps for an organisation.

    Returns:
        Response[IncidentTimestampsV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[IncidentTimestampsV2ListResponseBody]:
    """List Incident Timestamps V2

     List all incident timestamps for an organisation.

    Returns:
        Response[IncidentTimestampsV2ListResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
