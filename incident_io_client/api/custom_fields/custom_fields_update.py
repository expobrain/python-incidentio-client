from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.custom_fields_update_request_body import CustomFieldsUpdateRequestBody
from ...models.custom_fields_update_response_body import CustomFieldsUpdateResponseBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: CustomFieldsUpdateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/custom_fields/{id}"

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


def _parse_response(*, response: httpx.Response) -> Optional[CustomFieldsUpdateResponseBody]:
    if response.status_code == 200:
        response_200 = CustomFieldsUpdateResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CustomFieldsUpdateResponseBody]:
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
    json_body: CustomFieldsUpdateRequestBody,
) -> Response[CustomFieldsUpdateResponseBody]:
    """Update Custom Fields

     Update the details of a custom field

    Args:
        id (str):
        json_body (CustomFieldsUpdateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'name': 'Affected Team', 'required': 'never',
            'show_before_closure': True, 'show_before_creation': True}.

    Returns:
        Response[CustomFieldsUpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.put(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: CustomFieldsUpdateRequestBody,
) -> Optional[CustomFieldsUpdateResponseBody]:
    """Update Custom Fields

     Update the details of a custom field

    Args:
        id (str):
        json_body (CustomFieldsUpdateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'name': 'Affected Team', 'required': 'never',
            'show_before_closure': True, 'show_before_creation': True}.

    Returns:
        Response[CustomFieldsUpdateResponseBody]
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
    json_body: CustomFieldsUpdateRequestBody,
) -> Response[CustomFieldsUpdateResponseBody]:
    """Update Custom Fields

     Update the details of a custom field

    Args:
        id (str):
        json_body (CustomFieldsUpdateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'name': 'Affected Team', 'required': 'never',
            'show_before_closure': True, 'show_before_creation': True}.

    Returns:
        Response[CustomFieldsUpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: CustomFieldsUpdateRequestBody,
) -> Optional[CustomFieldsUpdateResponseBody]:
    """Update Custom Fields

     Update the details of a custom field

    Args:
        id (str):
        json_body (CustomFieldsUpdateRequestBody):  Example: {'description': 'Which team is
            impacted by this issue', 'name': 'Affected Team', 'required': 'never',
            'show_before_closure': True, 'show_before_creation': True}.

    Returns:
        Response[CustomFieldsUpdateResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
