from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_events_v2_create_http_request_body import (
    AlertEventsV2CreateHTTPRequestBody,
)
from ...models.alert_events_v2_create_http_response_body import (
    AlertEventsV2CreateHTTPResponseBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    alert_source_config_id: str,
    *,
    json_body: AlertEventsV2CreateHTTPRequestBody,
    token: Union[Unset, None, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: Dict[str, Any] = {}
    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v2/alert_events/http/{alert_source_config_id}".format(
            alert_source_config_id=alert_source_config_id,
        ),
        "json": json_json_body,
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AlertEventsV2CreateHTTPResponseBody]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = AlertEventsV2CreateHTTPResponseBody.from_dict(response.json())

        return response_202
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AlertEventsV2CreateHTTPResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_source_config_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AlertEventsV2CreateHTTPRequestBody,
    token: Union[Unset, None, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[AlertEventsV2CreateHTTPResponseBody]:
    """CreateHTTP Alert Events V2

     Create an alert event using an HTTP source.

    Args:
        alert_source_config_id (str):
        token (Union[Unset, None, str]):
        authorization (Union[Unset, str]):
        json_body (AlertEventsV2CreateHTTPRequestBody):  Example: {'deduplication_key':
            '4293868629', 'description': "We've detected a number of timeouts on hello.world.com, the
            service may be down. To fix...", 'metadata': {'service': 'hello.world.com', 'team': ['my-
            team']}, 'source_url': 'https://www.my-alerting-platform.com/alerts/my-alert-123',
            'status': 'firing', 'title': '*errors.withMessage: PG::Error failed to connect'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertEventsV2CreateHTTPResponseBody]
    """

    kwargs = _get_kwargs(
        alert_source_config_id=alert_source_config_id,
        json_body=json_body,
        token=token,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_source_config_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AlertEventsV2CreateHTTPRequestBody,
    token: Union[Unset, None, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[AlertEventsV2CreateHTTPResponseBody]:
    """CreateHTTP Alert Events V2

     Create an alert event using an HTTP source.

    Args:
        alert_source_config_id (str):
        token (Union[Unset, None, str]):
        authorization (Union[Unset, str]):
        json_body (AlertEventsV2CreateHTTPRequestBody):  Example: {'deduplication_key':
            '4293868629', 'description': "We've detected a number of timeouts on hello.world.com, the
            service may be down. To fix...", 'metadata': {'service': 'hello.world.com', 'team': ['my-
            team']}, 'source_url': 'https://www.my-alerting-platform.com/alerts/my-alert-123',
            'status': 'firing', 'title': '*errors.withMessage: PG::Error failed to connect'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertEventsV2CreateHTTPResponseBody
    """

    return sync_detailed(
        alert_source_config_id=alert_source_config_id,
        client=client,
        json_body=json_body,
        token=token,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    alert_source_config_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AlertEventsV2CreateHTTPRequestBody,
    token: Union[Unset, None, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[AlertEventsV2CreateHTTPResponseBody]:
    """CreateHTTP Alert Events V2

     Create an alert event using an HTTP source.

    Args:
        alert_source_config_id (str):
        token (Union[Unset, None, str]):
        authorization (Union[Unset, str]):
        json_body (AlertEventsV2CreateHTTPRequestBody):  Example: {'deduplication_key':
            '4293868629', 'description': "We've detected a number of timeouts on hello.world.com, the
            service may be down. To fix...", 'metadata': {'service': 'hello.world.com', 'team': ['my-
            team']}, 'source_url': 'https://www.my-alerting-platform.com/alerts/my-alert-123',
            'status': 'firing', 'title': '*errors.withMessage: PG::Error failed to connect'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertEventsV2CreateHTTPResponseBody]
    """

    kwargs = _get_kwargs(
        alert_source_config_id=alert_source_config_id,
        json_body=json_body,
        token=token,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_source_config_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AlertEventsV2CreateHTTPRequestBody,
    token: Union[Unset, None, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[AlertEventsV2CreateHTTPResponseBody]:
    """CreateHTTP Alert Events V2

     Create an alert event using an HTTP source.

    Args:
        alert_source_config_id (str):
        token (Union[Unset, None, str]):
        authorization (Union[Unset, str]):
        json_body (AlertEventsV2CreateHTTPRequestBody):  Example: {'deduplication_key':
            '4293868629', 'description': "We've detected a number of timeouts on hello.world.com, the
            service may be down. To fix...", 'metadata': {'service': 'hello.world.com', 'team': ['my-
            team']}, 'source_url': 'https://www.my-alerting-platform.com/alerts/my-alert-123',
            'status': 'firing', 'title': '*errors.withMessage: PG::Error failed to connect'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertEventsV2CreateHTTPResponseBody
    """

    return (
        await asyncio_detailed(
            alert_source_config_id=alert_source_config_id,
            client=client,
            json_body=json_body,
            token=token,
            authorization=authorization,
        )
    ).parsed
