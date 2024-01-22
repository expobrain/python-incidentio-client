from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_attachments_v1_list_resource_type import (
    IncidentAttachmentsV1ListResourceType,
)
from ...models.incident_attachments_v1_list_response_body import (
    IncidentAttachmentsV1ListResponseBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    incident_id: Union[Unset, str] = UNSET,
    external_id: Union[Unset, str] = UNSET,
    resource_type: Union[Unset, IncidentAttachmentsV1ListResourceType] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["incident_id"] = incident_id

    params["external_id"] = external_id

    json_resource_type: Union[Unset, str] = UNSET
    if not isinstance(resource_type, Unset):
        json_resource_type = resource_type.value

    params["resource_type"] = json_resource_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/incident_attachments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentAttachmentsV1ListResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentAttachmentsV1ListResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentAttachmentsV1ListResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    external_id: Union[Unset, str] = UNSET,
    resource_type: Union[Unset, IncidentAttachmentsV1ListResourceType] = UNSET,
) -> Response[IncidentAttachmentsV1ListResponseBody]:
    """List Incident Attachments V1

     List all incident attachements for a given external resource or incident. You must provide either a
    specific incident ID or a specific external resource type and external ID.

    Args:
        incident_id (Union[Unset, str]):
        external_id (Union[Unset, str]):
        resource_type (Union[Unset, IncidentAttachmentsV1ListResourceType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentAttachmentsV1ListResponseBody]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        external_id=external_id,
        resource_type=resource_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    external_id: Union[Unset, str] = UNSET,
    resource_type: Union[Unset, IncidentAttachmentsV1ListResourceType] = UNSET,
) -> Optional[IncidentAttachmentsV1ListResponseBody]:
    """List Incident Attachments V1

     List all incident attachements for a given external resource or incident. You must provide either a
    specific incident ID or a specific external resource type and external ID.

    Args:
        incident_id (Union[Unset, str]):
        external_id (Union[Unset, str]):
        resource_type (Union[Unset, IncidentAttachmentsV1ListResourceType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentAttachmentsV1ListResponseBody
    """

    return sync_detailed(
        client=client,
        incident_id=incident_id,
        external_id=external_id,
        resource_type=resource_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    external_id: Union[Unset, str] = UNSET,
    resource_type: Union[Unset, IncidentAttachmentsV1ListResourceType] = UNSET,
) -> Response[IncidentAttachmentsV1ListResponseBody]:
    """List Incident Attachments V1

     List all incident attachements for a given external resource or incident. You must provide either a
    specific incident ID or a specific external resource type and external ID.

    Args:
        incident_id (Union[Unset, str]):
        external_id (Union[Unset, str]):
        resource_type (Union[Unset, IncidentAttachmentsV1ListResourceType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentAttachmentsV1ListResponseBody]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        external_id=external_id,
        resource_type=resource_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    external_id: Union[Unset, str] = UNSET,
    resource_type: Union[Unset, IncidentAttachmentsV1ListResourceType] = UNSET,
) -> Optional[IncidentAttachmentsV1ListResponseBody]:
    """List Incident Attachments V1

     List all incident attachements for a given external resource or incident. You must provide either a
    specific incident ID or a specific external resource type and external ID.

    Args:
        incident_id (Union[Unset, str]):
        external_id (Union[Unset, str]):
        resource_type (Union[Unset, IncidentAttachmentsV1ListResourceType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentAttachmentsV1ListResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            external_id=external_id,
            resource_type=resource_type,
        )
    ).parsed
