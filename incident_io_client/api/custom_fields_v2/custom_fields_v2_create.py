from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_fields_v2_create_request_body import (
    CustomFieldsV2CreateRequestBody,
)
from ...models.custom_fields_v2_create_response_body import (
    CustomFieldsV2CreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    json_body: CustomFieldsV2CreateRequestBody,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v2/custom_fields",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CustomFieldsV2CreateResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CustomFieldsV2CreateResponseBody.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CustomFieldsV2CreateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CustomFieldsV2CreateRequestBody,
) -> Response[CustomFieldsV2CreateResponseBody]:
    """Create Custom Fields V2

     Create a new custom field

    Args:
        json_body (CustomFieldsV2CreateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldsV2CreateResponseBody]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CustomFieldsV2CreateRequestBody,
) -> Optional[CustomFieldsV2CreateResponseBody]:
    """Create Custom Fields V2

     Create a new custom field

    Args:
        json_body (CustomFieldsV2CreateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldsV2CreateResponseBody
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CustomFieldsV2CreateRequestBody,
) -> Response[CustomFieldsV2CreateResponseBody]:
    """Create Custom Fields V2

     Create a new custom field

    Args:
        json_body (CustomFieldsV2CreateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldsV2CreateResponseBody]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CustomFieldsV2CreateRequestBody,
) -> Optional[CustomFieldsV2CreateResponseBody]:
    """Create Custom Fields V2

     Create a new custom field

    Args:
        json_body (CustomFieldsV2CreateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldsV2CreateResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
