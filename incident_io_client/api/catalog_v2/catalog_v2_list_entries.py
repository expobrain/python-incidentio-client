from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_v2_list_entries_response_body import (
    CatalogV2ListEntriesResponseBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    catalog_type_id: str,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["catalog_type_id"] = catalog_type_id

    params["page_size"] = page_size

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/catalog_entries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CatalogV2ListEntriesResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CatalogV2ListEntriesResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CatalogV2ListEntriesResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    catalog_type_id: str,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Response[CatalogV2ListEntriesResponseBody]:
    """ListEntries Catalog V2

     List entries for a catalog type.

    Args:
        catalog_type_id (str):
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2ListEntriesResponseBody]
    """

    kwargs = _get_kwargs(
        catalog_type_id=catalog_type_id,
        page_size=page_size,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    catalog_type_id: str,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Optional[CatalogV2ListEntriesResponseBody]:
    """ListEntries Catalog V2

     List entries for a catalog type.

    Args:
        catalog_type_id (str):
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2ListEntriesResponseBody
    """

    return sync_detailed(
        client=client,
        catalog_type_id=catalog_type_id,
        page_size=page_size,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    catalog_type_id: str,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Response[CatalogV2ListEntriesResponseBody]:
    """ListEntries Catalog V2

     List entries for a catalog type.

    Args:
        catalog_type_id (str):
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2ListEntriesResponseBody]
    """

    kwargs = _get_kwargs(
        catalog_type_id=catalog_type_id,
        page_size=page_size,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    catalog_type_id: str,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Optional[CatalogV2ListEntriesResponseBody]:
    """ListEntries Catalog V2

     List entries for a catalog type.

    Args:
        catalog_type_id (str):
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2ListEntriesResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            catalog_type_id=catalog_type_id,
            page_size=page_size,
            after=after,
        )
    ).parsed
