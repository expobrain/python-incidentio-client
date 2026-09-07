from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.maintenance_windows_list_result_v1 import MaintenanceWindowsListResultV1
from ...models.maintenance_windows_v1_list_status import MaintenanceWindowsV1ListStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    status: Union[Unset, MaintenanceWindowsV1ListStatus] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/maintenance_windows",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, MaintenanceWindowsListResultV1]]:
    if response.status_code == 200:
        response_200 = MaintenanceWindowsListResultV1.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, MaintenanceWindowsListResultV1]]:
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
    status: Union[Unset, MaintenanceWindowsV1ListStatus] = UNSET,
) -> Response[Union[ErrorResponse, MaintenanceWindowsListResultV1]]:
    """List MaintenanceWindows V1

     List maintenance windows for your organisation.

    Args:
        page_size (Union[Unset, int]): Number of maintenance windows to return per page Default:
            25. Example: 25.
        after (Union[Unset, str]): The ID of the last maintenance window on the previous page
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        status (Union[Unset, MaintenanceWindowsV1ListStatus]): Filter by window status: active
            (start_at <= now < end_at), upcoming (now < start_at), or past (end_at <= now) Example:
            active.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, MaintenanceWindowsListResultV1]]
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
    status: Union[Unset, MaintenanceWindowsV1ListStatus] = UNSET,
) -> Optional[Union[ErrorResponse, MaintenanceWindowsListResultV1]]:
    """List MaintenanceWindows V1

     List maintenance windows for your organisation.

    Args:
        page_size (Union[Unset, int]): Number of maintenance windows to return per page Default:
            25. Example: 25.
        after (Union[Unset, str]): The ID of the last maintenance window on the previous page
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        status (Union[Unset, MaintenanceWindowsV1ListStatus]): Filter by window status: active
            (start_at <= now < end_at), upcoming (now < start_at), or past (end_at <= now) Example:
            active.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, MaintenanceWindowsListResultV1]
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
    status: Union[Unset, MaintenanceWindowsV1ListStatus] = UNSET,
) -> Response[Union[ErrorResponse, MaintenanceWindowsListResultV1]]:
    """List MaintenanceWindows V1

     List maintenance windows for your organisation.

    Args:
        page_size (Union[Unset, int]): Number of maintenance windows to return per page Default:
            25. Example: 25.
        after (Union[Unset, str]): The ID of the last maintenance window on the previous page
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        status (Union[Unset, MaintenanceWindowsV1ListStatus]): Filter by window status: active
            (start_at <= now < end_at), upcoming (now < start_at), or past (end_at <= now) Example:
            active.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, MaintenanceWindowsListResultV1]]
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
    status: Union[Unset, MaintenanceWindowsV1ListStatus] = UNSET,
) -> Optional[Union[ErrorResponse, MaintenanceWindowsListResultV1]]:
    """List MaintenanceWindows V1

     List maintenance windows for your organisation.

    Args:
        page_size (Union[Unset, int]): Number of maintenance windows to return per page Default:
            25. Example: 25.
        after (Union[Unset, str]): The ID of the last maintenance window on the previous page
            Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        status (Union[Unset, MaintenanceWindowsV1ListStatus]): Filter by window status: active
            (start_at <= now < end_at), upcoming (now < start_at), or past (end_at <= now) Example:
            active.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, MaintenanceWindowsListResultV1]
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            status=status,
        )
    ).parsed
