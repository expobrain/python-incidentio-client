from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.actions_v2_list_incident_mode import ActionsV2ListIncidentMode
from ...models.actions_v2_list_response_body import ActionsV2ListResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    incident_id: Union[Unset, str] = UNSET,
    incident_mode: Union[Unset, ActionsV2ListIncidentMode] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["incident_id"] = incident_id

    json_incident_mode: Union[Unset, str] = UNSET
    if not isinstance(incident_mode, Unset):
        json_incident_mode = incident_mode.value

    params["incident_mode"] = json_incident_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/actions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ActionsV2ListResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ActionsV2ListResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ActionsV2ListResponseBody]:
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
    incident_mode: Union[Unset, ActionsV2ListIncidentMode] = UNSET,
) -> Response[ActionsV2ListResponseBody]:
    """List Actions V2

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, str]):
        incident_mode (Union[Unset, ActionsV2ListIncidentMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
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
    incident_mode: Union[Unset, ActionsV2ListIncidentMode] = UNSET,
) -> Optional[ActionsV2ListResponseBody]:
    """List Actions V2

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, str]):
        incident_mode (Union[Unset, ActionsV2ListIncidentMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsV2ListResponseBody
    """

    return sync_detailed(
        client=client,
        incident_id=incident_id,
        incident_mode=incident_mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    incident_mode: Union[Unset, ActionsV2ListIncidentMode] = UNSET,
) -> Response[ActionsV2ListResponseBody]:
    """List Actions V2

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, str]):
        incident_mode (Union[Unset, ActionsV2ListIncidentMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        incident_mode=incident_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    incident_mode: Union[Unset, ActionsV2ListIncidentMode] = UNSET,
) -> Optional[ActionsV2ListResponseBody]:
    """List Actions V2

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, str]):
        incident_mode (Union[Unset, ActionsV2ListIncidentMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsV2ListResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            incident_mode=incident_mode,
        )
    ).parsed
