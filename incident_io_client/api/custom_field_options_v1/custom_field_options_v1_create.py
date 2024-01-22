from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_options_v1_create_request_body import (
    CustomFieldOptionsV1CreateRequestBody,
)
from ...models.custom_field_options_v1_create_response_body import (
    CustomFieldOptionsV1CreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: CustomFieldOptionsV1CreateRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/custom_field_options",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CustomFieldOptionsV1CreateResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CustomFieldOptionsV1CreateResponseBody.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CustomFieldOptionsV1CreateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomFieldOptionsV1CreateRequestBody,
) -> Response[CustomFieldOptionsV1CreateResponseBody]:
    """Create Custom Field Options V1

     Create a custom field option. If the sort key is not supplied, it'll default to 1000, so the option
    appears near the end of the list.

    Args:
        body (CustomFieldOptionsV1CreateRequestBody):  Example: {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldOptionsV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomFieldOptionsV1CreateRequestBody,
) -> Optional[CustomFieldOptionsV1CreateResponseBody]:
    """Create Custom Field Options V1

     Create a custom field option. If the sort key is not supplied, it'll default to 1000, so the option
    appears near the end of the list.

    Args:
        body (CustomFieldOptionsV1CreateRequestBody):  Example: {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldOptionsV1CreateResponseBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomFieldOptionsV1CreateRequestBody,
) -> Response[CustomFieldOptionsV1CreateResponseBody]:
    """Create Custom Field Options V1

     Create a custom field option. If the sort key is not supplied, it'll default to 1000, so the option
    appears near the end of the list.

    Args:
        body (CustomFieldOptionsV1CreateRequestBody):  Example: {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldOptionsV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomFieldOptionsV1CreateRequestBody,
) -> Optional[CustomFieldOptionsV1CreateResponseBody]:
    """Create Custom Field Options V1

     Create a custom field option. If the sort key is not supplied, it'll default to 1000, so the option
    appears near the end of the list.

    Args:
        body (CustomFieldOptionsV1CreateRequestBody):  Example: {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldOptionsV1CreateResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
