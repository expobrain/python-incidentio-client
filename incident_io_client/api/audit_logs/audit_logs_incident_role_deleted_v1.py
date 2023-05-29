from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.audit_logs_incident_role_deleted_v1_response_body import (
    AuditLogsIncidentRoleDeletedV1ResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = f"{client.base_url}/x-audit-logs/incident_role.deleted.1"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[AuditLogsIncidentRoleDeletedV1ResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuditLogsIncidentRoleDeletedV1ResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[AuditLogsIncidentRoleDeletedV1ResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[AuditLogsIncidentRoleDeletedV1ResponseBody]:
    """IncidentRoleDeletedV1 Audit logs

     This entry is created whenever a incident role is deleted

    Returns:
        Response[AuditLogsIncidentRoleDeletedV1ResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[AuditLogsIncidentRoleDeletedV1ResponseBody]:
    """IncidentRoleDeletedV1 Audit logs

     This entry is created whenever a incident role is deleted

    Returns:
        Response[AuditLogsIncidentRoleDeletedV1ResponseBody]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[AuditLogsIncidentRoleDeletedV1ResponseBody]:
    """IncidentRoleDeletedV1 Audit logs

     This entry is created whenever a incident role is deleted

    Returns:
        Response[AuditLogsIncidentRoleDeletedV1ResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[AuditLogsIncidentRoleDeletedV1ResponseBody]:
    """IncidentRoleDeletedV1 Audit logs

     This entry is created whenever a incident role is deleted

    Returns:
        Response[AuditLogsIncidentRoleDeletedV1ResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
