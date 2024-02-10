from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incidents_v2_show_response_body import IncidentsV2ShowResponseBody
from ...types import Response


def _get_kwargs(
    id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/incidents/{id}".format(
            id=id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentsV2ShowResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentsV2ShowResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentsV2ShowResponseBody]:
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
) -> Response[IncidentsV2ShowResponseBody]:
    r""" Show Incidents V2

     Get a single incident.

    The ID supplied can be either the incident's full ID, or the numeric part of its
    reference. For example, to get INC-123, you could use either its full ID or:

    		curl \
    			--get 'https://api.incident.io/v2/incidents/123

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentsV2ShowResponseBody]
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
) -> Optional[IncidentsV2ShowResponseBody]:
    r""" Show Incidents V2

     Get a single incident.

    The ID supplied can be either the incident's full ID, or the numeric part of its
    reference. For example, to get INC-123, you could use either its full ID or:

    		curl \
    			--get 'https://api.incident.io/v2/incidents/123

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentsV2ShowResponseBody
     """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[IncidentsV2ShowResponseBody]:
    r""" Show Incidents V2

     Get a single incident.

    The ID supplied can be either the incident's full ID, or the numeric part of its
    reference. For example, to get INC-123, you could use either its full ID or:

    		curl \
    			--get 'https://api.incident.io/v2/incidents/123

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentsV2ShowResponseBody]
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
) -> Optional[IncidentsV2ShowResponseBody]:
    r""" Show Incidents V2

     Get a single incident.

    The ID supplied can be either the incident's full ID, or the numeric part of its
    reference. For example, to get INC-123, you could use either its full ID or:

    		curl \
    			--get 'https://api.incident.io/v2/incidents/123

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentsV2ShowResponseBody
     """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
