from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_v2_update_entry_request_body import (
    CatalogV2UpdateEntryRequestBody,
)
from ...models.catalog_v2_update_entry_response_body import (
    CatalogV2UpdateEntryResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: CatalogV2UpdateEntryRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/v2/catalog_entries/{id}".format(
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
) -> Optional[CatalogV2UpdateEntryResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CatalogV2UpdateEntryResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CatalogV2UpdateEntryResponseBody]:
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
    body: CatalogV2UpdateEntryRequestBody,
) -> Response[CatalogV2UpdateEntryResponseBody]:
    """UpdateEntry Catalog V2

     Updates an existing catalog entry.

    Args:
        id (str):
        body (CatalogV2UpdateEntryRequestBody):  Example: {'aliases': ['lawrence@incident.io',
            'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name':
            'Primary On-call', 'rank': 3}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2UpdateEntryResponseBody]
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
    body: CatalogV2UpdateEntryRequestBody,
) -> Optional[CatalogV2UpdateEntryResponseBody]:
    """UpdateEntry Catalog V2

     Updates an existing catalog entry.

    Args:
        id (str):
        body (CatalogV2UpdateEntryRequestBody):  Example: {'aliases': ['lawrence@incident.io',
            'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name':
            'Primary On-call', 'rank': 3}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2UpdateEntryResponseBody
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
    body: CatalogV2UpdateEntryRequestBody,
) -> Response[CatalogV2UpdateEntryResponseBody]:
    """UpdateEntry Catalog V2

     Updates an existing catalog entry.

    Args:
        id (str):
        body (CatalogV2UpdateEntryRequestBody):  Example: {'aliases': ['lawrence@incident.io',
            'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name':
            'Primary On-call', 'rank': 3}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2UpdateEntryResponseBody]
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
    body: CatalogV2UpdateEntryRequestBody,
) -> Optional[CatalogV2UpdateEntryResponseBody]:
    """UpdateEntry Catalog V2

     Updates an existing catalog entry.

    Args:
        id (str):
        body (CatalogV2UpdateEntryRequestBody):  Example: {'aliases': ['lawrence@incident.io',
            'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name':
            'Primary On-call', 'rank': 3}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2UpdateEntryResponseBody
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
