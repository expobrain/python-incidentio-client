from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_v2_create_type_request_body import CatalogV2CreateTypeRequestBody
from ...models.catalog_v2_create_type_response_body import (
    CatalogV2CreateTypeResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: CatalogV2CreateTypeRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/catalog_types",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CatalogV2CreateTypeResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CatalogV2CreateTypeResponseBody.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CatalogV2CreateTypeResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogV2CreateTypeRequestBody,
) -> Response[CatalogV2CreateTypeResponseBody]:
    """CreateType Catalog V2

     Create a catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        body (CatalogV2CreateTypeRequestBody):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['issue-tracker'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog', 'type_name':
            'Custom["BackstageGroup"]'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2CreateTypeResponseBody]
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
    body: CatalogV2CreateTypeRequestBody,
) -> Optional[CatalogV2CreateTypeResponseBody]:
    """CreateType Catalog V2

     Create a catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        body (CatalogV2CreateTypeRequestBody):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['issue-tracker'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog', 'type_name':
            'Custom["BackstageGroup"]'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2CreateTypeResponseBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogV2CreateTypeRequestBody,
) -> Response[CatalogV2CreateTypeResponseBody]:
    """CreateType Catalog V2

     Create a catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        body (CatalogV2CreateTypeRequestBody):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['issue-tracker'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog', 'type_name':
            'Custom["BackstageGroup"]'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2CreateTypeResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogV2CreateTypeRequestBody,
) -> Optional[CatalogV2CreateTypeResponseBody]:
    """CreateType Catalog V2

     Create a catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        body (CatalogV2CreateTypeRequestBody):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['issue-tracker'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog', 'type_name':
            'Custom["BackstageGroup"]'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2CreateTypeResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
