from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_notes_create_payload_v1 import AlertNotesCreatePayloadV1
from ...models.alert_notes_create_result_v1 import AlertNotesCreateResultV1
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AlertNotesCreatePayloadV1,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/alert_notes",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AlertNotesCreateResultV1, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = AlertNotesCreateResultV1.from_dict(response.json())

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
) -> Response[Union[AlertNotesCreateResultV1, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertNotesCreatePayloadV1,
) -> Response[Union[AlertNotesCreateResultV1, ErrorResponse]]:
    r"""Create Alert Notes V1

     Add a note to an alert.

    Args:
        body (AlertNotesCreatePayloadV1):  Example: {'alert_group_id':
            '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'content':
            'Customer reports **checkout 500s** starting ~14:32 UTC. Investigating `payments-
            api`.\n\n- Error rate: ~12% on `/checkout`\n- Region: `eu-west-1`\n- See
            [dashboard](https://grafana.example.com/d/abc)\n'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertNotesCreateResultV1, ErrorResponse]]
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
    body: AlertNotesCreatePayloadV1,
) -> Optional[Union[AlertNotesCreateResultV1, ErrorResponse]]:
    r"""Create Alert Notes V1

     Add a note to an alert.

    Args:
        body (AlertNotesCreatePayloadV1):  Example: {'alert_group_id':
            '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'content':
            'Customer reports **checkout 500s** starting ~14:32 UTC. Investigating `payments-
            api`.\n\n- Error rate: ~12% on `/checkout`\n- Region: `eu-west-1`\n- See
            [dashboard](https://grafana.example.com/d/abc)\n'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertNotesCreateResultV1, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertNotesCreatePayloadV1,
) -> Response[Union[AlertNotesCreateResultV1, ErrorResponse]]:
    r"""Create Alert Notes V1

     Add a note to an alert.

    Args:
        body (AlertNotesCreatePayloadV1):  Example: {'alert_group_id':
            '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'content':
            'Customer reports **checkout 500s** starting ~14:32 UTC. Investigating `payments-
            api`.\n\n- Error rate: ~12% on `/checkout`\n- Region: `eu-west-1`\n- See
            [dashboard](https://grafana.example.com/d/abc)\n'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertNotesCreateResultV1, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertNotesCreatePayloadV1,
) -> Optional[Union[AlertNotesCreateResultV1, ErrorResponse]]:
    r"""Create Alert Notes V1

     Add a note to an alert.

    Args:
        body (AlertNotesCreatePayloadV1):  Example: {'alert_group_id':
            '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'content':
            'Customer reports **checkout 500s** starting ~14:32 UTC. Investigating `payments-
            api`.\n\n- Error rate: ~12% on `/checkout`\n- Region: `eu-west-1`\n- See
            [dashboard](https://grafana.example.com/d/abc)\n'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertNotesCreateResultV1, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
