from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.custom_fields_show_response_body import CustomFieldsShowResponseBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/custom_fields/{id}"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[CustomFieldsShowResponseBody]:
    if response.status_code == 200:
        response_200 = CustomFieldsShowResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CustomFieldsShowResponseBody]:
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
) -> Response[CustomFieldsShowResponseBody]:
    """Show Custom Fields

     Get a single custom field.

    Args:
        id (str):

    Returns:
        Response[CustomFieldsShowResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
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
) -> Optional[CustomFieldsShowResponseBody]:
    """Show Custom Fields

     Get a single custom field.

    Args:
        id (str):

    Returns:
        Response[CustomFieldsShowResponseBody]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[CustomFieldsShowResponseBody]:
    """Show Custom Fields

     Get a single custom field.

    Args:
        id (str):

    Returns:
        Response[CustomFieldsShowResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
) -> Optional[CustomFieldsShowResponseBody]:
    """Show Custom Fields

     Get a single custom field.

    Args:
        id (str):

    Returns:
        Response[CustomFieldsShowResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
