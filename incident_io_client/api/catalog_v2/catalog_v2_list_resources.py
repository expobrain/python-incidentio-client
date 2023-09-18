from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.catalog_v2_list_resources_response_body import (
    CatalogV2ListResourcesResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/catalog_resources"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[CatalogV2ListResourcesResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CatalogV2ListResourcesResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CatalogV2ListResourcesResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[CatalogV2ListResourcesResponseBody]:
    """ListResources Catalog V2

     List available engine resources for the catalog.

    A resource represents a type of data that can be held within the catalog, so this
    endpoint can be used to see what attribute types can be used when updating the
    schema of a catalog type.

    Returns:
        Response[CatalogV2ListResourcesResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[CatalogV2ListResourcesResponseBody]:
    """ListResources Catalog V2

     List available engine resources for the catalog.

    A resource represents a type of data that can be held within the catalog, so this
    endpoint can be used to see what attribute types can be used when updating the
    schema of a catalog type.

    Returns:
        Response[CatalogV2ListResourcesResponseBody]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[CatalogV2ListResourcesResponseBody]:
    """ListResources Catalog V2

     List available engine resources for the catalog.

    A resource represents a type of data that can be held within the catalog, so this
    endpoint can be used to see what attribute types can be used when updating the
    schema of a catalog type.

    Returns:
        Response[CatalogV2ListResourcesResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[CatalogV2ListResourcesResponseBody]:
    """ListResources Catalog V2

     List available engine resources for the catalog.

    A resource represents a type of data that can be held within the catalog, so this
    endpoint can be used to see what attribute types can be used when updating the
    schema of a catalog type.

    Returns:
        Response[CatalogV2ListResourcesResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
