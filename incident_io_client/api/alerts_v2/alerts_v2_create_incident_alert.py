from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alerts_create_incident_alert_payload_v2 import (
    AlertsCreateIncidentAlertPayloadV2,
)
from ...models.alerts_create_incident_alert_result_v2 import (
    AlertsCreateIncidentAlertResultV2,
)
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AlertsCreateIncidentAlertPayloadV2,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/incident_alerts",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AlertsCreateIncidentAlertResultV2, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = AlertsCreateIncidentAlertResultV2.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 405:
        response_405 = ErrorResponse.from_dict(response.json())

        return response_405
    if response.status_code == 406:
        response_406 = ErrorResponse.from_dict(response.json())

        return response_406
    if response.status_code == 408:
        response_408 = ErrorResponse.from_dict(response.json())

        return response_408
    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409
    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412
    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413
    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422
    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AlertsCreateIncidentAlertResultV2, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertsCreateIncidentAlertPayloadV2,
) -> Response[Union[AlertsCreateIncidentAlertResultV2, ErrorResponse]]:
    """CreateIncidentAlert Alerts V2

     Attach an alert to an incident, creating the connection between them.

    The API key also needs the 'manage incident alerts' scope, which is what actually relates
    the alert once the connection exists.

    If the alert is already related to this incident, the existing connection is returned
    unchanged. If someone previously marked the alert as unrelated to this incident, that
    decision is preserved and this endpoint returns a 422 — set re_relate to override it.

    Private alerts can only be attached to private incidents, including when re_relate is set.
    An API key that cannot see the alert or the incident receives a 404.

    Busy incidents can be locked by another operation, in which case this endpoint returns a
    409 and the request can be retried.

    Note that this endpoint returns 201 even when it re-relates or returns an existing
    connection rather than creating a new one.

    Args:
        body (AlertsCreateIncidentAlertPayloadV2):  Example: {'alert_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 're_relate':
            False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertsCreateIncidentAlertResultV2, ErrorResponse]]
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
    body: AlertsCreateIncidentAlertPayloadV2,
) -> Optional[Union[AlertsCreateIncidentAlertResultV2, ErrorResponse]]:
    """CreateIncidentAlert Alerts V2

     Attach an alert to an incident, creating the connection between them.

    The API key also needs the 'manage incident alerts' scope, which is what actually relates
    the alert once the connection exists.

    If the alert is already related to this incident, the existing connection is returned
    unchanged. If someone previously marked the alert as unrelated to this incident, that
    decision is preserved and this endpoint returns a 422 — set re_relate to override it.

    Private alerts can only be attached to private incidents, including when re_relate is set.
    An API key that cannot see the alert or the incident receives a 404.

    Busy incidents can be locked by another operation, in which case this endpoint returns a
    409 and the request can be retried.

    Note that this endpoint returns 201 even when it re-relates or returns an existing
    connection rather than creating a new one.

    Args:
        body (AlertsCreateIncidentAlertPayloadV2):  Example: {'alert_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 're_relate':
            False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertsCreateIncidentAlertResultV2, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertsCreateIncidentAlertPayloadV2,
) -> Response[Union[AlertsCreateIncidentAlertResultV2, ErrorResponse]]:
    """CreateIncidentAlert Alerts V2

     Attach an alert to an incident, creating the connection between them.

    The API key also needs the 'manage incident alerts' scope, which is what actually relates
    the alert once the connection exists.

    If the alert is already related to this incident, the existing connection is returned
    unchanged. If someone previously marked the alert as unrelated to this incident, that
    decision is preserved and this endpoint returns a 422 — set re_relate to override it.

    Private alerts can only be attached to private incidents, including when re_relate is set.
    An API key that cannot see the alert or the incident receives a 404.

    Busy incidents can be locked by another operation, in which case this endpoint returns a
    409 and the request can be retried.

    Note that this endpoint returns 201 even when it re-relates or returns an existing
    connection rather than creating a new one.

    Args:
        body (AlertsCreateIncidentAlertPayloadV2):  Example: {'alert_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 're_relate':
            False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertsCreateIncidentAlertResultV2, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertsCreateIncidentAlertPayloadV2,
) -> Optional[Union[AlertsCreateIncidentAlertResultV2, ErrorResponse]]:
    """CreateIncidentAlert Alerts V2

     Attach an alert to an incident, creating the connection between them.

    The API key also needs the 'manage incident alerts' scope, which is what actually relates
    the alert once the connection exists.

    If the alert is already related to this incident, the existing connection is returned
    unchanged. If someone previously marked the alert as unrelated to this incident, that
    decision is preserved and this endpoint returns a 422 — set re_relate to override it.

    Private alerts can only be attached to private incidents, including when re_relate is set.
    An API key that cannot see the alert or the incident receives a 404.

    Busy incidents can be locked by another operation, in which case this endpoint returns a
    409 and the request can be retried.

    Note that this endpoint returns 201 even when it re-relates or returns an existing
    connection rather than creating a new one.

    Args:
        body (AlertsCreateIncidentAlertPayloadV2):  Example: {'alert_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 're_relate':
            False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertsCreateIncidentAlertResultV2, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
