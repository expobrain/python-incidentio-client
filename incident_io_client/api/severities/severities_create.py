from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.severities_create_request_body import SeveritiesCreateRequestBody
from ...models.severities_create_response_body import SeveritiesCreateResponseBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SeveritiesCreateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/severities"

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


def _parse_response(*, response: httpx.Response) -> Optional[SeveritiesCreateResponseBody]:
    if response.status_code == 201:
        response_201 = SeveritiesCreateResponseBody.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[SeveritiesCreateResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SeveritiesCreateRequestBody,
) -> Response[SeveritiesCreateResponseBody]:
    """Create Severities

     Create a new severity

    Args:
        json_body (SeveritiesCreateRequestBody):  Example: {'description': "It's not really that
            bad, everyone chill", 'name': 'Minor', 'rank': 1}.

    Returns:
        Response[SeveritiesCreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: SeveritiesCreateRequestBody,
) -> Optional[SeveritiesCreateResponseBody]:
    """Create Severities

     Create a new severity

    Args:
        json_body (SeveritiesCreateRequestBody):  Example: {'description': "It's not really that
            bad, everyone chill", 'name': 'Minor', 'rank': 1}.

    Returns:
        Response[SeveritiesCreateResponseBody]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SeveritiesCreateRequestBody,
) -> Response[SeveritiesCreateResponseBody]:
    """Create Severities

     Create a new severity

    Args:
        json_body (SeveritiesCreateRequestBody):  Example: {'description': "It's not really that
            bad, everyone chill", 'name': 'Minor', 'rank': 1}.

    Returns:
        Response[SeveritiesCreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: SeveritiesCreateRequestBody,
) -> Optional[SeveritiesCreateResponseBody]:
    """Create Severities

     Create a new severity

    Args:
        json_body (SeveritiesCreateRequestBody):  Example: {'description': "It's not really that
            bad, everyone chill", 'name': 'Minor', 'rank': 1}.

    Returns:
        Response[SeveritiesCreateResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
