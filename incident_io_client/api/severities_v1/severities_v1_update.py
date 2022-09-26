from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.severities_v1_update_request_body import SeveritiesV1UpdateRequestBody
from ...models.severities_v1_update_response_body import SeveritiesV1UpdateResponseBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: SeveritiesV1UpdateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/severities/{id}"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[SeveritiesV1UpdateResponseBody]:
    if response.status_code == 200:
        response_200 = SeveritiesV1UpdateResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SeveritiesV1UpdateResponseBody]:
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
    json_body: SeveritiesV1UpdateRequestBody,
) -> Response[SeveritiesV1UpdateResponseBody]:
    """Update Severities V1

     Update an existing severity

    Args:
        id (str):
        json_body (SeveritiesV1UpdateRequestBody):  Example: {'description': "It's not really that
            bad, everyone chill", 'name': 'Minor', 'rank': 1}.

    Returns:
        Response[SeveritiesV1UpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: SeveritiesV1UpdateRequestBody,
) -> Optional[SeveritiesV1UpdateResponseBody]:
    """Update Severities V1

     Update an existing severity

    Args:
        id (str):
        json_body (SeveritiesV1UpdateRequestBody):  Example: {'description': "It's not really that
            bad, everyone chill", 'name': 'Minor', 'rank': 1}.

    Returns:
        Response[SeveritiesV1UpdateResponseBody]
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
    json_body: SeveritiesV1UpdateRequestBody,
) -> Response[SeveritiesV1UpdateResponseBody]:
    """Update Severities V1

     Update an existing severity

    Args:
        id (str):
        json_body (SeveritiesV1UpdateRequestBody):  Example: {'description': "It's not really that
            bad, everyone chill", 'name': 'Minor', 'rank': 1}.

    Returns:
        Response[SeveritiesV1UpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: SeveritiesV1UpdateRequestBody,
) -> Optional[SeveritiesV1UpdateResponseBody]:
    """Update Severities V1

     Update an existing severity

    Args:
        id (str):
        json_body (SeveritiesV1UpdateRequestBody):  Example: {'description': "It's not really that
            bad, everyone chill", 'name': 'Minor', 'rank': 1}.

    Returns:
        Response[SeveritiesV1UpdateResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
