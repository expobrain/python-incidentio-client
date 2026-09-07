from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_create_type_payload_v2 import CatalogCreateTypePayloadV2
from ...models.catalog_create_type_result_v2 import CatalogCreateTypeResultV2
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CatalogCreateTypePayloadV2,
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
) -> Optional[Union[CatalogCreateTypeResultV2, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CatalogCreateTypeResultV2.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 405:
        response_405 = ErrorResponse.from_dict(response.json())

        return response_405
    if response.status_code == 406:
        response_406 = ErrorResponse.from_dict(response.json())

        return response_406
    if response.status_code == 408:
        response_408 = ErrorResponse.from_dict(response.json())

        return response_408
    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409
    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412
    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413
    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422
    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CatalogCreateTypeResultV2, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogCreateTypePayloadV2,
) -> Response[Union[CatalogCreateTypeResultV2, ErrorResponse]]:
    """CreateType Catalog V2

     Create a catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        body (CatalogCreateTypePayloadV2):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['customer'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog', 'type_name':
            'Custom["BackstageGroup"]'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogCreateTypeResultV2, ErrorResponse]]
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
    body: CatalogCreateTypePayloadV2,
) -> Optional[Union[CatalogCreateTypeResultV2, ErrorResponse]]:
    """CreateType Catalog V2

     Create a catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        body (CatalogCreateTypePayloadV2):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['customer'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog', 'type_name':
            'Custom["BackstageGroup"]'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CatalogCreateTypeResultV2, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogCreateTypePayloadV2,
) -> Response[Union[CatalogCreateTypeResultV2, ErrorResponse]]:
    """CreateType Catalog V2

     Create a catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        body (CatalogCreateTypePayloadV2):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['customer'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog', 'type_name':
            'Custom["BackstageGroup"]'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogCreateTypeResultV2, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CatalogCreateTypePayloadV2,
) -> Optional[Union[CatalogCreateTypeResultV2, ErrorResponse]]:
    """CreateType Catalog V2

     Create a catalog type. The schema must be updated using the UpdateTypeSchema endpoint.

    Args:
        body (CatalogCreateTypePayloadV2):  Example: {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'categories': ['customer'], 'color': 'yellow',
            'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon':
            'alert', 'name': 'Kubernetes Cluster', 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog', 'type_name':
            'Custom["BackstageGroup"]'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CatalogCreateTypeResultV2, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
