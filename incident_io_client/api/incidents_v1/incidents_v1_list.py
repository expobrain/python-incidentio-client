from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incidents_v1_list_response_body import IncidentsV1ListResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    status: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    json_status: Union[Unset, List[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/incidents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentsV1ListResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentsV1ListResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentsV1ListResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    status: Union[Unset, List[str]] = UNSET,
) -> Response[IncidentsV1ListResponseBody]:
    """List Incidents V1

     List all incidents for an organisation.

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):
        status (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentsV1ListResponseBody]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    status: Union[Unset, List[str]] = UNSET,
) -> Optional[IncidentsV1ListResponseBody]:
    """List Incidents V1

     List all incidents for an organisation.

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):
        status (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentsV1ListResponseBody
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    status: Union[Unset, List[str]] = UNSET,
) -> Response[IncidentsV1ListResponseBody]:
    """List Incidents V1

     List all incidents for an organisation.

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):
        status (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentsV1ListResponseBody]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    status: Union[Unset, List[str]] = UNSET,
) -> Optional[IncidentsV1ListResponseBody]:
    """List Incidents V1

     List all incidents for an organisation.

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):
        status (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentsV1ListResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            status=status,
        )
    ).parsed
