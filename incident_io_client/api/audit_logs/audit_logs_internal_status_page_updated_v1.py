from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_logs_internal_status_page_updated_v1_response_body import (
    AuditLogsInternalStatusPageUpdatedV1ResponseBody,
)
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/x-audit-logs/internal_status_page.updated.1",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AuditLogsInternalStatusPageUpdatedV1ResponseBody]:
    if response.status_code == 200:
        response_200 = AuditLogsInternalStatusPageUpdatedV1ResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AuditLogsInternalStatusPageUpdatedV1ResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuditLogsInternalStatusPageUpdatedV1ResponseBody]:
    """InternalStatusPageUpdatedV1 Audit logs

     This entry is created whenever an internal status page has its configuration updated

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsInternalStatusPageUpdatedV1ResponseBody]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuditLogsInternalStatusPageUpdatedV1ResponseBody]:
    """InternalStatusPageUpdatedV1 Audit logs

     This entry is created whenever an internal status page has its configuration updated

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsInternalStatusPageUpdatedV1ResponseBody
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuditLogsInternalStatusPageUpdatedV1ResponseBody]:
    """InternalStatusPageUpdatedV1 Audit logs

     This entry is created whenever an internal status page has its configuration updated

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsInternalStatusPageUpdatedV1ResponseBody]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuditLogsInternalStatusPageUpdatedV1ResponseBody]:
    """InternalStatusPageUpdatedV1 Audit logs

     This entry is created whenever an internal status page has its configuration updated

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsInternalStatusPageUpdatedV1ResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
