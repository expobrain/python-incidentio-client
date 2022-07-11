from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incident_types_list_response_body import IncidentTypesListResponseBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/incident_types"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncidentTypesListResponseBody]:
    if response.status_code == 200:
        response_200 = IncidentTypesListResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentTypesListResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[IncidentTypesListResponseBody]:
    """List Incident Types

     List all incident types for an organisation.

    Returns:
        Response[IncidentTypesListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[IncidentTypesListResponseBody]:
    """List Incident Types

     List all incident types for an organisation.

    Returns:
        Response[IncidentTypesListResponseBody]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[IncidentTypesListResponseBody]:
    """List Incident Types

     List all incident types for an organisation.

    Returns:
        Response[IncidentTypesListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[IncidentTypesListResponseBody]:
    """List Incident Types

     List all incident types for an organisation.

    Returns:
        Response[IncidentTypesListResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
