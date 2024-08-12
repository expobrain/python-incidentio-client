import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.schedules_v2_list_schedule_entries_response_body import (
    SchedulesV2ListScheduleEntriesResponseBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    schedule_id: str,
    entry_window_start: Union[Unset, datetime.datetime] = UNSET,
    entry_window_end: Union[Unset, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["schedule_id"] = schedule_id

    json_entry_window_start: Union[Unset, str] = UNSET
    if not isinstance(entry_window_start, Unset):
        json_entry_window_start = entry_window_start.isoformat()
    params["entry_window_start"] = json_entry_window_start

    json_entry_window_end: Union[Unset, str] = UNSET
    if not isinstance(entry_window_end, Unset):
        json_entry_window_end = entry_window_end.isoformat()
    params["entry_window_end"] = json_entry_window_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/schedule_entries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SchedulesV2ListScheduleEntriesResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SchedulesV2ListScheduleEntriesResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SchedulesV2ListScheduleEntriesResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    schedule_id: str,
    entry_window_start: Union[Unset, datetime.datetime] = UNSET,
    entry_window_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[SchedulesV2ListScheduleEntriesResponseBody]:
    """ListScheduleEntries Schedules V2

     Get a list of schedule entries. The endpoint will return all entries that overlap with the given
    window, if one is provided.

    Args:
        schedule_id (str):
        entry_window_start (Union[Unset, datetime.datetime]):
        entry_window_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SchedulesV2ListScheduleEntriesResponseBody]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        entry_window_start=entry_window_start,
        entry_window_end=entry_window_end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    schedule_id: str,
    entry_window_start: Union[Unset, datetime.datetime] = UNSET,
    entry_window_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[SchedulesV2ListScheduleEntriesResponseBody]:
    """ListScheduleEntries Schedules V2

     Get a list of schedule entries. The endpoint will return all entries that overlap with the given
    window, if one is provided.

    Args:
        schedule_id (str):
        entry_window_start (Union[Unset, datetime.datetime]):
        entry_window_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SchedulesV2ListScheduleEntriesResponseBody
    """

    return sync_detailed(
        client=client,
        schedule_id=schedule_id,
        entry_window_start=entry_window_start,
        entry_window_end=entry_window_end,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    schedule_id: str,
    entry_window_start: Union[Unset, datetime.datetime] = UNSET,
    entry_window_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[SchedulesV2ListScheduleEntriesResponseBody]:
    """ListScheduleEntries Schedules V2

     Get a list of schedule entries. The endpoint will return all entries that overlap with the given
    window, if one is provided.

    Args:
        schedule_id (str):
        entry_window_start (Union[Unset, datetime.datetime]):
        entry_window_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SchedulesV2ListScheduleEntriesResponseBody]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        entry_window_start=entry_window_start,
        entry_window_end=entry_window_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    schedule_id: str,
    entry_window_start: Union[Unset, datetime.datetime] = UNSET,
    entry_window_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[SchedulesV2ListScheduleEntriesResponseBody]:
    """ListScheduleEntries Schedules V2

     Get a list of schedule entries. The endpoint will return all entries that overlap with the given
    window, if one is provided.

    Args:
        schedule_id (str):
        entry_window_start (Union[Unset, datetime.datetime]):
        entry_window_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SchedulesV2ListScheduleEntriesResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            schedule_id=schedule_id,
            entry_window_start=entry_window_start,
            entry_window_end=entry_window_end,
        )
    ).parsed
