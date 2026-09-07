from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incident_activity_log_entries_list_result_v2 import (
    IncidentActivityLogEntriesListResultV2,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    incident_id: str,
    id: Union[Unset, List[str]] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["incident_id"] = incident_id

    json_id: Union[Unset, List[str]] = UNSET
    if not isinstance(id, Unset):
        json_id = id

    params["id"] = json_id

    params["page_size"] = page_size

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/incident_activity_log_entries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, IncidentActivityLogEntriesListResultV2]]:
    if response.status_code == 200:
        response_200 = IncidentActivityLogEntriesListResultV2.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, IncidentActivityLogEntriesListResultV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: str,
    id: Union[Unset, List[str]] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, IncidentActivityLogEntriesListResultV2]]:
    """List Incident Activity Log Entries V2

     List the activity log entries for an incident, oldest first.

    If the incident has streams, this returns their entries too, and incident_id on each entry
    tells you which stream it came from.

    Platform noise is left out: channel joins and leaves, chat messages and call transcript
    fragments are recorded internally but never returned here.

    Args:
        incident_id (str):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        id (Union[Unset, List[str]]): Return only the entries with these IDs Example:
            ['01FCNDV6P870EA6S7TK1DSYDG0', '01FCNDV6P870EA6S7TK1DSYDG1'].
        page_size (Union[Unset, int]): Integer number of records to return Default: 25. Example:
            25.
        after (Union[Unset, str]): An entry's ID. This endpoint returns the entries that follow
            it. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, IncidentActivityLogEntriesListResultV2]]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        id=id,
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
    incident_id: str,
    id: Union[Unset, List[str]] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, IncidentActivityLogEntriesListResultV2]]:
    """List Incident Activity Log Entries V2

     List the activity log entries for an incident, oldest first.

    If the incident has streams, this returns their entries too, and incident_id on each entry
    tells you which stream it came from.

    Platform noise is left out: channel joins and leaves, chat messages and call transcript
    fragments are recorded internally but never returned here.

    Args:
        incident_id (str):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        id (Union[Unset, List[str]]): Return only the entries with these IDs Example:
            ['01FCNDV6P870EA6S7TK1DSYDG0', '01FCNDV6P870EA6S7TK1DSYDG1'].
        page_size (Union[Unset, int]): Integer number of records to return Default: 25. Example:
            25.
        after (Union[Unset, str]): An entry's ID. This endpoint returns the entries that follow
            it. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, IncidentActivityLogEntriesListResultV2]
    """

    return sync_detailed(
        client=client,
        incident_id=incident_id,
        id=id,
        page_size=page_size,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: str,
    id: Union[Unset, List[str]] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, IncidentActivityLogEntriesListResultV2]]:
    """List Incident Activity Log Entries V2

     List the activity log entries for an incident, oldest first.

    If the incident has streams, this returns their entries too, and incident_id on each entry
    tells you which stream it came from.

    Platform noise is left out: channel joins and leaves, chat messages and call transcript
    fragments are recorded internally but never returned here.

    Args:
        incident_id (str):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        id (Union[Unset, List[str]]): Return only the entries with these IDs Example:
            ['01FCNDV6P870EA6S7TK1DSYDG0', '01FCNDV6P870EA6S7TK1DSYDG1'].
        page_size (Union[Unset, int]): Integer number of records to return Default: 25. Example:
            25.
        after (Union[Unset, str]): An entry's ID. This endpoint returns the entries that follow
            it. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, IncidentActivityLogEntriesListResultV2]]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        id=id,
        page_size=page_size,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: str,
    id: Union[Unset, List[str]] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, IncidentActivityLogEntriesListResultV2]]:
    """List Incident Activity Log Entries V2

     List the activity log entries for an incident, oldest first.

    If the incident has streams, this returns their entries too, and incident_id on each entry
    tells you which stream it came from.

    Platform noise is left out: channel joins and leaves, chat messages and call transcript
    fragments are recorded internally but never returned here.

    Args:
        incident_id (str):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        id (Union[Unset, List[str]]): Return only the entries with these IDs Example:
            ['01FCNDV6P870EA6S7TK1DSYDG0', '01FCNDV6P870EA6S7TK1DSYDG1'].
        page_size (Union[Unset, int]): Integer number of records to return Default: 25. Example:
            25.
        after (Union[Unset, str]): An entry's ID. This endpoint returns the entries that follow
            it. Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, IncidentActivityLogEntriesListResultV2]
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            id=id,
            page_size=page_size,
            after=after,
        )
    ).parsed
