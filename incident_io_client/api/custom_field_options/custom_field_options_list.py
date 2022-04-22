from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.custom_field_options_list_response_body import (
    CustomFieldOptionsListResponseBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    custom_field_id: str,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/custom_field_options"

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "page_size": page_size,
        "after": after,
        "custom_field_id": custom_field_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CustomFieldOptionsListResponseBody]:
    if response.status_code == 200:
        response_200 = CustomFieldOptionsListResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CustomFieldOptionsListResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    custom_field_id: str,
) -> Response[CustomFieldOptionsListResponseBody]:
    """List Custom Field Options

     Show custom field options for a custom field

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        custom_field_id (str):

    Returns:
        Response[CustomFieldOptionsListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        after=after,
        custom_field_id=custom_field_id,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    custom_field_id: str,
) -> Optional[CustomFieldOptionsListResponseBody]:
    """List Custom Field Options

     Show custom field options for a custom field

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        custom_field_id (str):

    Returns:
        Response[CustomFieldOptionsListResponseBody]
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        custom_field_id=custom_field_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    custom_field_id: str,
) -> Response[CustomFieldOptionsListResponseBody]:
    """List Custom Field Options

     Show custom field options for a custom field

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        custom_field_id (str):

    Returns:
        Response[CustomFieldOptionsListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        after=after,
        custom_field_id=custom_field_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    custom_field_id: str,
) -> Optional[CustomFieldOptionsListResponseBody]:
    """List Custom Field Options

     Show custom field options for a custom field

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        custom_field_id (str):

    Returns:
        Response[CustomFieldOptionsListResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            custom_field_id=custom_field_id,
        )
    ).parsed
