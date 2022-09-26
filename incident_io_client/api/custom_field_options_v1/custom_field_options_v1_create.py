from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.custom_field_options_v1_create_request_body import (
    CustomFieldOptionsV1CreateRequestBody,
)
from ...models.custom_field_options_v1_create_response_body import (
    CustomFieldOptionsV1CreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CustomFieldOptionsV1CreateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/custom_field_options"

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[CustomFieldOptionsV1CreateResponseBody]:
    if response.status_code == 201:
        response_201 = CustomFieldOptionsV1CreateResponseBody.from_dict(response.json())

        return response_201
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[CustomFieldOptionsV1CreateResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CustomFieldOptionsV1CreateRequestBody,
) -> Response[CustomFieldOptionsV1CreateResponseBody]:
    """Create Custom Field Options V1

     Create a custom field option. If the sort key is not supplied, it'll default to 1000, so the option
    appears near the end of the list.

    Args:
        json_body (CustomFieldOptionsV1CreateRequestBody):  Example: {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}.

    Returns:
        Response[CustomFieldOptionsV1CreateResponseBody]
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
    json_body: CustomFieldOptionsV1CreateRequestBody,
) -> Optional[CustomFieldOptionsV1CreateResponseBody]:
    """Create Custom Field Options V1

     Create a custom field option. If the sort key is not supplied, it'll default to 1000, so the option
    appears near the end of the list.

    Args:
        json_body (CustomFieldOptionsV1CreateRequestBody):  Example: {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}.

    Returns:
        Response[CustomFieldOptionsV1CreateResponseBody]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CustomFieldOptionsV1CreateRequestBody,
) -> Response[CustomFieldOptionsV1CreateResponseBody]:
    """Create Custom Field Options V1

     Create a custom field option. If the sort key is not supplied, it'll default to 1000, so the option
    appears near the end of the list.

    Args:
        json_body (CustomFieldOptionsV1CreateRequestBody):  Example: {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}.

    Returns:
        Response[CustomFieldOptionsV1CreateResponseBody]
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
    json_body: CustomFieldOptionsV1CreateRequestBody,
) -> Optional[CustomFieldOptionsV1CreateResponseBody]:
    """Create Custom Field Options V1

     Create a custom field option. If the sort key is not supplied, it'll default to 1000, so the option
    appears near the end of the list.

    Args:
        json_body (CustomFieldOptionsV1CreateRequestBody):  Example: {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}.

    Returns:
        Response[CustomFieldOptionsV1CreateResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
