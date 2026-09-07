from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.users_show_paging_provider_result_v2 import (
    UsersShowPagingProviderResultV2,
)
from ...types import Response


def _get_kwargs(
    user_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/users/{user_id}/paging_provider".format(
            user_id=user_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UsersShowPagingProviderResultV2]]:
    if response.status_code == 200:
        response_200 = UsersShowPagingProviderResultV2.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 405:
        response_405 = ErrorResponse.from_dict(response.json())

        return response_405
    if response.status_code == 406:
        response_406 = ErrorResponse.from_dict(response.json())

        return response_406
    if response.status_code == 408:
        response_408 = ErrorResponse.from_dict(response.json())

        return response_408
    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409
    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412
    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413
    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422
    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, UsersShowPagingProviderResultV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, UsersShowPagingProviderResultV2]]:
    """ShowPagingProvider Users V2

     Show the paging provider that would be used to escalate to this user. Reflects their explicit
    preference if set; otherwise resolves to the effective fallback (typically `native` for on-call seat
    users, or a linked external provider otherwise). May be omitted only when the user cannot be
    escalated to at all (no seat and no linked external user).

    Args:
        user_id (str): The ID of the user. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UsersShowPagingProviderResultV2]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, UsersShowPagingProviderResultV2]]:
    """ShowPagingProvider Users V2

     Show the paging provider that would be used to escalate to this user. Reflects their explicit
    preference if set; otherwise resolves to the effective fallback (typically `native` for on-call seat
    users, or a linked external provider otherwise). May be omitted only when the user cannot be
    escalated to at all (no seat and no linked external user).

    Args:
        user_id (str): The ID of the user. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UsersShowPagingProviderResultV2]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, UsersShowPagingProviderResultV2]]:
    """ShowPagingProvider Users V2

     Show the paging provider that would be used to escalate to this user. Reflects their explicit
    preference if set; otherwise resolves to the effective fallback (typically `native` for on-call seat
    users, or a linked external provider otherwise). May be omitted only when the user cannot be
    escalated to at all (no seat and no linked external user).

    Args:
        user_id (str): The ID of the user. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UsersShowPagingProviderResultV2]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, UsersShowPagingProviderResultV2]]:
    """ShowPagingProvider Users V2

     Show the paging provider that would be used to escalate to this user. Reflects their explicit
    preference if set; otherwise resolves to the effective fallback (typically `native` for on-call seat
    users, or a linked external provider otherwise). May be omitted only when the user cannot be
    escalated to at all (no seat and no linked external user).

    Args:
        user_id (str): The ID of the user. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UsersShowPagingProviderResultV2]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
