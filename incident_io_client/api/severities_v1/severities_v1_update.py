from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.severities_v1_update_request_body import SeveritiesV1UpdateRequestBody
from ...models.severities_v1_update_response_body import SeveritiesV1UpdateResponseBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: SeveritiesV1UpdateRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/v1/severities/{id}".format(
            id=id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SeveritiesV1UpdateResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SeveritiesV1UpdateResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SeveritiesV1UpdateResponseBody]:
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
    body: SeveritiesV1UpdateRequestBody,
) -> Response[SeveritiesV1UpdateResponseBody]:
    """Update Severities V1

     Update an existing severity

    Args:
        id (str):
        body (SeveritiesV1UpdateRequestBody):  Example: {'description': 'Issues with **low
            impact**.', 'name': 'Minor', 'rank': 1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SeveritiesV1UpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SeveritiesV1UpdateRequestBody,
) -> Optional[SeveritiesV1UpdateResponseBody]:
    """Update Severities V1

     Update an existing severity

    Args:
        id (str):
        body (SeveritiesV1UpdateRequestBody):  Example: {'description': 'Issues with **low
            impact**.', 'name': 'Minor', 'rank': 1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SeveritiesV1UpdateResponseBody
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SeveritiesV1UpdateRequestBody,
) -> Response[SeveritiesV1UpdateResponseBody]:
    """Update Severities V1

     Update an existing severity

    Args:
        id (str):
        body (SeveritiesV1UpdateRequestBody):  Example: {'description': 'Issues with **low
            impact**.', 'name': 'Minor', 'rank': 1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SeveritiesV1UpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SeveritiesV1UpdateRequestBody,
) -> Optional[SeveritiesV1UpdateResponseBody]:
    """Update Severities V1

     Update an existing severity

    Args:
        id (str):
        body (SeveritiesV1UpdateRequestBody):  Example: {'description': 'Issues with **low
            impact**.', 'name': 'Minor', 'rank': 1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SeveritiesV1UpdateResponseBody
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
