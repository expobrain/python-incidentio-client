from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.schedules_v2_update_request_body import SchedulesV2UpdateRequestBody
from ...models.schedules_v2_update_response_body import SchedulesV2UpdateResponseBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: SchedulesV2UpdateRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/v2/schedules/{id}".format(
            id=id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SchedulesV2UpdateResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SchedulesV2UpdateResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SchedulesV2UpdateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SchedulesV2UpdateRequestBody,
) -> Response[SchedulesV2UpdateResponseBody]:
    """Update Schedules V2

     Update a schedule.

    Args:
        id (str):
        body (SchedulesV2UpdateRequestBody):  Example: {'schedule': {'annotations':
            {'incident.io/terraform/version': 'version-of-terraform'}, 'config': {'rotations':
            [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'daily'}],
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'My Rotation', 'users': [{'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}], 'working_interval':
            [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'tuesday'}]}]},
            'holidays_public_config': {'country_codes': ['abc123']}, 'name': 'My Schedule',
            'timezone': 'America/Los_Angeles'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SchedulesV2UpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SchedulesV2UpdateRequestBody,
) -> Optional[SchedulesV2UpdateResponseBody]:
    """Update Schedules V2

     Update a schedule.

    Args:
        id (str):
        body (SchedulesV2UpdateRequestBody):  Example: {'schedule': {'annotations':
            {'incident.io/terraform/version': 'version-of-terraform'}, 'config': {'rotations':
            [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'daily'}],
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'My Rotation', 'users': [{'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}], 'working_interval':
            [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'tuesday'}]}]},
            'holidays_public_config': {'country_codes': ['abc123']}, 'name': 'My Schedule',
            'timezone': 'America/Los_Angeles'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SchedulesV2UpdateResponseBody
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SchedulesV2UpdateRequestBody,
) -> Response[SchedulesV2UpdateResponseBody]:
    """Update Schedules V2

     Update a schedule.

    Args:
        id (str):
        body (SchedulesV2UpdateRequestBody):  Example: {'schedule': {'annotations':
            {'incident.io/terraform/version': 'version-of-terraform'}, 'config': {'rotations':
            [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'daily'}],
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'My Rotation', 'users': [{'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}], 'working_interval':
            [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'tuesday'}]}]},
            'holidays_public_config': {'country_codes': ['abc123']}, 'name': 'My Schedule',
            'timezone': 'America/Los_Angeles'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SchedulesV2UpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SchedulesV2UpdateRequestBody,
) -> Optional[SchedulesV2UpdateResponseBody]:
    """Update Schedules V2

     Update a schedule.

    Args:
        id (str):
        body (SchedulesV2UpdateRequestBody):  Example: {'schedule': {'annotations':
            {'incident.io/terraform/version': 'version-of-terraform'}, 'config': {'rotations':
            [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at':
            '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1, 'interval_type': 'daily'}],
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'My Rotation', 'users': [{'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}], 'working_interval':
            [{'end_time': '17:00', 'start_time': '09:00', 'weekday': 'tuesday'}]}]},
            'holidays_public_config': {'country_codes': ['abc123']}, 'name': 'My Schedule',
            'timezone': 'America/Los_Angeles'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SchedulesV2UpdateResponseBody
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
