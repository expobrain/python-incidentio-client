from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.users_list_result_v2 import UsersListResultV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    email: Union[Unset, str] = UNSET,
    slack_user_id: Union[Unset, str] = UNSET,
    include_inactive: Union[Unset, bool] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["email"] = email

    params["slack_user_id"] = slack_user_id

    params["include_inactive"] = include_inactive

    params["page_size"] = page_size

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UsersListResultV2]]:
    if response.status_code == 200:
        response_200 = UsersListResultV2.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UsersListResultV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    email: Union[Unset, str] = UNSET,
    slack_user_id: Union[Unset, str] = UNSET,
    include_inactive: Union[Unset, bool] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, UsersListResultV2]]:
    """List Users V2

     List users in your account.

    Args:
        email (Union[Unset, str]): Filter by email address Example: john.doe@incident.io.
        slack_user_id (Union[Unset, str]): Filter by Slack user ID Example: U12345678.
        include_inactive (Union[Unset, bool]): Include deactivated or not-yet-active users
            (defaults to false). Useful for resolving users who have since been offboarded. Example:
            True.
        page_size (Union[Unset, int]): Integer number of records to return Default: 25. Example:
            25.
        after (Union[Unset, str]): An record's ID. This endpoint will return a list of records
            after this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UsersListResultV2]]
    """

    kwargs = _get_kwargs(
        email=email,
        slack_user_id=slack_user_id,
        include_inactive=include_inactive,
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
    email: Union[Unset, str] = UNSET,
    slack_user_id: Union[Unset, str] = UNSET,
    include_inactive: Union[Unset, bool] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, UsersListResultV2]]:
    """List Users V2

     List users in your account.

    Args:
        email (Union[Unset, str]): Filter by email address Example: john.doe@incident.io.
        slack_user_id (Union[Unset, str]): Filter by Slack user ID Example: U12345678.
        include_inactive (Union[Unset, bool]): Include deactivated or not-yet-active users
            (defaults to false). Useful for resolving users who have since been offboarded. Example:
            True.
        page_size (Union[Unset, int]): Integer number of records to return Default: 25. Example:
            25.
        after (Union[Unset, str]): An record's ID. This endpoint will return a list of records
            after this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UsersListResultV2]
    """

    return sync_detailed(
        client=client,
        email=email,
        slack_user_id=slack_user_id,
        include_inactive=include_inactive,
        page_size=page_size,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    email: Union[Unset, str] = UNSET,
    slack_user_id: Union[Unset, str] = UNSET,
    include_inactive: Union[Unset, bool] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, UsersListResultV2]]:
    """List Users V2

     List users in your account.

    Args:
        email (Union[Unset, str]): Filter by email address Example: john.doe@incident.io.
        slack_user_id (Union[Unset, str]): Filter by Slack user ID Example: U12345678.
        include_inactive (Union[Unset, bool]): Include deactivated or not-yet-active users
            (defaults to false). Useful for resolving users who have since been offboarded. Example:
            True.
        page_size (Union[Unset, int]): Integer number of records to return Default: 25. Example:
            25.
        after (Union[Unset, str]): An record's ID. This endpoint will return a list of records
            after this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UsersListResultV2]]
    """

    kwargs = _get_kwargs(
        email=email,
        slack_user_id=slack_user_id,
        include_inactive=include_inactive,
        page_size=page_size,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    email: Union[Unset, str] = UNSET,
    slack_user_id: Union[Unset, str] = UNSET,
    include_inactive: Union[Unset, bool] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, UsersListResultV2]]:
    """List Users V2

     List users in your account.

    Args:
        email (Union[Unset, str]): Filter by email address Example: john.doe@incident.io.
        slack_user_id (Union[Unset, str]): Filter by Slack user ID Example: U12345678.
        include_inactive (Union[Unset, bool]): Include deactivated or not-yet-active users
            (defaults to false). Useful for resolving users who have since been offboarded. Example:
            True.
        page_size (Union[Unset, int]): Integer number of records to return Default: 25. Example:
            25.
        after (Union[Unset, str]): An record's ID. This endpoint will return a list of records
            after this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UsersListResultV2]
    """

    return (
        await asyncio_detailed(
            client=client,
            email=email,
            slack_user_id=slack_user_id,
            include_inactive=include_inactive,
            page_size=page_size,
            after=after,
        )
    ).parsed
