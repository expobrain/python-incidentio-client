from typing import Any, Dict, Optional

import httpx

from ...client import Client
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
    client: Client,
    json_body: CustomFieldOptionsV1UpdateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/custom_field_options/{id}"

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[CustomFieldOptionsV1UpdateResponseBody]:
    if response.status_code == 200:
        response_200 = CustomFieldOptionsV1UpdateResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[CustomFieldOptionsV1UpdateResponseBody]:
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
    json_body: CustomFieldOptionsV1UpdateRequestBody,
) -> Response[CustomFieldOptionsV1UpdateResponseBody]:
    """Update Custom Field Options V1

     Update a custom field option

    Args:
        id (str):
        json_body (CustomFieldOptionsV1UpdateRequestBody):  Example: {'sort_key': 10, 'value':
            'Product'}.

    Returns:
        Response[CustomFieldOptionsV1UpdateResponseBody]
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
    json_body: CustomFieldOptionsV1UpdateRequestBody,
) -> Optional[CustomFieldOptionsV1UpdateResponseBody]:
    """Update Custom Field Options V1

     Update a custom field option

    Args:
        id (str):
        json_body (CustomFieldOptionsV1UpdateRequestBody):  Example: {'sort_key': 10, 'value':
            'Product'}.

    Returns:
        Response[CustomFieldOptionsV1UpdateResponseBody]
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
    json_body: CustomFieldOptionsV1UpdateRequestBody,
) -> Response[CustomFieldOptionsV1UpdateResponseBody]:
    """Update Custom Field Options V1

     Update a custom field option

    Args:
        id (str):
        json_body (CustomFieldOptionsV1UpdateRequestBody):  Example: {'sort_key': 10, 'value':
            'Product'}.

    Returns:
        Response[CustomFieldOptionsV1UpdateResponseBody]
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
    json_body: CustomFieldOptionsV1UpdateRequestBody,
) -> Optional[CustomFieldOptionsV1UpdateResponseBody]:
    """Update Custom Field Options V1

     Update a custom field option

    Args:
        id (str):
        json_body (CustomFieldOptionsV1UpdateRequestBody):  Example: {'sort_key': 10, 'value':
            'Product'}.

    Returns:
        Response[CustomFieldOptionsV1UpdateResponseBody]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
