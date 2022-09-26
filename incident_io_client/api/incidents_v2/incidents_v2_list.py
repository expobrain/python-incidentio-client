from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.incidents_v2_list_response_body import IncidentsV2ListResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, Any] = UNSET,
) -> Dict[str, Any]:
    url = f"{client.base_url}/api/public/v2/incidents"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page_size"] = page_size

    params["after"] = after

    params["status"] = status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncidentsV2ListResponseBody]:
    if response.status_code == 200:
        response_200 = IncidentsV2ListResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentsV2ListResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, Any] = UNSET,
) -> Response[IncidentsV2ListResponseBody]:
    """List Incidents V2

     List all incidents for an organisation.

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        status (Union[Unset, None, Any]):

    Returns:
        Response[IncidentsV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        after=after,
        status=status,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, Any] = UNSET,
) -> Optional[IncidentsV2ListResponseBody]:
    """List Incidents V2

     List all incidents for an organisation.

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        status (Union[Unset, None, Any]):

    Returns:
        Response[IncidentsV2ListResponseBody]
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, Any] = UNSET,
) -> Response[IncidentsV2ListResponseBody]:
    """List Incidents V2

     List all incidents for an organisation.

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        status (Union[Unset, None, Any]):

    Returns:
        Response[IncidentsV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        after=after,
        status=status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, Any] = UNSET,
) -> Optional[IncidentsV2ListResponseBody]:
    """List Incidents V2

     List all incidents for an organisation.

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        status (Union[Unset, None, Any]):

    Returns:
        Response[IncidentsV2ListResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            status=status,
        )
    ).parsed
