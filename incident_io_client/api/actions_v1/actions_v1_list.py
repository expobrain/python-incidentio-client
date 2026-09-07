from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.actions_list_result_v1 import ActionsListResultV1
from ...models.actions_v1_list_incident_mode import ActionsV1ListIncidentMode
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    incident_id: Union[Unset, str] = UNSET,
    is_follow_up: Union[Unset, bool] = UNSET,
    incident_mode: Union[Unset, ActionsV1ListIncidentMode] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["incident_id"] = incident_id

    params["is_follow_up"] = is_follow_up

    json_incident_mode: Union[Unset, str] = UNSET
    if not isinstance(incident_mode, Unset):
        json_incident_mode = incident_mode.value

    params["incident_mode"] = json_incident_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/actions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ActionsListResultV1, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = ActionsListResultV1.from_dict(response.json())

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
) -> Response[Union[ActionsListResultV1, ErrorResponse]]:
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
    is_follow_up: Union[Unset, bool] = UNSET,
    incident_mode: Union[Unset, ActionsV1ListIncidentMode] = UNSET,
) -> Response[Union[ActionsListResultV1, ErrorResponse]]:
    """List Actions V1

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, str]):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        is_follow_up (Union[Unset, bool]): Filter to actions marked as being follow up actions
            Example: True.
        incident_mode (Union[Unset, ActionsV1ListIncidentMode]): Filter to actions from incidents
            of the given mode. If not set, only actions from `real` incidents are returned Example:
            real.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionsListResultV1, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        is_follow_up=is_follow_up,
        incident_mode=incident_mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    is_follow_up: Union[Unset, bool] = UNSET,
    incident_mode: Union[Unset, ActionsV1ListIncidentMode] = UNSET,
) -> Optional[Union[ActionsListResultV1, ErrorResponse]]:
    """List Actions V1

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, str]):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        is_follow_up (Union[Unset, bool]): Filter to actions marked as being follow up actions
            Example: True.
        incident_mode (Union[Unset, ActionsV1ListIncidentMode]): Filter to actions from incidents
            of the given mode. If not set, only actions from `real` incidents are returned Example:
            real.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActionsListResultV1, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        incident_id=incident_id,
        is_follow_up=is_follow_up,
        incident_mode=incident_mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    is_follow_up: Union[Unset, bool] = UNSET,
    incident_mode: Union[Unset, ActionsV1ListIncidentMode] = UNSET,
) -> Response[Union[ActionsListResultV1, ErrorResponse]]:
    """List Actions V1

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, str]):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        is_follow_up (Union[Unset, bool]): Filter to actions marked as being follow up actions
            Example: True.
        incident_mode (Union[Unset, ActionsV1ListIncidentMode]): Filter to actions from incidents
            of the given mode. If not set, only actions from `real` incidents are returned Example:
            real.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionsListResultV1, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        is_follow_up=is_follow_up,
        incident_mode=incident_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    is_follow_up: Union[Unset, bool] = UNSET,
    incident_mode: Union[Unset, ActionsV1ListIncidentMode] = UNSET,
) -> Optional[Union[ActionsListResultV1, ErrorResponse]]:
    """List Actions V1

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, str]):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        is_follow_up (Union[Unset, bool]): Filter to actions marked as being follow up actions
            Example: True.
        incident_mode (Union[Unset, ActionsV1ListIncidentMode]): Filter to actions from incidents
            of the given mode. If not set, only actions from `real` incidents are returned Example:
            real.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActionsListResultV1, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            is_follow_up=is_follow_up,
            incident_mode=incident_mode,
        )
    ).parsed
