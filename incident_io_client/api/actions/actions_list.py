from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.actions_list_incident_mode import ActionsListIncidentMode
from ...models.actions_list_response_body import ActionsListResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    is_follow_up: Union[Unset, None, bool] = UNSET,
    incident_mode: Union[Unset, None, ActionsListIncidentMode] = UNSET,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/actions"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["incident_id"] = incident_id

    params["is_follow_up"] = is_follow_up

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


def _parse_response(*, response: httpx.Response) -> Optional[ActionsListResponseBody]:
    if response.status_code == 200:
        response_200 = ActionsListResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionsListResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    is_follow_up: Union[Unset, None, bool] = UNSET,
    incident_mode: Union[Unset, None, ActionsListIncidentMode] = UNSET,
) -> Response[ActionsListResponseBody]:
    """List Actions

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, None, str]):
        is_follow_up (Union[Unset, None, bool]):
        incident_mode (Union[Unset, None, ActionsListIncidentMode]):

    Returns:
        Response[ActionsListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        incident_id=incident_id,
        is_follow_up=is_follow_up,
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
    is_follow_up: Union[Unset, None, bool] = UNSET,
    incident_mode: Union[Unset, None, ActionsListIncidentMode] = UNSET,
) -> Optional[ActionsListResponseBody]:
    """List Actions

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, None, str]):
        is_follow_up (Union[Unset, None, bool]):
        incident_mode (Union[Unset, None, ActionsListIncidentMode]):

    Returns:
        Response[ActionsListResponseBody]
    """

    return sync_detailed(
        client=client,
        incident_id=incident_id,
        is_follow_up=is_follow_up,
        incident_mode=incident_mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    is_follow_up: Union[Unset, None, bool] = UNSET,
    incident_mode: Union[Unset, None, ActionsListIncidentMode] = UNSET,
) -> Response[ActionsListResponseBody]:
    """List Actions

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, None, str]):
        is_follow_up (Union[Unset, None, bool]):
        incident_mode (Union[Unset, None, ActionsListIncidentMode]):

    Returns:
        Response[ActionsListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        incident_id=incident_id,
        is_follow_up=is_follow_up,
        incident_mode=incident_mode,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    is_follow_up: Union[Unset, None, bool] = UNSET,
    incident_mode: Union[Unset, None, ActionsListIncidentMode] = UNSET,
) -> Optional[ActionsListResponseBody]:
    """List Actions

     List all actions for an organisation.

    Args:
        incident_id (Union[Unset, None, str]):
        is_follow_up (Union[Unset, None, bool]):
        incident_mode (Union[Unset, None, ActionsListIncidentMode]):

    Returns:
        Response[ActionsListResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            is_follow_up=is_follow_up,
            incident_mode=incident_mode,
        )
    ).parsed
