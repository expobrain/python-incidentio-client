from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.custom_field_options_show_response_body import (
    CustomFieldOptionsShowResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/custom_field_options/{id}"

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[CustomFieldOptionsShowResponseBody]:
    if response.status_code == 200:
        response_200 = CustomFieldOptionsShowResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CustomFieldOptionsShowResponseBody]:
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
) -> Response[CustomFieldOptionsShowResponseBody]:
    """Show Custom Field Options

     Get a single custom field option

    Args:
        id (str):

    Returns:
        Response[CustomFieldOptionsShowResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
) -> Optional[CustomFieldOptionsShowResponseBody]:
    """Show Custom Field Options

     Get a single custom field option

    Args:
        id (str):

    Returns:
        Response[CustomFieldOptionsShowResponseBody]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[CustomFieldOptionsShowResponseBody]:
    """Show Custom Field Options

     Get a single custom field option

    Args:
        id (str):

    Returns:
        Response[CustomFieldOptionsShowResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
) -> Optional[CustomFieldOptionsShowResponseBody]:
    """Show Custom Field Options

     Get a single custom field option

    Args:
        id (str):

    Returns:
        Response[CustomFieldOptionsShowResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
