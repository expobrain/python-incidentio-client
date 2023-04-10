from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.catalog_v2_update_type_request_body import CatalogV2UpdateTypeRequestBody
from ...models.catalog_v2_update_type_response_body import (
    CatalogV2UpdateTypeResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: CatalogV2UpdateTypeRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/catalog_types/{id}"

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


def _parse_response(*, response: httpx.Response) -> Optional[CatalogV2UpdateTypeResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CatalogV2UpdateTypeResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CatalogV2UpdateTypeResponseBody]:
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
    json_body: CatalogV2UpdateTypeRequestBody,
) -> Response[CatalogV2UpdateTypeResponseBody]:
    """UpdateType Catalog V2

     Updates an existing catalog type.

    Args:
        id (str):
        json_body (CatalogV2UpdateTypeRequestBody):  Example: {'color': 'slate', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'box', 'name':
            'Kubernetes Cluster', 'ranked': True, 'semantic_type': 'custom'}.

    Returns:
        Response[CatalogV2UpdateTypeResponseBody]
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
    json_body: CatalogV2UpdateTypeRequestBody,
) -> Optional[CatalogV2UpdateTypeResponseBody]:
    """UpdateType Catalog V2

     Updates an existing catalog type.

    Args:
        id (str):
        json_body (CatalogV2UpdateTypeRequestBody):  Example: {'color': 'slate', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'box', 'name':
            'Kubernetes Cluster', 'ranked': True, 'semantic_type': 'custom'}.

    Returns:
        Response[CatalogV2UpdateTypeResponseBody]
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
    json_body: CatalogV2UpdateTypeRequestBody,
) -> Response[CatalogV2UpdateTypeResponseBody]:
    """UpdateType Catalog V2

     Updates an existing catalog type.

    Args:
        id (str):
        json_body (CatalogV2UpdateTypeRequestBody):  Example: {'color': 'slate', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'box', 'name':
            'Kubernetes Cluster', 'ranked': True, 'semantic_type': 'custom'}.

    Returns:
        Response[CatalogV2UpdateTypeResponseBody]
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
    json_body: CatalogV2UpdateTypeRequestBody,
) -> Optional[CatalogV2UpdateTypeResponseBody]:
    """UpdateType Catalog V2

     Updates an existing catalog type.

    Args:
        id (str):
        json_body (CatalogV2UpdateTypeRequestBody):  Example: {'color': 'slate', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'box', 'name':
            'Kubernetes Cluster', 'ranked': True, 'semantic_type': 'custom'}.

    Returns:
        Response[CatalogV2UpdateTypeResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
