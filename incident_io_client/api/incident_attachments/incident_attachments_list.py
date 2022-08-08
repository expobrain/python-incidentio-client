from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incident_attachments_list_resource_type import (
    IncidentAttachmentsListResourceType,
)
from ...models.incident_attachments_list_response_body import (
    IncidentAttachmentsListResponseBody,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    external_id: str,
    resource_type: IncidentAttachmentsListResourceType,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/incident_attachments"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["external_id"] = external_id

    json_resource_type = resource_type.value

    params["resource_type"] = json_resource_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncidentAttachmentsListResponseBody]:
    if response.status_code == 200:
        response_200 = IncidentAttachmentsListResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentAttachmentsListResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    external_id: str,
    resource_type: IncidentAttachmentsListResourceType,
) -> Response[IncidentAttachmentsListResponseBody]:
    """List Incident Attachments

     List all incident attachements for an external resouce

    Args:
        external_id (str):
        resource_type (IncidentAttachmentsListResourceType):

    Returns:
        Response[IncidentAttachmentsListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        external_id=external_id,
        resource_type=resource_type,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    external_id: str,
    resource_type: IncidentAttachmentsListResourceType,
) -> Optional[IncidentAttachmentsListResponseBody]:
    """List Incident Attachments

     List all incident attachements for an external resouce

    Args:
        external_id (str):
        resource_type (IncidentAttachmentsListResourceType):

    Returns:
        Response[IncidentAttachmentsListResponseBody]
    """

    return sync_detailed(
        client=client,
        external_id=external_id,
        resource_type=resource_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    external_id: str,
    resource_type: IncidentAttachmentsListResourceType,
) -> Response[IncidentAttachmentsListResponseBody]:
    """List Incident Attachments

     List all incident attachements for an external resouce

    Args:
        external_id (str):
        resource_type (IncidentAttachmentsListResourceType):

    Returns:
        Response[IncidentAttachmentsListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        external_id=external_id,
        resource_type=resource_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    external_id: str,
    resource_type: IncidentAttachmentsListResourceType,
) -> Optional[IncidentAttachmentsListResponseBody]:
    """List Incident Attachments

     List all incident attachements for an external resouce

    Args:
        external_id (str):
        resource_type (IncidentAttachmentsListResourceType):

    Returns:
        Response[IncidentAttachmentsListResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            external_id=external_id,
            resource_type=resource_type,
        )
    ).parsed
