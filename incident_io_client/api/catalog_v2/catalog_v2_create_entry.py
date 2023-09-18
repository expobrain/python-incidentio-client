from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.catalog_v2_create_entry_request_body import (
    CatalogV2CreateEntryRequestBody,
)
from ...models.catalog_v2_create_entry_response_body import (
    CatalogV2CreateEntryResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CatalogV2CreateEntryRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/catalog_entries"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CatalogV2CreateEntryResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CatalogV2CreateEntryResponseBody.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[CatalogV2CreateEntryResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CatalogV2CreateEntryRequestBody,
) -> Response[CatalogV2CreateEntryResponseBody]:
    """CreateEntry Catalog V2

     Create an entry within the catalog. We support a maximum of 50,000 entries per type.

    Args:
        json_body (CatalogV2CreateEntryRequestBody):  Example: {'aliases':
            ['lawrence@incident.io', 'lawrence'], 'attribute_values': {'abc123': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank':
            3}.

    Returns:
        Response[CatalogV2CreateEntryResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: CatalogV2CreateEntryRequestBody,
) -> Optional[CatalogV2CreateEntryResponseBody]:
    """CreateEntry Catalog V2

     Create an entry within the catalog. We support a maximum of 50,000 entries per type.

    Args:
        json_body (CatalogV2CreateEntryRequestBody):  Example: {'aliases':
            ['lawrence@incident.io', 'lawrence'], 'attribute_values': {'abc123': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank':
            3}.

    Returns:
        Response[CatalogV2CreateEntryResponseBody]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CatalogV2CreateEntryRequestBody,
) -> Response[CatalogV2CreateEntryResponseBody]:
    """CreateEntry Catalog V2

     Create an entry within the catalog. We support a maximum of 50,000 entries per type.

    Args:
        json_body (CatalogV2CreateEntryRequestBody):  Example: {'aliases':
            ['lawrence@incident.io', 'lawrence'], 'attribute_values': {'abc123': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank':
            3}.

    Returns:
        Response[CatalogV2CreateEntryResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CatalogV2CreateEntryRequestBody,
) -> Optional[CatalogV2CreateEntryResponseBody]:
    """CreateEntry Catalog V2

     Create an entry within the catalog. We support a maximum of 50,000 entries per type.

    Args:
        json_body (CatalogV2CreateEntryRequestBody):  Example: {'aliases':
            ['lawrence@incident.io', 'lawrence'], 'attribute_values': {'abc123': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank':
            3}.

    Returns:
        Response[CatalogV2CreateEntryResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
