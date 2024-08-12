from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_v2_create_entry_request_body import (
    CatalogV2CreateEntryRequestBody,
)
from ...models.catalog_v2_create_entry_response_body import (
    CatalogV2CreateEntryResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: CatalogV2CreateEntryRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/catalog_entries",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CatalogV2CreateEntryResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CatalogV2CreateEntryResponseBody.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CatalogV2CreateEntryResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogV2CreateEntryRequestBody,
) -> Response[CatalogV2CreateEntryResponseBody]:
    """CreateEntry Catalog V2

     Create an entry within the catalog. We support a maximum of 50,000 entries per type.

    If you call this API with a payload where the external_id and catalog_type_id match an existing
    entry, the existing entry will be updated.

    Args:
        body (CatalogV2CreateEntryRequestBody):  Example: {'aliases': ['lawrence@incident.io',
            'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank': 3}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2CreateEntryResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogV2CreateEntryRequestBody,
) -> Optional[CatalogV2CreateEntryResponseBody]:
    """CreateEntry Catalog V2

     Create an entry within the catalog. We support a maximum of 50,000 entries per type.

    If you call this API with a payload where the external_id and catalog_type_id match an existing
    entry, the existing entry will be updated.

    Args:
        body (CatalogV2CreateEntryRequestBody):  Example: {'aliases': ['lawrence@incident.io',
            'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank': 3}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2CreateEntryResponseBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogV2CreateEntryRequestBody,
) -> Response[CatalogV2CreateEntryResponseBody]:
    """CreateEntry Catalog V2

     Create an entry within the catalog. We support a maximum of 50,000 entries per type.

    If you call this API with a payload where the external_id and catalog_type_id match an existing
    entry, the existing entry will be updated.

    Args:
        body (CatalogV2CreateEntryRequestBody):  Example: {'aliases': ['lawrence@incident.io',
            'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank': 3}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2CreateEntryResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogV2CreateEntryRequestBody,
) -> Optional[CatalogV2CreateEntryResponseBody]:
    """CreateEntry Catalog V2

     Create an entry within the catalog. We support a maximum of 50,000 entries per type.

    If you call this API with a payload where the external_id and catalog_type_id match an existing
    entry, the existing entry will be updated.

    Args:
        body (CatalogV2CreateEntryRequestBody):  Example: {'aliases': ['lawrence@incident.io',
            'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank': 3}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2CreateEntryResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
