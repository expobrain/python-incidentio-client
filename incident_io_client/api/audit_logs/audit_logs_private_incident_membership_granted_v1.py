from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_logs_private_incident_membership_granted_v1_response_body import (
    AuditLogsPrivateIncidentMembershipGrantedV1ResponseBody,
)
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/x-audit-logs/private_incident_membership.granted.1",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AuditLogsPrivateIncidentMembershipGrantedV1ResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuditLogsPrivateIncidentMembershipGrantedV1ResponseBody.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AuditLogsPrivateIncidentMembershipGrantedV1ResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuditLogsPrivateIncidentMembershipGrantedV1ResponseBody]:
    """PrivateIncidentMembershipGrantedV1 Audit logs

     This entry is created whenever someone is granted access to a private incident. If they have the
    'manage private incidents' permission, then it'll appear that the system has given them access to
    the incident.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsPrivateIncidentMembershipGrantedV1ResponseBody]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuditLogsPrivateIncidentMembershipGrantedV1ResponseBody]:
    """PrivateIncidentMembershipGrantedV1 Audit logs

     This entry is created whenever someone is granted access to a private incident. If they have the
    'manage private incidents' permission, then it'll appear that the system has given them access to
    the incident.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsPrivateIncidentMembershipGrantedV1ResponseBody
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuditLogsPrivateIncidentMembershipGrantedV1ResponseBody]:
    """PrivateIncidentMembershipGrantedV1 Audit logs

     This entry is created whenever someone is granted access to a private incident. If they have the
    'manage private incidents' permission, then it'll appear that the system has given them access to
    the incident.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsPrivateIncidentMembershipGrantedV1ResponseBody]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuditLogsPrivateIncidentMembershipGrantedV1ResponseBody]:
    """PrivateIncidentMembershipGrantedV1 Audit logs

     This entry is created whenever someone is granted access to a private incident. If they have the
    'manage private incidents' permission, then it'll appear that the system has given them access to
    the incident.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsPrivateIncidentMembershipGrantedV1ResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
