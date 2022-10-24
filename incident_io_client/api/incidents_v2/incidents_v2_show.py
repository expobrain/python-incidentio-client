from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incidents_v2_show_response_body import IncidentsV2ShowResponseBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/incidents/{id}"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncidentsV2ShowResponseBody]:
    if response.status_code == 200:
        response_200 = IncidentsV2ShowResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentsV2ShowResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
) -> Response[IncidentsV2ShowResponseBody]:
    """Show Incidents V2

     Get a single incident.

    Args:
        id (str):

    Returns:
        Response[IncidentsV2ShowResponseBody]
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
) -> Optional[IncidentsV2ShowResponseBody]:
    """Show Incidents V2

     Get a single incident.

    Args:
        id (str):

    Returns:
        Response[IncidentsV2ShowResponseBody]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[IncidentsV2ShowResponseBody]:
    """Show Incidents V2

     Get a single incident.

    Args:
        id (str):

    Returns:
        Response[IncidentsV2ShowResponseBody]
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
) -> Optional[IncidentsV2ShowResponseBody]:
    """Show Incidents V2

     Get a single incident.

    Args:
        id (str):

    Returns:
        Response[IncidentsV2ShowResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
