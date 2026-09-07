from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_notes_list_result_v1 import AlertNotesListResultV1
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    alert_id: Union[Unset, str] = UNSET,
    alert_group_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["alert_id"] = alert_id

    params["alert_group_id"] = alert_group_id

    params["page_size"] = page_size

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/alert_notes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AlertNotesListResultV1, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AlertNotesListResultV1.from_dict(response.json())

        return response_200
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
) -> Response[Union[AlertNotesListResultV1, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    alert_id: Union[Unset, str] = UNSET,
    alert_group_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Response[Union[AlertNotesListResultV1, ErrorResponse]]:
    """List Alert Notes V1

     List alert notes attached to an alert.

    Args:
        alert_id (Union[Unset, str]): ID of the alert to list notes for. Provide exactly one of
            alert_id or alert_group_id. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        alert_group_id (Union[Unset, str]): ID of the alert group to list notes for. Provide
            exactly one of alert_id or alert_group_id. Example: 01HB9Z8WANK6P870EA6S7TK1DS.
        page_size (Union[Unset, int]): Integer number of records to return Default: 25. Example:
            25.
        after (Union[Unset, str]): An record's ID. This endpoint will return a list of records
            after this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertNotesListResultV1, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        alert_group_id=alert_group_id,
        page_size=page_size,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    alert_id: Union[Unset, str] = UNSET,
    alert_group_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Optional[Union[AlertNotesListResultV1, ErrorResponse]]:
    """List Alert Notes V1

     List alert notes attached to an alert.

    Args:
        alert_id (Union[Unset, str]): ID of the alert to list notes for. Provide exactly one of
            alert_id or alert_group_id. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        alert_group_id (Union[Unset, str]): ID of the alert group to list notes for. Provide
            exactly one of alert_id or alert_group_id. Example: 01HB9Z8WANK6P870EA6S7TK1DS.
        page_size (Union[Unset, int]): Integer number of records to return Default: 25. Example:
            25.
        after (Union[Unset, str]): An record's ID. This endpoint will return a list of records
            after this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertNotesListResultV1, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        alert_id=alert_id,
        alert_group_id=alert_group_id,
        page_size=page_size,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    alert_id: Union[Unset, str] = UNSET,
    alert_group_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Response[Union[AlertNotesListResultV1, ErrorResponse]]:
    """List Alert Notes V1

     List alert notes attached to an alert.

    Args:
        alert_id (Union[Unset, str]): ID of the alert to list notes for. Provide exactly one of
            alert_id or alert_group_id. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        alert_group_id (Union[Unset, str]): ID of the alert group to list notes for. Provide
            exactly one of alert_id or alert_group_id. Example: 01HB9Z8WANK6P870EA6S7TK1DS.
        page_size (Union[Unset, int]): Integer number of records to return Default: 25. Example:
            25.
        after (Union[Unset, str]): An record's ID. This endpoint will return a list of records
            after this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertNotesListResultV1, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        alert_group_id=alert_group_id,
        page_size=page_size,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    alert_id: Union[Unset, str] = UNSET,
    alert_group_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
) -> Optional[Union[AlertNotesListResultV1, ErrorResponse]]:
    """List Alert Notes V1

     List alert notes attached to an alert.

    Args:
        alert_id (Union[Unset, str]): ID of the alert to list notes for. Provide exactly one of
            alert_id or alert_group_id. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        alert_group_id (Union[Unset, str]): ID of the alert group to list notes for. Provide
            exactly one of alert_id or alert_group_id. Example: 01HB9Z8WANK6P870EA6S7TK1DS.
        page_size (Union[Unset, int]): Integer number of records to return Default: 25. Example:
            25.
        after (Union[Unset, str]): An record's ID. This endpoint will return a list of records
            after this ID in relation to the API response order. Example: 01FDAG4SAP5TYPT98WGR2N7W91.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertNotesListResultV1, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            alert_id=alert_id,
            alert_group_id=alert_group_id,
            page_size=page_size,
            after=after,
        )
    ).parsed
