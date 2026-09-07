from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.policies_list_result_v2 import PoliciesListResultV2
from ...models.policies_v2_list_policy_type import PoliciesV2ListPolicyType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    policy_type: Union[Unset, PoliciesV2ListPolicyType] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    json_policy_type: Union[Unset, str] = UNSET
    if not isinstance(policy_type, Unset):
        json_policy_type = policy_type.value

    params["policy_type"] = json_policy_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/policies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PoliciesListResultV2]]:
    if response.status_code == 200:
        response_200 = PoliciesListResultV2.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PoliciesListResultV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    policy_type: Union[Unset, PoliciesV2ListPolicyType] = UNSET,
) -> Response[Union[ErrorResponse, PoliciesListResultV2]]:
    """List Policies V2

     List all policies for an organisation.

    Args:
        page_size (Union[Unset, int]): Number of policies to return per page Default: 25. Example:
            25.
        after (Union[Unset, str]): The ID of the last policy on the previous page Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        policy_type (Union[Unset, PoliciesV2ListPolicyType]): Filter to policies of this type
            Example: follow_up.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PoliciesListResultV2]]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        policy_type=policy_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    policy_type: Union[Unset, PoliciesV2ListPolicyType] = UNSET,
) -> Optional[Union[ErrorResponse, PoliciesListResultV2]]:
    """List Policies V2

     List all policies for an organisation.

    Args:
        page_size (Union[Unset, int]): Number of policies to return per page Default: 25. Example:
            25.
        after (Union[Unset, str]): The ID of the last policy on the previous page Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        policy_type (Union[Unset, PoliciesV2ListPolicyType]): Filter to policies of this type
            Example: follow_up.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PoliciesListResultV2]
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        policy_type=policy_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    policy_type: Union[Unset, PoliciesV2ListPolicyType] = UNSET,
) -> Response[Union[ErrorResponse, PoliciesListResultV2]]:
    """List Policies V2

     List all policies for an organisation.

    Args:
        page_size (Union[Unset, int]): Number of policies to return per page Default: 25. Example:
            25.
        after (Union[Unset, str]): The ID of the last policy on the previous page Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        policy_type (Union[Unset, PoliciesV2ListPolicyType]): Filter to policies of this type
            Example: follow_up.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PoliciesListResultV2]]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        policy_type=policy_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    policy_type: Union[Unset, PoliciesV2ListPolicyType] = UNSET,
) -> Optional[Union[ErrorResponse, PoliciesListResultV2]]:
    """List Policies V2

     List all policies for an organisation.

    Args:
        page_size (Union[Unset, int]): Number of policies to return per page Default: 25. Example:
            25.
        after (Union[Unset, str]): The ID of the last policy on the previous page Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        policy_type (Union[Unset, PoliciesV2ListPolicyType]): Filter to policies of this type
            Example: follow_up.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PoliciesListResultV2]
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            policy_type=policy_type,
        )
    ).parsed
