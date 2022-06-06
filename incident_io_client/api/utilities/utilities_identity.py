from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.utilities_identity_response_body import UtilitiesIdentityResponseBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/identity"

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[UtilitiesIdentityResponseBody]:
    if response.status_code == 200:
        response_200 = UtilitiesIdentityResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[UtilitiesIdentityResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[UtilitiesIdentityResponseBody]:
    """Identity Utilities

     Test if your API key is valid, and which roles it has.

    Returns:
        Response[UtilitiesIdentityResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[UtilitiesIdentityResponseBody]:
    """Identity Utilities

     Test if your API key is valid, and which roles it has.

    Returns:
        Response[UtilitiesIdentityResponseBody]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[UtilitiesIdentityResponseBody]:
    """Identity Utilities

     Test if your API key is valid, and which roles it has.

    Returns:
        Response[UtilitiesIdentityResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[UtilitiesIdentityResponseBody]:
    """Identity Utilities

     Test if your API key is valid, and which roles it has.

    Returns:
        Response[UtilitiesIdentityResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
