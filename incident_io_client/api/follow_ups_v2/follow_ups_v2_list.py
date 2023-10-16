from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.follow_ups_v2_list_incident_mode import FollowUpsV2ListIncidentMode
from ...models.follow_ups_v2_list_response_body import FollowUpsV2ListResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_mode: Union[Unset, None, FollowUpsV2ListIncidentMode] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["incident_id"] = incident_id

    json_incident_mode: Union[Unset, None, str] = UNSET
    if not isinstance(incident_mode, Unset):
        json_incident_mode = incident_mode.value if incident_mode else None

    params["incident_mode"] = json_incident_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v2/follow_ups",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FollowUpsV2ListResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FollowUpsV2ListResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FollowUpsV2ListResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, None, str] = UNSET,
    incident_mode: Union[Unset, None, FollowUpsV2ListIncidentMode] = UNSET,
) -> Response[FollowUpsV2ListResponseBody]:
    """List Follow-ups V2

     List all follow-ups for an organisation.

    Args:
        incident_id (Union[Unset, None, str]):
        incident_mode (Union[Unset, None, FollowUpsV2ListIncidentMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FollowUpsV2ListResponseBody]
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
    incident_id: Union[Unset, None, str] = UNSET,
    incident_mode: Union[Unset, None, FollowUpsV2ListIncidentMode] = UNSET,
) -> Optional[FollowUpsV2ListResponseBody]:
    """List Follow-ups V2

     List all follow-ups for an organisation.

    Args:
        incident_id (Union[Unset, None, str]):
        incident_mode (Union[Unset, None, FollowUpsV2ListIncidentMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FollowUpsV2ListResponseBody
    """

    return sync_detailed(
        client=client,
        incident_id=incident_id,
        incident_mode=incident_mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, None, str] = UNSET,
    incident_mode: Union[Unset, None, FollowUpsV2ListIncidentMode] = UNSET,
) -> Response[FollowUpsV2ListResponseBody]:
    """List Follow-ups V2

     List all follow-ups for an organisation.

    Args:
        incident_id (Union[Unset, None, str]):
        incident_mode (Union[Unset, None, FollowUpsV2ListIncidentMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FollowUpsV2ListResponseBody]
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
    incident_id: Union[Unset, None, str] = UNSET,
    incident_mode: Union[Unset, None, FollowUpsV2ListIncidentMode] = UNSET,
) -> Optional[FollowUpsV2ListResponseBody]:
    """List Follow-ups V2

     List all follow-ups for an organisation.

    Args:
        incident_id (Union[Unset, None, str]):
        incident_mode (Union[Unset, None, FollowUpsV2ListIncidentMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FollowUpsV2ListResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            incident_mode=incident_mode,
        )
    ).parsed
