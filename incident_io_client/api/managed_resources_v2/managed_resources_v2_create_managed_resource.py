from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.managed_resources_v2_create_managed_resource_request_body import (
    ManagedResourcesV2CreateManagedResourceRequestBody,
)
from ...models.managed_resources_v2_create_managed_resource_response_body import (
    ManagedResourcesV2CreateManagedResourceResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: ManagedResourcesV2CreateManagedResourceRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/managed_resources",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ManagedResourcesV2CreateManagedResourceResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ManagedResourcesV2CreateManagedResourceResponseBody.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ManagedResourcesV2CreateManagedResourceResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ManagedResourcesV2CreateManagedResourceRequestBody,
) -> Response[ManagedResourcesV2CreateManagedResourceResponseBody]:
    """CreateManagedResource Managed Resources V2

     Called by external providers such as Terraform, this can 'claim' an incident.io resource as being
    managed externally.

    Args:
        body (ManagedResourcesV2CreateManagedResourceRequestBody):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'resource_id': 'abc123', 'resource_type':
            'schedule'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ManagedResourcesV2CreateManagedResourceResponseBody]
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
    body: ManagedResourcesV2CreateManagedResourceRequestBody,
) -> Optional[ManagedResourcesV2CreateManagedResourceResponseBody]:
    """CreateManagedResource Managed Resources V2

     Called by external providers such as Terraform, this can 'claim' an incident.io resource as being
    managed externally.

    Args:
        body (ManagedResourcesV2CreateManagedResourceRequestBody):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'resource_id': 'abc123', 'resource_type':
            'schedule'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ManagedResourcesV2CreateManagedResourceResponseBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ManagedResourcesV2CreateManagedResourceRequestBody,
) -> Response[ManagedResourcesV2CreateManagedResourceResponseBody]:
    """CreateManagedResource Managed Resources V2

     Called by external providers such as Terraform, this can 'claim' an incident.io resource as being
    managed externally.

    Args:
        body (ManagedResourcesV2CreateManagedResourceRequestBody):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'resource_id': 'abc123', 'resource_type':
            'schedule'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ManagedResourcesV2CreateManagedResourceResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ManagedResourcesV2CreateManagedResourceRequestBody,
) -> Optional[ManagedResourcesV2CreateManagedResourceResponseBody]:
    """CreateManagedResource Managed Resources V2

     Called by external providers such as Terraform, this can 'claim' an incident.io resource as being
    managed externally.

    Args:
        body (ManagedResourcesV2CreateManagedResourceRequestBody):  Example: {'annotations':
            {'incident.io/terraform/version': '3.0.0'}, 'resource_id': 'abc123', 'resource_type':
            'schedule'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ManagedResourcesV2CreateManagedResourceResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
