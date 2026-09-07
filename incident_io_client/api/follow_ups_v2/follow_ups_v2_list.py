from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.follow_ups_list_result_v2 import FollowUpsListResultV2
from ...models.follow_ups_v2_list_incident_mode import FollowUpsV2ListIncidentMode
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    incident_id: Union[Unset, str] = UNSET,
    incident_mode: Union[Unset, FollowUpsV2ListIncidentMode] = UNSET,
    assignee_team_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["incident_id"] = incident_id

    json_incident_mode: Union[Unset, str] = UNSET
    if not isinstance(incident_mode, Unset):
        json_incident_mode = incident_mode.value

    params["incident_mode"] = json_incident_mode

    params["assignee_team_id"] = assignee_team_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/follow_ups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, FollowUpsListResultV2]]:
    if response.status_code == 200:
        response_200 = FollowUpsListResultV2.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, FollowUpsListResultV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    incident_mode: Union[Unset, FollowUpsV2ListIncidentMode] = UNSET,
    assignee_team_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, FollowUpsListResultV2]]:
    """List Follow-ups V2

     List all follow-ups for an organisation.

    Args:
        incident_id (Union[Unset, str]):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_mode (Union[Unset, FollowUpsV2ListIncidentMode]): Filter to follow-ups from
            incidents of the given mode. If not set, only follow-ups from `standard` and
            `retrospective` incidents are returned Example: standard.
        assignee_team_id (Union[Unset, str]): Filter follow-ups that are assigned to the given
            team Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FollowUpsListResultV2]]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        incident_mode=incident_mode,
        assignee_team_id=assignee_team_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    incident_mode: Union[Unset, FollowUpsV2ListIncidentMode] = UNSET,
    assignee_team_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, FollowUpsListResultV2]]:
    """List Follow-ups V2

     List all follow-ups for an organisation.

    Args:
        incident_id (Union[Unset, str]):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_mode (Union[Unset, FollowUpsV2ListIncidentMode]): Filter to follow-ups from
            incidents of the given mode. If not set, only follow-ups from `standard` and
            `retrospective` incidents are returned Example: standard.
        assignee_team_id (Union[Unset, str]): Filter follow-ups that are assigned to the given
            team Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FollowUpsListResultV2]
    """

    return sync_detailed(
        client=client,
        incident_id=incident_id,
        incident_mode=incident_mode,
        assignee_team_id=assignee_team_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    incident_mode: Union[Unset, FollowUpsV2ListIncidentMode] = UNSET,
    assignee_team_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, FollowUpsListResultV2]]:
    """List Follow-ups V2

     List all follow-ups for an organisation.

    Args:
        incident_id (Union[Unset, str]):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_mode (Union[Unset, FollowUpsV2ListIncidentMode]): Filter to follow-ups from
            incidents of the given mode. If not set, only follow-ups from `standard` and
            `retrospective` incidents are returned Example: standard.
        assignee_team_id (Union[Unset, str]): Filter follow-ups that are assigned to the given
            team Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FollowUpsListResultV2]]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        incident_mode=incident_mode,
        assignee_team_id=assignee_team_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    incident_mode: Union[Unset, FollowUpsV2ListIncidentMode] = UNSET,
    assignee_team_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, FollowUpsListResultV2]]:
    """List Follow-ups V2

     List all follow-ups for an organisation.

    Args:
        incident_id (Union[Unset, str]):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_mode (Union[Unset, FollowUpsV2ListIncidentMode]): Filter to follow-ups from
            incidents of the given mode. If not set, only follow-ups from `standard` and
            `retrospective` incidents are returned Example: standard.
        assignee_team_id (Union[Unset, str]): Filter follow-ups that are assigned to the given
            team Example: 01FCNDV6P870EA6S7TK1DSYDG0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FollowUpsListResultV2]
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            incident_mode=incident_mode,
            assignee_team_id=assignee_team_id,
        )
    ).parsed
