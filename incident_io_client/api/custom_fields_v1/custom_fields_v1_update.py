from typing import Any, Dict, Optional

import httpx

from ...client import Client
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
    client: Client,
    json_body: CustomFieldsV1UpdateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/custom_fields/{id}"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CustomFieldsV1UpdateResponseBody]:
    if response.status_code == 200:
        response_200 = CustomFieldsV1UpdateResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CustomFieldsV1UpdateResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    json_body: CustomFieldsV1UpdateRequestBody,
) -> Response[CustomFieldsV1UpdateResponseBody]:
    """Update Custom Fields V1

     Update the details of a custom field

    Args:
        id (str):
        json_body (CustomFieldsV1UpdateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'name': 'Affected Team', 'required': 'never',
            'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post':
            True}.

    Returns:
        Response[CustomFieldsV1UpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: CustomFieldsV1UpdateRequestBody,
) -> Optional[CustomFieldsV1UpdateResponseBody]:
    """Update Custom Fields V1

     Update the details of a custom field

    Args:
        id (str):
        json_body (CustomFieldsV1UpdateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'name': 'Affected Team', 'required': 'never',
            'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post':
            True}.

    Returns:
        Response[CustomFieldsV1UpdateResponseBody]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: CustomFieldsV1UpdateRequestBody,
) -> Response[CustomFieldsV1UpdateResponseBody]:
    """Update Custom Fields V1

     Update the details of a custom field

    Args:
        id (str):
        json_body (CustomFieldsV1UpdateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'name': 'Affected Team', 'required': 'never',
            'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post':
            True}.

    Returns:
        Response[CustomFieldsV1UpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: CustomFieldsV1UpdateRequestBody,
) -> Optional[CustomFieldsV1UpdateResponseBody]:
    """Update Custom Fields V1

     Update the details of a custom field

    Args:
        id (str):
        json_body (CustomFieldsV1UpdateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'name': 'Affected Team', 'required': 'never',
            'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post':
            True}.

    Returns:
        Response[CustomFieldsV1UpdateResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
