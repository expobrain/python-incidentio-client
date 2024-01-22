from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_options_v1_update_request_body import (
    CustomFieldOptionsV1UpdateRequestBody,
)
from ...models.custom_field_options_v1_update_response_body import (
    CustomFieldOptionsV1UpdateResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: CustomFieldOptionsV1UpdateRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/v1/custom_field_options/{id}".format(
            id=id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CustomFieldOptionsV1UpdateResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CustomFieldOptionsV1UpdateResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CustomFieldOptionsV1UpdateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomFieldOptionsV1UpdateRequestBody,
) -> Response[CustomFieldOptionsV1UpdateResponseBody]:
    """Update Custom Field Options V1

     Update a custom field option

    Args:
        id (str):
        body (CustomFieldOptionsV1UpdateRequestBody):  Example: {'sort_key': 10, 'value':
            'Product'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldOptionsV1UpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomFieldOptionsV1UpdateRequestBody,
) -> Optional[CustomFieldOptionsV1UpdateResponseBody]:
    """Update Custom Field Options V1

     Update a custom field option

    Args:
        id (str):
        body (CustomFieldOptionsV1UpdateRequestBody):  Example: {'sort_key': 10, 'value':
            'Product'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldOptionsV1UpdateResponseBody
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomFieldOptionsV1UpdateRequestBody,
) -> Response[CustomFieldOptionsV1UpdateResponseBody]:
    """Update Custom Field Options V1

     Update a custom field option

    Args:
        id (str):
        body (CustomFieldOptionsV1UpdateRequestBody):  Example: {'sort_key': 10, 'value':
            'Product'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldOptionsV1UpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomFieldOptionsV1UpdateRequestBody,
) -> Optional[CustomFieldOptionsV1UpdateResponseBody]:
    """Update Custom Field Options V1

     Update a custom field option

    Args:
        id (str):
        body (CustomFieldOptionsV1UpdateRequestBody):  Example: {'sort_key': 10, 'value':
            'Product'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldOptionsV1UpdateResponseBody
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
