from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_fields_v1_create_request_body import (
    CustomFieldsV1CreateRequestBody,
)
from ...models.custom_fields_v1_create_response_body import (
    CustomFieldsV1CreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: CustomFieldsV1CreateRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/custom_fields",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CustomFieldsV1CreateResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CustomFieldsV1CreateResponseBody.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CustomFieldsV1CreateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomFieldsV1CreateRequestBody,
) -> Response[CustomFieldsV1CreateResponseBody]:
    """Create Custom Fields V1

     Create a new custom field

    Args:
        body (CustomFieldsV1CreateRequestBody):  Example: {'description': 'Which team is impacted
            by this issue', 'field_type': 'single_select', 'name': 'Affected Team', 'required':
            'never', 'required_v2': 'never', 'show_before_closure': True, 'show_before_creation':
            True, 'show_before_update': True, 'show_in_announcement_post': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldsV1CreateResponseBody]
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
    body: CustomFieldsV1CreateRequestBody,
) -> Optional[CustomFieldsV1CreateResponseBody]:
    """Create Custom Fields V1

     Create a new custom field

    Args:
        body (CustomFieldsV1CreateRequestBody):  Example: {'description': 'Which team is impacted
            by this issue', 'field_type': 'single_select', 'name': 'Affected Team', 'required':
            'never', 'required_v2': 'never', 'show_before_closure': True, 'show_before_creation':
            True, 'show_before_update': True, 'show_in_announcement_post': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldsV1CreateResponseBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomFieldsV1CreateRequestBody,
) -> Response[CustomFieldsV1CreateResponseBody]:
    """Create Custom Fields V1

     Create a new custom field

    Args:
        body (CustomFieldsV1CreateRequestBody):  Example: {'description': 'Which team is impacted
            by this issue', 'field_type': 'single_select', 'name': 'Affected Team', 'required':
            'never', 'required_v2': 'never', 'show_before_closure': True, 'show_before_creation':
            True, 'show_before_update': True, 'show_in_announcement_post': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldsV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomFieldsV1CreateRequestBody,
) -> Optional[CustomFieldsV1CreateResponseBody]:
    """Create Custom Fields V1

     Create a new custom field

    Args:
        body (CustomFieldsV1CreateRequestBody):  Example: {'description': 'Which team is impacted
            by this issue', 'field_type': 'single_select', 'name': 'Affected Team', 'required':
            'never', 'required_v2': 'never', 'show_before_closure': True, 'show_before_creation':
            True, 'show_before_update': True, 'show_in_announcement_post': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldsV1CreateResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
