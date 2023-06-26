from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
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
    client: Client,
    json_body: CatalogV2UpdateEntryRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/catalog_entries/{id}"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CatalogV2UpdateEntryResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CatalogV2UpdateEntryResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CatalogV2UpdateEntryResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    json_body: CatalogV2UpdateEntryRequestBody,
) -> Response[CatalogV2UpdateEntryResponseBody]:
    """UpdateEntry Catalog V2

     Updates an existing catalog entry.

    Args:
        id (str):
        json_body (CatalogV2UpdateEntryRequestBody):  Example: {'aliases':
            ['lawrence@incident.io', 'lawrence'], 'attribute_values': {'abc123': {'array_value':
            [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}}, 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank': 3}.

    Returns:
        Response[CatalogV2UpdateEntryResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: CatalogV2UpdateEntryRequestBody,
) -> Optional[CatalogV2UpdateEntryResponseBody]:
    """UpdateEntry Catalog V2

     Updates an existing catalog entry.

    Args:
        id (str):
        json_body (CatalogV2UpdateEntryRequestBody):  Example: {'aliases':
            ['lawrence@incident.io', 'lawrence'], 'attribute_values': {'abc123': {'array_value':
            [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}}, 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank': 3}.

    Returns:
        Response[CatalogV2UpdateEntryResponseBody]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: CatalogV2UpdateEntryRequestBody,
) -> Response[CatalogV2UpdateEntryResponseBody]:
    """UpdateEntry Catalog V2

     Updates an existing catalog entry.

    Args:
        id (str):
        json_body (CatalogV2UpdateEntryRequestBody):  Example: {'aliases':
            ['lawrence@incident.io', 'lawrence'], 'attribute_values': {'abc123': {'array_value':
            [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}}, 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank': 3}.

    Returns:
        Response[CatalogV2UpdateEntryResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: CatalogV2UpdateEntryRequestBody,
) -> Optional[CatalogV2UpdateEntryResponseBody]:
    """UpdateEntry Catalog V2

     Updates an existing catalog entry.

    Args:
        id (str):
        json_body (CatalogV2UpdateEntryRequestBody):  Example: {'aliases':
            ['lawrence@incident.io', 'lawrence'], 'attribute_values': {'abc123': {'array_value':
            [{'literal': 'SEV123'}], 'value': {'literal': 'SEV123'}}}, 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'name': 'Primary On-call', 'rank': 3}.

    Returns:
        Response[CatalogV2UpdateEntryResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
