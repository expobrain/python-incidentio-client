from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.custom_fields_create_request_body import CustomFieldsCreateRequestBody
from ...models.custom_fields_create_response_body import CustomFieldsCreateResponseBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CustomFieldsCreateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/custom_fields"

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CustomFieldsCreateResponseBody]:
    if response.status_code == 201:
        response_201 = CustomFieldsCreateResponseBody.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[CustomFieldsCreateResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CustomFieldsCreateRequestBody,
) -> Response[CustomFieldsCreateResponseBody]:
    """Create Custom Fields

     Create a new custom field

    Args:
        json_body (CustomFieldsCreateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team',
            'required': 'never', 'show_before_closure': True, 'show_before_creation': True}.

    Returns:
        Response[CustomFieldsCreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: CustomFieldsCreateRequestBody,
) -> Optional[CustomFieldsCreateResponseBody]:
    """Create Custom Fields

     Create a new custom field

    Args:
        json_body (CustomFieldsCreateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team',
            'required': 'never', 'show_before_closure': True, 'show_before_creation': True}.

    Returns:
        Response[CustomFieldsCreateResponseBody]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CustomFieldsCreateRequestBody,
) -> Response[CustomFieldsCreateResponseBody]:
    """Create Custom Fields

     Create a new custom field

    Args:
        json_body (CustomFieldsCreateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team',
            'required': 'never', 'show_before_closure': True, 'show_before_creation': True}.

    Returns:
        Response[CustomFieldsCreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CustomFieldsCreateRequestBody,
) -> Optional[CustomFieldsCreateResponseBody]:
    """Create Custom Fields

     Create a new custom field

    Args:
        json_body (CustomFieldsCreateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'field_type': 'single_select', 'name': 'Affected Team',
            'required': 'never', 'show_before_closure': True, 'show_before_creation': True}.

    Returns:
        Response[CustomFieldsCreateResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
