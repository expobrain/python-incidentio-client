from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.catalog_v2_update_type_schema_request_body import (
    CatalogV2UpdateTypeSchemaRequestBody,
)
from ...models.catalog_v2_update_type_schema_response_body import (
    CatalogV2UpdateTypeSchemaResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: CatalogV2UpdateTypeSchemaRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/catalog_types/{id}/actions/update_schema"

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[CatalogV2UpdateTypeSchemaResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CatalogV2UpdateTypeSchemaResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[CatalogV2UpdateTypeSchemaResponseBody]:
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
    json_body: CatalogV2UpdateTypeSchemaRequestBody,
) -> Response[CatalogV2UpdateTypeSchemaResponseBody]:
    """UpdateTypeSchema Catalog V2

     Update an existing catalog types schema, adding or removing attributes.

    Args:
        id (str):
        json_body (CatalogV2UpdateTypeSchemaRequestBody):  Example: {'attributes': [{'array':
            False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'tier'}], 'version':
            1}.

    Returns:
        Response[CatalogV2UpdateTypeSchemaResponseBody]
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
    json_body: CatalogV2UpdateTypeSchemaRequestBody,
) -> Optional[CatalogV2UpdateTypeSchemaResponseBody]:
    """UpdateTypeSchema Catalog V2

     Update an existing catalog types schema, adding or removing attributes.

    Args:
        id (str):
        json_body (CatalogV2UpdateTypeSchemaRequestBody):  Example: {'attributes': [{'array':
            False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'tier'}], 'version':
            1}.

    Returns:
        Response[CatalogV2UpdateTypeSchemaResponseBody]
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
    json_body: CatalogV2UpdateTypeSchemaRequestBody,
) -> Response[CatalogV2UpdateTypeSchemaResponseBody]:
    """UpdateTypeSchema Catalog V2

     Update an existing catalog types schema, adding or removing attributes.

    Args:
        id (str):
        json_body (CatalogV2UpdateTypeSchemaRequestBody):  Example: {'attributes': [{'array':
            False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'tier'}], 'version':
            1}.

    Returns:
        Response[CatalogV2UpdateTypeSchemaResponseBody]
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
    json_body: CatalogV2UpdateTypeSchemaRequestBody,
) -> Optional[CatalogV2UpdateTypeSchemaResponseBody]:
    """UpdateTypeSchema Catalog V2

     Update an existing catalog types schema, adding or removing attributes.

    Args:
        id (str):
        json_body (CatalogV2UpdateTypeSchemaRequestBody):  Example: {'attributes': [{'array':
            False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'tier'}], 'version':
            1}.

    Returns:
        Response[CatalogV2UpdateTypeSchemaResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
