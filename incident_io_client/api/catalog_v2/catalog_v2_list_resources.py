from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_v2_list_resources_response_body import (
    CatalogV2ListResourcesResponseBody,
)
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/catalog_resources",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CatalogV2ListResourcesResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CatalogV2ListResourcesResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CatalogV2ListResourcesResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CatalogV2ListResourcesResponseBody]:
    """ListResources Catalog V2

     List available engine resources for the catalog.

    A resource represents a type of data that can be held within the catalog, so this
    endpoint can be used to see what attribute types can be used when updating the
    schema of a catalog type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2ListResourcesResponseBody]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CatalogV2ListResourcesResponseBody]:
    """ListResources Catalog V2

     List available engine resources for the catalog.

    A resource represents a type of data that can be held within the catalog, so this
    endpoint can be used to see what attribute types can be used when updating the
    schema of a catalog type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2ListResourcesResponseBody
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CatalogV2ListResourcesResponseBody]:
    """ListResources Catalog V2

     List available engine resources for the catalog.

    A resource represents a type of data that can be held within the catalog, so this
    endpoint can be used to see what attribute types can be used when updating the
    schema of a catalog type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2ListResourcesResponseBody]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CatalogV2ListResourcesResponseBody]:
    """ListResources Catalog V2

     List available engine resources for the catalog.

    A resource represents a type of data that can be held within the catalog, so this
    endpoint can be used to see what attribute types can be used when updating the
    schema of a catalog type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2ListResourcesResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
