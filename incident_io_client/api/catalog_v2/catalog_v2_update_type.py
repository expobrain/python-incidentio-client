from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_v2_update_type_request_body import CatalogV2UpdateTypeRequestBody
from ...models.catalog_v2_update_type_response_body import (
    CatalogV2UpdateTypeResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: CatalogV2UpdateTypeRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/v2/catalog_types/{id}".format(
            id=id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CatalogV2UpdateTypeResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CatalogV2UpdateTypeResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CatalogV2UpdateTypeResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogV2UpdateTypeRequestBody,
) -> Response[CatalogV2UpdateTypeResponseBody]:
    """UpdateType Catalog V2

     Updates an existing catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        id (str):
        body (CatalogV2UpdateTypeRequestBody):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['issue-tracker'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2UpdateTypeResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogV2UpdateTypeRequestBody,
) -> Optional[CatalogV2UpdateTypeResponseBody]:
    """UpdateType Catalog V2

     Updates an existing catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        id (str):
        body (CatalogV2UpdateTypeRequestBody):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['issue-tracker'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2UpdateTypeResponseBody
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogV2UpdateTypeRequestBody,
) -> Response[CatalogV2UpdateTypeResponseBody]:
    """UpdateType Catalog V2

     Updates an existing catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        id (str):
        body (CatalogV2UpdateTypeRequestBody):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['issue-tracker'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2UpdateTypeResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogV2UpdateTypeRequestBody,
) -> Optional[CatalogV2UpdateTypeResponseBody]:
    """UpdateType Catalog V2

     Updates an existing catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        id (str):
        body (CatalogV2UpdateTypeRequestBody):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['issue-tracker'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2UpdateTypeResponseBody
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
