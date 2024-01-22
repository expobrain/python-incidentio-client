from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.actions_v1_list_incident_mode import ActionsV1ListIncidentMode
from ...models.actions_v1_list_response_body import ActionsV1ListResponseBody
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
) -> Optional[ActionsV1ListResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ActionsV1ListResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ActionsV1ListResponseBody]:
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
) -> Response[ActionsV1ListResponseBody]:
    """List Actions V1

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, str]):
        is_follow_up (Union[Unset, bool]):
        incident_mode (Union[Unset, ActionsV1ListIncidentMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsV1ListResponseBody]
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
) -> Optional[ActionsV1ListResponseBody]:
    """List Actions V1

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, str]):
        is_follow_up (Union[Unset, bool]):
        incident_mode (Union[Unset, ActionsV1ListIncidentMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsV1ListResponseBody
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
) -> Response[ActionsV1ListResponseBody]:
    """List Actions V1

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, str]):
        is_follow_up (Union[Unset, bool]):
        incident_mode (Union[Unset, ActionsV1ListIncidentMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsV1ListResponseBody]
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
) -> Optional[ActionsV1ListResponseBody]:
    """List Actions V1

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, str]):
        is_follow_up (Union[Unset, bool]):
        incident_mode (Union[Unset, ActionsV1ListIncidentMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsV1ListResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            is_follow_up=is_follow_up,
            incident_mode=incident_mode,
        )
    ).parsed
