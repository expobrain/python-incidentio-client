from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_options_v1_list_response_body import (
    CustomFieldOptionsV1ListResponseBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    custom_field_id: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    params["custom_field_id"] = custom_field_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/custom_field_options",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CustomFieldOptionsV1ListResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CustomFieldOptionsV1ListResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CustomFieldOptionsV1ListResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    custom_field_id: str,
) -> Response[CustomFieldOptionsV1ListResponseBody]:
    """List Custom Field Options V1

     Show custom field options for a custom field

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):
        custom_field_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldOptionsV1ListResponseBody]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        custom_field_id=custom_field_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    custom_field_id: str,
) -> Optional[CustomFieldOptionsV1ListResponseBody]:
    """List Custom Field Options V1

     Show custom field options for a custom field

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):
        custom_field_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldOptionsV1ListResponseBody
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        custom_field_id=custom_field_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    custom_field_id: str,
) -> Response[CustomFieldOptionsV1ListResponseBody]:
    """List Custom Field Options V1

     Show custom field options for a custom field

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):
        custom_field_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldOptionsV1ListResponseBody]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        custom_field_id=custom_field_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    custom_field_id: str,
) -> Optional[CustomFieldOptionsV1ListResponseBody]:
    """List Custom Field Options V1

     Show custom field options for a custom field

    Args:
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):
        custom_field_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldOptionsV1ListResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            custom_field_id=custom_field_id,
        )
    ).parsed
