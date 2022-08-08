from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incident_attachments_create_request_body import (
    IncidentAttachmentsCreateRequestBody,
)
from ...models.incident_attachments_create_response_body import (
    IncidentAttachmentsCreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: IncidentAttachmentsCreateRequestBody,
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
) -> Optional[IncidentAttachmentsCreateResponseBody]:
    if response.status_code == 201:
        response_201 = IncidentAttachmentsCreateResponseBody.from_dict(response.json())

        return response_201
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[IncidentAttachmentsCreateResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: IncidentAttachmentsCreateRequestBody,
) -> Response[IncidentAttachmentsCreateResponseBody]:
    """Create Incident Attachments

     Attaches an external resource to an incident

    Args:
        json_body (IncidentAttachmentsCreateRequestBody):  Example: {'incident_id': 'Omnis ut.',
            'resource': {'external_id': '123', 'resource_type': 'pager_duty_incident'}}.

    Returns:
        Response[IncidentAttachmentsCreateResponseBody]
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
    json_body: IncidentAttachmentsCreateRequestBody,
) -> Optional[IncidentAttachmentsCreateResponseBody]:
    """Create Incident Attachments

     Attaches an external resource to an incident

    Args:
        json_body (IncidentAttachmentsCreateRequestBody):  Example: {'incident_id': 'Omnis ut.',
            'resource': {'external_id': '123', 'resource_type': 'pager_duty_incident'}}.

    Returns:
        Response[IncidentAttachmentsCreateResponseBody]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: IncidentAttachmentsCreateRequestBody,
) -> Response[IncidentAttachmentsCreateResponseBody]:
    """Create Incident Attachments

     Attaches an external resource to an incident

    Args:
        json_body (IncidentAttachmentsCreateRequestBody):  Example: {'incident_id': 'Omnis ut.',
            'resource': {'external_id': '123', 'resource_type': 'pager_duty_incident'}}.

    Returns:
        Response[IncidentAttachmentsCreateResponseBody]
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
    json_body: IncidentAttachmentsCreateRequestBody,
) -> Optional[IncidentAttachmentsCreateResponseBody]:
    """Create Incident Attachments

     Attaches an external resource to an incident

    Args:
        json_body (IncidentAttachmentsCreateRequestBody):  Example: {'incident_id': 'Omnis ut.',
            'resource': {'external_id': '123', 'resource_type': 'pager_duty_incident'}}.

    Returns:
        Response[IncidentAttachmentsCreateResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
