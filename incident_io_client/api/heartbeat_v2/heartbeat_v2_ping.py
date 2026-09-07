from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    alert_source_config_id: str,
    *,
    token: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: Dict[str, Any] = {}

    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/heartbeat/{alert_source_config_id}/ping".format(
            alert_source_config_id=alert_source_config_id,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
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
) -> Response[Union[Any, ErrorResponse]]:
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
    token: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Ping Heartbeat V2

     Send a heartbeat ping for the specified alert source.

    Records a ping, indicating that the monitored job or service is healthy. The
    heartbeat monitor uses these pings to detect missed heartbeats and fire alerts.
    Both GET and POST are accepted

    Args:
        alert_source_config_id (str): The alert source config this heartbeat ping is for Example:
            01GW2G3V0S59R238FAHPDS1R66.
        token (Union[Unset, str]): Token provided via the token query parameter Example: some-
            random-string.
        authorization (Union[Unset, str]): Bearer token provided via the Authorization header
            Example: Bearer some-random-string.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        alert_source_config_id=alert_source_config_id,
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
    token: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Ping Heartbeat V2

     Send a heartbeat ping for the specified alert source.

    Records a ping, indicating that the monitored job or service is healthy. The
    heartbeat monitor uses these pings to detect missed heartbeats and fire alerts.
    Both GET and POST are accepted

    Args:
        alert_source_config_id (str): The alert source config this heartbeat ping is for Example:
            01GW2G3V0S59R238FAHPDS1R66.
        token (Union[Unset, str]): Token provided via the token query parameter Example: some-
            random-string.
        authorization (Union[Unset, str]): Bearer token provided via the Authorization header
            Example: Bearer some-random-string.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return sync_detailed(
        alert_source_config_id=alert_source_config_id,
        client=client,
        token=token,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    alert_source_config_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    token: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Ping Heartbeat V2

     Send a heartbeat ping for the specified alert source.

    Records a ping, indicating that the monitored job or service is healthy. The
    heartbeat monitor uses these pings to detect missed heartbeats and fire alerts.
    Both GET and POST are accepted

    Args:
        alert_source_config_id (str): The alert source config this heartbeat ping is for Example:
            01GW2G3V0S59R238FAHPDS1R66.
        token (Union[Unset, str]): Token provided via the token query parameter Example: some-
            random-string.
        authorization (Union[Unset, str]): Bearer token provided via the Authorization header
            Example: Bearer some-random-string.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        alert_source_config_id=alert_source_config_id,
        token=token,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_source_config_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    token: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Ping Heartbeat V2

     Send a heartbeat ping for the specified alert source.

    Records a ping, indicating that the monitored job or service is healthy. The
    heartbeat monitor uses these pings to detect missed heartbeats and fire alerts.
    Both GET and POST are accepted

    Args:
        alert_source_config_id (str): The alert source config this heartbeat ping is for Example:
            01GW2G3V0S59R238FAHPDS1R66.
        token (Union[Unset, str]): Token provided via the token query parameter Example: some-
            random-string.
        authorization (Union[Unset, str]): Bearer token provided via the Authorization header
            Example: Bearer some-random-string.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            alert_source_config_id=alert_source_config_id,
            client=client,
            token=token,
            authorization=authorization,
        )
    ).parsed
