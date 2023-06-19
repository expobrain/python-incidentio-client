from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.audit_logs_incident_role_created_v1_response_body import (
    AuditLogsIncidentRoleCreatedV1ResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = f"{client.base_url}/x-audit-logs/incident_role.created.1"

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
) -> Optional[AuditLogsIncidentRoleCreatedV1ResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuditLogsIncidentRoleCreatedV1ResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[AuditLogsIncidentRoleCreatedV1ResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[AuditLogsIncidentRoleCreatedV1ResponseBody]:
    """IncidentRoleCreatedV1 Audit logs

     This entry is created whenever a incident role is created

    Returns:
        Response[AuditLogsIncidentRoleCreatedV1ResponseBody]
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
) -> Optional[AuditLogsIncidentRoleCreatedV1ResponseBody]:
    """IncidentRoleCreatedV1 Audit logs

     This entry is created whenever a incident role is created

    Returns:
        Response[AuditLogsIncidentRoleCreatedV1ResponseBody]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[AuditLogsIncidentRoleCreatedV1ResponseBody]:
    """IncidentRoleCreatedV1 Audit logs

     This entry is created whenever a incident role is created

    Returns:
        Response[AuditLogsIncidentRoleCreatedV1ResponseBody]
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
) -> Optional[AuditLogsIncidentRoleCreatedV1ResponseBody]:
    """IncidentRoleCreatedV1 Audit logs

     This entry is created whenever a incident role is created

    Returns:
        Response[AuditLogsIncidentRoleCreatedV1ResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
