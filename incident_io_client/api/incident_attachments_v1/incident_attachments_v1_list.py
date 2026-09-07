from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.incident_attachments_list_result_v1 import (
    IncidentAttachmentsListResultV1,
)
from ...models.incident_attachments_v1_list_resource_type import (
    IncidentAttachmentsV1ListResourceType,
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
) -> Optional[Union[ErrorResponse, IncidentAttachmentsListResultV1]]:
    if response.status_code == 200:
        response_200 = IncidentAttachmentsListResultV1.from_dict(response.json())

        return response_200
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
) -> Response[Union[ErrorResponse, IncidentAttachmentsListResultV1]]:
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
) -> Response[Union[ErrorResponse, IncidentAttachmentsListResultV1]]:
    """List Incident Attachments V1

     List all incident attachments for a given external resource or incident. You must provide either a
    specific incident ID or a specific external resource type and external ID.

    Args:
        incident_id (Union[Unset, str]):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        external_id (Union[Unset, str]): ID of the resource in the external system Example: 123.
        resource_type (Union[Unset, IncidentAttachmentsV1ListResourceType]): E.g. PagerDuty: the
            external system that holds the resource Example: pager_duty_incident.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, IncidentAttachmentsListResultV1]]
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
) -> Optional[Union[ErrorResponse, IncidentAttachmentsListResultV1]]:
    """List Incident Attachments V1

     List all incident attachments for a given external resource or incident. You must provide either a
    specific incident ID or a specific external resource type and external ID.

    Args:
        incident_id (Union[Unset, str]):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        external_id (Union[Unset, str]): ID of the resource in the external system Example: 123.
        resource_type (Union[Unset, IncidentAttachmentsV1ListResourceType]): E.g. PagerDuty: the
            external system that holds the resource Example: pager_duty_incident.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, IncidentAttachmentsListResultV1]
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
) -> Response[Union[ErrorResponse, IncidentAttachmentsListResultV1]]:
    """List Incident Attachments V1

     List all incident attachments for a given external resource or incident. You must provide either a
    specific incident ID or a specific external resource type and external ID.

    Args:
        incident_id (Union[Unset, str]):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        external_id (Union[Unset, str]): ID of the resource in the external system Example: 123.
        resource_type (Union[Unset, IncidentAttachmentsV1ListResourceType]): E.g. PagerDuty: the
            external system that holds the resource Example: pager_duty_incident.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, IncidentAttachmentsListResultV1]]
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
) -> Optional[Union[ErrorResponse, IncidentAttachmentsListResultV1]]:
    """List Incident Attachments V1

     List all incident attachments for a given external resource or incident. You must provide either a
    specific incident ID or a specific external resource type and external ID.

    Args:
        incident_id (Union[Unset, str]):  Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        external_id (Union[Unset, str]): ID of the resource in the external system Example: 123.
        resource_type (Union[Unset, IncidentAttachmentsV1ListResourceType]): E.g. PagerDuty: the
            external system that holds the resource Example: pager_duty_incident.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, IncidentAttachmentsListResultV1]
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            external_id=external_id,
            resource_type=resource_type,
        )
    ).parsed
