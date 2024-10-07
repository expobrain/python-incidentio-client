from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.schedules_v2_create_override_request_body import (
    SchedulesV2CreateOverrideRequestBody,
)
from ...models.schedules_v2_create_override_response_body import (
    SchedulesV2CreateOverrideResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: SchedulesV2CreateOverrideRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/schedule_overrides",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SchedulesV2CreateOverrideResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SchedulesV2CreateOverrideResponseBody.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SchedulesV2CreateOverrideResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SchedulesV2CreateOverrideRequestBody,
) -> Response[SchedulesV2CreateOverrideResponseBody]:
    """CreateOverride Schedules V2

     Create a new schedule override.

    Args:
        body (SchedulesV2CreateOverrideRequestBody):  Example: {'end_at':
            '2021-08-17T14:00:00.000000Z', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'schedule_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at':
            '2021-08-17T13:00:00.000000Z', 'user': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SchedulesV2CreateOverrideResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SchedulesV2CreateOverrideRequestBody,
) -> Optional[SchedulesV2CreateOverrideResponseBody]:
    """CreateOverride Schedules V2

     Create a new schedule override.

    Args:
        body (SchedulesV2CreateOverrideRequestBody):  Example: {'end_at':
            '2021-08-17T14:00:00.000000Z', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'schedule_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at':
            '2021-08-17T13:00:00.000000Z', 'user': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SchedulesV2CreateOverrideResponseBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SchedulesV2CreateOverrideRequestBody,
) -> Response[SchedulesV2CreateOverrideResponseBody]:
    """CreateOverride Schedules V2

     Create a new schedule override.

    Args:
        body (SchedulesV2CreateOverrideRequestBody):  Example: {'end_at':
            '2021-08-17T14:00:00.000000Z', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'schedule_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at':
            '2021-08-17T13:00:00.000000Z', 'user': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SchedulesV2CreateOverrideResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SchedulesV2CreateOverrideRequestBody,
) -> Optional[SchedulesV2CreateOverrideResponseBody]:
    """CreateOverride Schedules V2

     Create a new schedule override.

    Args:
        body (SchedulesV2CreateOverrideRequestBody):  Example: {'end_at':
            '2021-08-17T14:00:00.000000Z', 'layer_id': '01G0J1EXE7AXZ2C93K61WBPYNH', 'rotation_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'schedule_id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'start_at':
            '2021-08-17T13:00:00.000000Z', 'user': {'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SchedulesV2CreateOverrideResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
