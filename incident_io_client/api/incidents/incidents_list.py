from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.incidents_list_response_body import IncidentsListResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/incidents"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page_size"] = page_size

    params["after"] = after

    json_status: Union[Unset, None, List[str]] = UNSET
    if not isinstance(status, Unset):
        if status is None:
            json_status = None
        else:
            json_status = status

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncidentsListResponseBody]:
    if response.status_code == 200:
        response_200 = IncidentsListResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentsListResponseBody]:
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
    status: Union[Unset, None, List[str]] = UNSET,
) -> Response[IncidentsListResponseBody]:
    """List Incidents

     List all incidents for an organisation.

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        status (Union[Unset, None, List[str]]):

    Returns:
        Response[IncidentsListResponseBody]
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
    status: Union[Unset, None, List[str]] = UNSET,
) -> Optional[IncidentsListResponseBody]:
    """List Incidents

     List all incidents for an organisation.

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        status (Union[Unset, None, List[str]]):

    Returns:
        Response[IncidentsListResponseBody]
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
    status: Union[Unset, None, List[str]] = UNSET,
) -> Response[IncidentsListResponseBody]:
    """List Incidents

     List all incidents for an organisation.

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        status (Union[Unset, None, List[str]]):

    Returns:
        Response[IncidentsListResponseBody]
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
    status: Union[Unset, None, List[str]] = UNSET,
) -> Optional[IncidentsListResponseBody]:
    """List Incidents

     List all incidents for an organisation.

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        status (Union[Unset, None, List[str]]):

    Returns:
        Response[IncidentsListResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            status=status,
        )
    ).parsed
