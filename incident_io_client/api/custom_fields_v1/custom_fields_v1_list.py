from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.custom_fields_v1_list_response_body import CustomFieldsV1ListResponseBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/custom_fields"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[CustomFieldsV1ListResponseBody]:
    if response.status_code == 200:
        response_200 = CustomFieldsV1ListResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CustomFieldsV1ListResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[CustomFieldsV1ListResponseBody]:
    """List Custom Fields V1

     List all custom fields for an organisation.

    Returns:
        Response[CustomFieldsV1ListResponseBody]
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
) -> Optional[CustomFieldsV1ListResponseBody]:
    """List Custom Fields V1

     List all custom fields for an organisation.

    Returns:
        Response[CustomFieldsV1ListResponseBody]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[CustomFieldsV1ListResponseBody]:
    """List Custom Fields V1

     List all custom fields for an organisation.

    Returns:
        Response[CustomFieldsV1ListResponseBody]
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
) -> Optional[CustomFieldsV1ListResponseBody]:
    """List Custom Fields V1

     List all custom fields for an organisation.

    Returns:
        Response[CustomFieldsV1ListResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
