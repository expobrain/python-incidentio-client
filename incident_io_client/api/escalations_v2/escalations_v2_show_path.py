from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.escalations_v2_show_path_response_body import (
    EscalationsV2ShowPathResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/escalation_paths/{id}".format(
            id=id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[EscalationsV2ShowPathResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EscalationsV2ShowPathResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EscalationsV2ShowPathResponseBody]:
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
) -> Response[EscalationsV2ShowPathResponseBody]:
    """ShowPath Escalations V2

     Show an escalation path.

    We recommend you create escalation paths in the incident.io dashboard where our path
    builder makes it easy to use conditions and visualise the path.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EscalationsV2ShowPathResponseBody]
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
) -> Optional[EscalationsV2ShowPathResponseBody]:
    """ShowPath Escalations V2

     Show an escalation path.

    We recommend you create escalation paths in the incident.io dashboard where our path
    builder makes it easy to use conditions and visualise the path.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EscalationsV2ShowPathResponseBody
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[EscalationsV2ShowPathResponseBody]:
    """ShowPath Escalations V2

     Show an escalation path.

    We recommend you create escalation paths in the incident.io dashboard where our path
    builder makes it easy to use conditions and visualise the path.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EscalationsV2ShowPathResponseBody]
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
) -> Optional[EscalationsV2ShowPathResponseBody]:
    """ShowPath Escalations V2

     Show an escalation path.

    We recommend you create escalation paths in the incident.io dashboard where our path
    builder makes it easy to use conditions and visualise the path.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EscalationsV2ShowPathResponseBody
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
