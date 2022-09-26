from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.custom_fields_v1_create_request_body import (
    CustomFieldsV1CreateRequestBody,
)
from ...models.custom_fields_v1_create_response_body import (
    CustomFieldsV1CreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CustomFieldsV1CreateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/custom_fields"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CustomFieldsV1CreateResponseBody]:
    if response.status_code == 201:
        response_201 = CustomFieldsV1CreateResponseBody.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[CustomFieldsV1CreateResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CustomFieldsV1CreateRequestBody,
) -> Response[CustomFieldsV1CreateResponseBody]:
    """Create Custom Fields V1

     Create a new custom field

    Args:
        json_body (CustomFieldsV1CreateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team',
            'required': 'never', 'show_before_closure': True, 'show_before_creation': True,
            'show_in_announcement_post': True}.

    Returns:
        Response[CustomFieldsV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: CustomFieldsV1CreateRequestBody,
) -> Optional[CustomFieldsV1CreateResponseBody]:
    """Create Custom Fields V1

     Create a new custom field

    Args:
        json_body (CustomFieldsV1CreateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team',
            'required': 'never', 'show_before_closure': True, 'show_before_creation': True,
            'show_in_announcement_post': True}.

    Returns:
        Response[CustomFieldsV1CreateResponseBody]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CustomFieldsV1CreateRequestBody,
) -> Response[CustomFieldsV1CreateResponseBody]:
    """Create Custom Fields V1

     Create a new custom field

    Args:
        json_body (CustomFieldsV1CreateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team',
            'required': 'never', 'show_before_closure': True, 'show_before_creation': True,
            'show_in_announcement_post': True}.

    Returns:
        Response[CustomFieldsV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CustomFieldsV1CreateRequestBody,
) -> Optional[CustomFieldsV1CreateResponseBody]:
    """Create Custom Fields V1

     Create a new custom field

    Args:
        json_body (CustomFieldsV1CreateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team',
            'required': 'never', 'show_before_closure': True, 'show_before_creation': True,
            'show_in_announcement_post': True}.

    Returns:
        Response[CustomFieldsV1CreateResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
