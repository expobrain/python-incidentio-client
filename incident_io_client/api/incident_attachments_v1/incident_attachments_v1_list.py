from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.incident_attachments_v1_list_resource_type import (
    IncidentAttachmentsV1ListResourceType,
)
from ...models.incident_attachments_v1_list_response_body import (
    IncidentAttachmentsV1ListResponseBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    external_id: str,
    resource_type: IncidentAttachmentsV1ListResourceType,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/incident_attachments"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["incident_id"] = incident_id

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[IncidentAttachmentsV1ListResponseBody]:
    if response.status_code == 200:
        response_200 = IncidentAttachmentsV1ListResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[IncidentAttachmentsV1ListResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    external_id: str,
    resource_type: IncidentAttachmentsV1ListResourceType,
) -> Response[IncidentAttachmentsV1ListResponseBody]:
    """List Incident Attachments V1

     List all incident attachements for an external resouce

    Args:
        incident_id (Union[Unset, None, str]):
        external_id (str):
        resource_type (IncidentAttachmentsV1ListResourceType):

    Returns:
        Response[IncidentAttachmentsV1ListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        incident_id=incident_id,
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
    incident_id: Union[Unset, None, str] = UNSET,
    external_id: str,
    resource_type: IncidentAttachmentsV1ListResourceType,
) -> Optional[IncidentAttachmentsV1ListResponseBody]:
    """List Incident Attachments V1

     List all incident attachements for an external resouce

    Args:
        incident_id (Union[Unset, None, str]):
        external_id (str):
        resource_type (IncidentAttachmentsV1ListResourceType):

    Returns:
        Response[IncidentAttachmentsV1ListResponseBody]
    """

    return sync_detailed(
        client=client,
        incident_id=incident_id,
        external_id=external_id,
        resource_type=resource_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    external_id: str,
    resource_type: IncidentAttachmentsV1ListResourceType,
) -> Response[IncidentAttachmentsV1ListResponseBody]:
    """List Incident Attachments V1

     List all incident attachements for an external resouce

    Args:
        incident_id (Union[Unset, None, str]):
        external_id (str):
        resource_type (IncidentAttachmentsV1ListResourceType):

    Returns:
        Response[IncidentAttachmentsV1ListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        incident_id=incident_id,
        external_id=external_id,
        resource_type=resource_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    external_id: str,
    resource_type: IncidentAttachmentsV1ListResourceType,
) -> Optional[IncidentAttachmentsV1ListResponseBody]:
    """List Incident Attachments V1

     List all incident attachements for an external resouce

    Args:
        incident_id (Union[Unset, None, str]):
        external_id (str):
        resource_type (IncidentAttachmentsV1ListResourceType):

    Returns:
        Response[IncidentAttachmentsV1ListResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            external_id=external_id,
            resource_type=resource_type,
        )
    ).parsed
