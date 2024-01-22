from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_fields_v1_update_request_body import (
    CustomFieldsV1UpdateRequestBody,
)
from ...models.custom_fields_v1_update_response_body import (
    CustomFieldsV1UpdateResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: CustomFieldsV1UpdateRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/v1/custom_fields/{id}".format(
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
) -> Optional[CustomFieldsV1UpdateResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CustomFieldsV1UpdateResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CustomFieldsV1UpdateResponseBody]:
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
    body: CustomFieldsV1UpdateRequestBody,
) -> Response[CustomFieldsV1UpdateResponseBody]:
    """Update Custom Fields V1

     Update the details of a custom field

    Args:
        id (str):
        body (CustomFieldsV1UpdateRequestBody):  Example: {'description': 'Which team is impacted
            by this issue', 'name': 'Affected Team', 'required': 'never', 'required_v2': 'never',
            'show_before_closure': True, 'show_before_creation': True, 'show_before_update': True,
            'show_in_announcement_post': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldsV1UpdateResponseBody]
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
    body: CustomFieldsV1UpdateRequestBody,
) -> Optional[CustomFieldsV1UpdateResponseBody]:
    """Update Custom Fields V1

     Update the details of a custom field

    Args:
        id (str):
        body (CustomFieldsV1UpdateRequestBody):  Example: {'description': 'Which team is impacted
            by this issue', 'name': 'Affected Team', 'required': 'never', 'required_v2': 'never',
            'show_before_closure': True, 'show_before_creation': True, 'show_before_update': True,
            'show_in_announcement_post': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldsV1UpdateResponseBody
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
    body: CustomFieldsV1UpdateRequestBody,
) -> Response[CustomFieldsV1UpdateResponseBody]:
    """Update Custom Fields V1

     Update the details of a custom field

    Args:
        id (str):
        body (CustomFieldsV1UpdateRequestBody):  Example: {'description': 'Which team is impacted
            by this issue', 'name': 'Affected Team', 'required': 'never', 'required_v2': 'never',
            'show_before_closure': True, 'show_before_creation': True, 'show_before_update': True,
            'show_in_announcement_post': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldsV1UpdateResponseBody]
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
    body: CustomFieldsV1UpdateRequestBody,
) -> Optional[CustomFieldsV1UpdateResponseBody]:
    """Update Custom Fields V1

     Update the details of a custom field

    Args:
        id (str):
        body (CustomFieldsV1UpdateRequestBody):  Example: {'description': 'Which team is impacted
            by this issue', 'name': 'Affected Team', 'required': 'never', 'required_v2': 'never',
            'show_before_closure': True, 'show_before_creation': True, 'show_before_update': True,
            'show_in_announcement_post': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldsV1UpdateResponseBody
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
