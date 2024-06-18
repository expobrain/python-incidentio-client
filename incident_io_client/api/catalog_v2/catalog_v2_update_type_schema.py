from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
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
    body: CatalogV2UpdateTypeSchemaRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/catalog_types/{id}/actions/update_schema".format(
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
) -> Optional[CatalogV2UpdateTypeSchemaResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CatalogV2UpdateTypeSchemaResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CatalogV2UpdateTypeSchemaResponseBody]:
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
    body: CatalogV2UpdateTypeSchemaRequestBody,
) -> Response[CatalogV2UpdateTypeSchemaResponseBody]:
    """UpdateTypeSchema Catalog V2

     Update an existing catalog types schema, adding or removing attributes.

    Updating the schema is handled separately from creating and updating types, so that you don't
    have to worry about dependencies between types. For example, if type A has an attribute that
    relies on type B, you would have to create type B first.

    By allowing the creation of types without a schema, they can be created in any order, but it
    means that you need to make a separate call to this endpoint to update the schema.

    Args:
        id (str):
        body (CatalogV2UpdateTypeSchemaRequestBody):  Example: {'attributes': [{'array': False,
            'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual',
            'name': 'tier', 'path': [{'attribute_id': 'abc123'}], 'type': 'Custom["Service"]'}],
            'version': 1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2UpdateTypeSchemaResponseBody]
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
    body: CatalogV2UpdateTypeSchemaRequestBody,
) -> Optional[CatalogV2UpdateTypeSchemaResponseBody]:
    """UpdateTypeSchema Catalog V2

     Update an existing catalog types schema, adding or removing attributes.

    Updating the schema is handled separately from creating and updating types, so that you don't
    have to worry about dependencies between types. For example, if type A has an attribute that
    relies on type B, you would have to create type B first.

    By allowing the creation of types without a schema, they can be created in any order, but it
    means that you need to make a separate call to this endpoint to update the schema.

    Args:
        id (str):
        body (CatalogV2UpdateTypeSchemaRequestBody):  Example: {'attributes': [{'array': False,
            'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual',
            'name': 'tier', 'path': [{'attribute_id': 'abc123'}], 'type': 'Custom["Service"]'}],
            'version': 1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2UpdateTypeSchemaResponseBody
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
    body: CatalogV2UpdateTypeSchemaRequestBody,
) -> Response[CatalogV2UpdateTypeSchemaResponseBody]:
    """UpdateTypeSchema Catalog V2

     Update an existing catalog types schema, adding or removing attributes.

    Updating the schema is handled separately from creating and updating types, so that you don't
    have to worry about dependencies between types. For example, if type A has an attribute that
    relies on type B, you would have to create type B first.

    By allowing the creation of types without a schema, they can be created in any order, but it
    means that you need to make a separate call to this endpoint to update the schema.

    Args:
        id (str):
        body (CatalogV2UpdateTypeSchemaRequestBody):  Example: {'attributes': [{'array': False,
            'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual',
            'name': 'tier', 'path': [{'attribute_id': 'abc123'}], 'type': 'Custom["Service"]'}],
            'version': 1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogV2UpdateTypeSchemaResponseBody]
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
    body: CatalogV2UpdateTypeSchemaRequestBody,
) -> Optional[CatalogV2UpdateTypeSchemaResponseBody]:
    """UpdateTypeSchema Catalog V2

     Update an existing catalog types schema, adding or removing attributes.

    Updating the schema is handled separately from creating and updating types, so that you don't
    have to worry about dependencies between types. For example, if type A has an attribute that
    relies on type B, you would have to create type B first.

    By allowing the creation of types without a schema, they can be created in any order, but it
    means that you need to make a separate call to this endpoint to update the schema.

    Args:
        id (str):
        body (CatalogV2UpdateTypeSchemaRequestBody):  Example: {'attributes': [{'array': False,
            'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual',
            'name': 'tier', 'path': [{'attribute_id': 'abc123'}], 'type': 'Custom["Service"]'}],
            'version': 1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogV2UpdateTypeSchemaResponseBody
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
