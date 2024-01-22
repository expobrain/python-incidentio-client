from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_logs_severity_created_v1_response_body import (
    AuditLogsSeverityCreatedV1ResponseBody,
)
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/x-audit-logs/severity.created.1",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AuditLogsSeverityCreatedV1ResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuditLogsSeverityCreatedV1ResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AuditLogsSeverityCreatedV1ResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuditLogsSeverityCreatedV1ResponseBody]:
    """SeverityCreatedV1 Audit logs

     This entry is created whenever a severity is created

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsSeverityCreatedV1ResponseBody]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuditLogsSeverityCreatedV1ResponseBody]:
    """SeverityCreatedV1 Audit logs

     This entry is created whenever a severity is created

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsSeverityCreatedV1ResponseBody
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuditLogsSeverityCreatedV1ResponseBody]:
    """SeverityCreatedV1 Audit logs

     This entry is created whenever a severity is created

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsSeverityCreatedV1ResponseBody]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuditLogsSeverityCreatedV1ResponseBody]:
    """SeverityCreatedV1 Audit logs

     This entry is created whenever a severity is created

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsSeverityCreatedV1ResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
