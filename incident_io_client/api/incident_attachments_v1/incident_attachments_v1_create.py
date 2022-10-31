from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incident_attachments_v1_create_request_body import (
    IncidentAttachmentsV1CreateRequestBody,
)
from ...models.incident_attachments_v1_create_response_body import (
    IncidentAttachmentsV1CreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: IncidentAttachmentsV1CreateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/incident_attachments"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[IncidentAttachmentsV1CreateResponseBody]:
    if response.status_code == 201:
        response_201 = IncidentAttachmentsV1CreateResponseBody.from_dict(response.json())

        return response_201
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[IncidentAttachmentsV1CreateResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: IncidentAttachmentsV1CreateRequestBody,
) -> Response[IncidentAttachmentsV1CreateResponseBody]:
    """Create Incident Attachments V1

     Attaches an external resource to an incident

    Args:
        json_body (IncidentAttachmentsV1CreateRequestBody):  Example: {'incident_id':
            '01FDAG4SAP5TYPT98WGR2N7W91', 'resource': {'external_id': '123', 'resource_type':
            'pager_duty_incident'}}.

    Returns:
        Response[IncidentAttachmentsV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: IncidentAttachmentsV1CreateRequestBody,
) -> Optional[IncidentAttachmentsV1CreateResponseBody]:
    """Create Incident Attachments V1

     Attaches an external resource to an incident

    Args:
        json_body (IncidentAttachmentsV1CreateRequestBody):  Example: {'incident_id':
            '01FDAG4SAP5TYPT98WGR2N7W91', 'resource': {'external_id': '123', 'resource_type':
            'pager_duty_incident'}}.

    Returns:
        Response[IncidentAttachmentsV1CreateResponseBody]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: IncidentAttachmentsV1CreateRequestBody,
) -> Response[IncidentAttachmentsV1CreateResponseBody]:
    """Create Incident Attachments V1

     Attaches an external resource to an incident

    Args:
        json_body (IncidentAttachmentsV1CreateRequestBody):  Example: {'incident_id':
            '01FDAG4SAP5TYPT98WGR2N7W91', 'resource': {'external_id': '123', 'resource_type':
            'pager_duty_incident'}}.

    Returns:
        Response[IncidentAttachmentsV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: IncidentAttachmentsV1CreateRequestBody,
) -> Optional[IncidentAttachmentsV1CreateResponseBody]:
    """Create Incident Attachments V1

     Attaches an external resource to an incident

    Args:
        json_body (IncidentAttachmentsV1CreateRequestBody):  Example: {'incident_id':
            '01FDAG4SAP5TYPT98WGR2N7W91', 'resource': {'external_id': '123', 'resource_type':
            'pager_duty_incident'}}.

    Returns:
        Response[IncidentAttachmentsV1CreateResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
