from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.catalog_v2_create_type_request_body import CatalogV2CreateTypeRequestBody
from ...models.catalog_v2_create_type_response_body import (
    CatalogV2CreateTypeResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CatalogV2CreateTypeRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/catalog_types"

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


def _parse_response(*, response: httpx.Response) -> Optional[CatalogV2CreateTypeResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CatalogV2CreateTypeResponseBody.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[CatalogV2CreateTypeResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CatalogV2CreateTypeRequestBody,
) -> Response[CatalogV2CreateTypeResponseBody]:
    """CreateType Catalog V2

     Create a catalog type.

    Args:
        json_body (CatalogV2CreateTypeRequestBody):  Example: {'color': 'slate', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'box', 'name':
            'Kubernetes Cluster', 'ranked': True, 'semantic_type': 'custom'}.

    Returns:
        Response[CatalogV2CreateTypeResponseBody]
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
    json_body: CatalogV2CreateTypeRequestBody,
) -> Optional[CatalogV2CreateTypeResponseBody]:
    """CreateType Catalog V2

     Create a catalog type.

    Args:
        json_body (CatalogV2CreateTypeRequestBody):  Example: {'color': 'slate', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'box', 'name':
            'Kubernetes Cluster', 'ranked': True, 'semantic_type': 'custom'}.

    Returns:
        Response[CatalogV2CreateTypeResponseBody]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CatalogV2CreateTypeRequestBody,
) -> Response[CatalogV2CreateTypeResponseBody]:
    """CreateType Catalog V2

     Create a catalog type.

    Args:
        json_body (CatalogV2CreateTypeRequestBody):  Example: {'color': 'slate', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'box', 'name':
            'Kubernetes Cluster', 'ranked': True, 'semantic_type': 'custom'}.

    Returns:
        Response[CatalogV2CreateTypeResponseBody]
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
    json_body: CatalogV2CreateTypeRequestBody,
) -> Optional[CatalogV2CreateTypeResponseBody]:
    """CreateType Catalog V2

     Create a catalog type.

    Args:
        json_body (CatalogV2CreateTypeRequestBody):  Example: {'color': 'slate', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'box', 'name':
            'Kubernetes Cluster', 'ranked': True, 'semantic_type': 'custom'}.

    Returns:
        Response[CatalogV2CreateTypeResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
