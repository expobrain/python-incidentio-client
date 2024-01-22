from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_updates_v2_list_response_body import (
    IncidentUpdatesV2ListResponseBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    incident_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["incident_id"] = incident_id

    params["page_size"] = page_size

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/incident_updates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentUpdatesV2ListResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentUpdatesV2ListResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentUpdatesV2ListResponseBody]:
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
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Response[IncidentUpdatesV2ListResponseBody]:
    """List Incident Updates V2

     List all incident updates for an organisation, or for a specific incident.

    Args:
        incident_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentUpdatesV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        page_size=page_size,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Optional[IncidentUpdatesV2ListResponseBody]:
    """List Incident Updates V2

     List all incident updates for an organisation, or for a specific incident.

    Args:
        incident_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentUpdatesV2ListResponseBody
    """

    return sync_detailed(
        client=client,
        incident_id=incident_id,
        page_size=page_size,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Response[IncidentUpdatesV2ListResponseBody]:
    """List Incident Updates V2

     List all incident updates for an organisation, or for a specific incident.

    Args:
        incident_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentUpdatesV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        page_size=page_size,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Optional[IncidentUpdatesV2ListResponseBody]:
    """List Incident Updates V2

     List all incident updates for an organisation, or for a specific incident.

    Args:
        incident_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentUpdatesV2ListResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            page_size=page_size,
            after=after,
        )
    ).parsed
