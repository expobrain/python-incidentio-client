from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.severities_update_request_body import SeveritiesUpdateRequestBody
from ...models.severities_update_response_body import SeveritiesUpdateResponseBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: SeveritiesUpdateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/severities/{id}"

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[SeveritiesUpdateResponseBody]:
    if response.status_code == 200:
        response_200 = SeveritiesUpdateResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SeveritiesUpdateResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    json_body: SeveritiesUpdateRequestBody,
) -> Response[SeveritiesUpdateResponseBody]:
    """Update Severities

     Update an existing severity

    Args:
        id (str):
        json_body (SeveritiesUpdateRequestBody):  Example: {'description': "It's not really that
            bad, everyone chill", 'name': 'Minor', 'rank': 1}.

    Returns:
        Response[SeveritiesUpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.put(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: SeveritiesUpdateRequestBody,
) -> Optional[SeveritiesUpdateResponseBody]:
    """Update Severities

     Update an existing severity

    Args:
        id (str):
        json_body (SeveritiesUpdateRequestBody):  Example: {'description': "It's not really that
            bad, everyone chill", 'name': 'Minor', 'rank': 1}.

    Returns:
        Response[SeveritiesUpdateResponseBody]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: SeveritiesUpdateRequestBody,
) -> Response[SeveritiesUpdateResponseBody]:
    """Update Severities

     Update an existing severity

    Args:
        id (str):
        json_body (SeveritiesUpdateRequestBody):  Example: {'description': "It's not really that
            bad, everyone chill", 'name': 'Minor', 'rank': 1}.

    Returns:
        Response[SeveritiesUpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: SeveritiesUpdateRequestBody,
) -> Optional[SeveritiesUpdateResponseBody]:
    """Update Severities

     Update an existing severity

    Args:
        id (str):
        json_body (SeveritiesUpdateRequestBody):  Example: {'description': "It's not really that
            bad, everyone chill", 'name': 'Minor', 'rank': 1}.

    Returns:
        Response[SeveritiesUpdateResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
