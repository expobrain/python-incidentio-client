from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.follow_ups_v2_list_incident_mode import FollowUpsV2ListIncidentMode
from ...models.follow_ups_v2_list_response_body import FollowUpsV2ListResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_mode: Union[Unset, None, FollowUpsV2ListIncidentMode] = UNSET,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/follow_ups"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["incident_id"] = incident_id

    json_incident_mode: Union[Unset, None, str] = UNSET
    if not isinstance(incident_mode, Unset):
        json_incident_mode = incident_mode.value if incident_mode else None

    params["incident_mode"] = json_incident_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[FollowUpsV2ListResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FollowUpsV2ListResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[FollowUpsV2ListResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_mode: Union[Unset, None, FollowUpsV2ListIncidentMode] = UNSET,
) -> Response[FollowUpsV2ListResponseBody]:
    """List Follow-ups V2

     List all follow-ups for an organisation.

    Args:
        incident_id (Union[Unset, None, str]):
        incident_mode (Union[Unset, None, FollowUpsV2ListIncidentMode]):

    Returns:
        Response[FollowUpsV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        incident_id=incident_id,
        incident_mode=incident_mode,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_mode: Union[Unset, None, FollowUpsV2ListIncidentMode] = UNSET,
) -> Optional[FollowUpsV2ListResponseBody]:
    """List Follow-ups V2

     List all follow-ups for an organisation.

    Args:
        incident_id (Union[Unset, None, str]):
        incident_mode (Union[Unset, None, FollowUpsV2ListIncidentMode]):

    Returns:
        Response[FollowUpsV2ListResponseBody]
    """

    return sync_detailed(
        client=client,
        incident_id=incident_id,
        incident_mode=incident_mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_mode: Union[Unset, None, FollowUpsV2ListIncidentMode] = UNSET,
) -> Response[FollowUpsV2ListResponseBody]:
    """List Follow-ups V2

     List all follow-ups for an organisation.

    Args:
        incident_id (Union[Unset, None, str]):
        incident_mode (Union[Unset, None, FollowUpsV2ListIncidentMode]):

    Returns:
        Response[FollowUpsV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        incident_id=incident_id,
        incident_mode=incident_mode,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_mode: Union[Unset, None, FollowUpsV2ListIncidentMode] = UNSET,
) -> Optional[FollowUpsV2ListResponseBody]:
    """List Follow-ups V2

     List all follow-ups for an organisation.

    Args:
        incident_id (Union[Unset, None, str]):
        incident_mode (Union[Unset, None, FollowUpsV2ListIncidentMode]):

    Returns:
        Response[FollowUpsV2ListResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            incident_mode=incident_mode,
        )
    ).parsed
