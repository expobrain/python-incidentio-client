from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.users_v2_list_response_body import UsersV2ListResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["page_size"] = page_size

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v2/users",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UsersV2ListResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UsersV2ListResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UsersV2ListResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
) -> Response[UsersV2ListResponseBody]:
    """List Users V2

     List users for an organisation.

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
) -> Optional[UsersV2ListResponseBody]:
    """List Users V2

     List users for an organisation.

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersV2ListResponseBody
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
) -> Response[UsersV2ListResponseBody]:
    """List Users V2

     List users for an organisation.

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
) -> Optional[UsersV2ListResponseBody]:
    """List Users V2

     List users for an organisation.

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersV2ListResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
        )
    ).parsed
