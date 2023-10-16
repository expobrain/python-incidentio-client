from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_timestamps_v2_show_response_body import (
    IncidentTimestampsV2ShowResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v2/incident_timestamps/{id}".format(
            id=id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentTimestampsV2ShowResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentTimestampsV2ShowResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentTimestampsV2ShowResponseBody]:
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
) -> Response[IncidentTimestampsV2ShowResponseBody]:
    """Show Incident Timestamps V2

     Get a single incident timestamp.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentTimestampsV2ShowResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[IncidentTimestampsV2ShowResponseBody]:
    """Show Incident Timestamps V2

     Get a single incident timestamp.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentTimestampsV2ShowResponseBody
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[IncidentTimestampsV2ShowResponseBody]:
    """Show Incident Timestamps V2

     Get a single incident timestamp.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentTimestampsV2ShowResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[IncidentTimestampsV2ShowResponseBody]:
    """Show Incident Timestamps V2

     Get a single incident timestamp.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentTimestampsV2ShowResponseBody
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
