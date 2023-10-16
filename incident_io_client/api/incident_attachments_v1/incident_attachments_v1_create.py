from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_attachments_v1_create_request_body import (
    IncidentAttachmentsV1CreateRequestBody,
)
from ...models.incident_attachments_v1_create_response_body import (
    IncidentAttachmentsV1CreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    json_body: IncidentAttachmentsV1CreateRequestBody,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v1/incident_attachments",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentAttachmentsV1CreateResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = IncidentAttachmentsV1CreateResponseBody.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentAttachmentsV1CreateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentAttachmentsV1CreateRequestBody,
) -> Response[IncidentAttachmentsV1CreateResponseBody]:
    """Create Incident Attachments V1

     Attaches an external resource to an incident

    Args:
        json_body (IncidentAttachmentsV1CreateRequestBody):  Example: {'incident_id':
            '01FDAG4SAP5TYPT98WGR2N7W91', 'resource': {'external_id': '123', 'resource_type':
            'pager_duty_incident'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentAttachmentsV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentAttachmentsV1CreateRequestBody,
) -> Optional[IncidentAttachmentsV1CreateResponseBody]:
    """Create Incident Attachments V1

     Attaches an external resource to an incident

    Args:
        json_body (IncidentAttachmentsV1CreateRequestBody):  Example: {'incident_id':
            '01FDAG4SAP5TYPT98WGR2N7W91', 'resource': {'external_id': '123', 'resource_type':
            'pager_duty_incident'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentAttachmentsV1CreateResponseBody
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentAttachmentsV1CreateRequestBody,
) -> Response[IncidentAttachmentsV1CreateResponseBody]:
    """Create Incident Attachments V1

     Attaches an external resource to an incident

    Args:
        json_body (IncidentAttachmentsV1CreateRequestBody):  Example: {'incident_id':
            '01FDAG4SAP5TYPT98WGR2N7W91', 'resource': {'external_id': '123', 'resource_type':
            'pager_duty_incident'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentAttachmentsV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentAttachmentsV1CreateRequestBody,
) -> Optional[IncidentAttachmentsV1CreateResponseBody]:
    """Create Incident Attachments V1

     Attaches an external resource to an incident

    Args:
        json_body (IncidentAttachmentsV1CreateRequestBody):  Example: {'incident_id':
            '01FDAG4SAP5TYPT98WGR2N7W91', 'resource': {'external_id': '123', 'resource_type':
            'pager_duty_incident'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentAttachmentsV1CreateResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
