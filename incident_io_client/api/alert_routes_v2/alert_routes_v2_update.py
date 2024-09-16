from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_routes_v2_update_request_body import AlertRoutesV2UpdateRequestBody
from ...models.alert_routes_v2_update_response_body import (
    AlertRoutesV2UpdateResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: AlertRoutesV2UpdateRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/v2/alert_routes/{id}".format(
            id=id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AlertRoutesV2UpdateResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AlertRoutesV2UpdateResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AlertRoutesV2UpdateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertRoutesV2UpdateRequestBody,
) -> Response[AlertRoutesV2UpdateResponseBody]:
    """Update Alert Routes V2

     Updates an alert route.

    We recommend you create alert routes in the incident.io dashboard where we allow
    previewing filter and grouping rules.

    Args:
        id (str):
        body (AlertRoutesV2UpdateRequestBody):  Example: {'alert_sources': [{'alert_source_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}]}], 'auto_decline_enabled': False, 'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'defer_time_seconds': 1,
            'enabled': False, 'escalation_bindings': [{'binding': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'expressions': [{'else_branch': {'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'grouping_keys': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0'}],
            'grouping_window_seconds': 1, 'incident_condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'incident_enabled': False, 'name': 'Production
            incidents', 'template': {'custom_field_priorities': {'abc123': 'abc123'}, 'custom_fields':
            {'custom_field_10014': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'incident_mode': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'incident_type': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'name': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'priority_severity':
            'severity-first-wins', 'severity': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'summary': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'workspace':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertRoutesV2UpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertRoutesV2UpdateRequestBody,
) -> Optional[AlertRoutesV2UpdateResponseBody]:
    """Update Alert Routes V2

     Updates an alert route.

    We recommend you create alert routes in the incident.io dashboard where we allow
    previewing filter and grouping rules.

    Args:
        id (str):
        body (AlertRoutesV2UpdateRequestBody):  Example: {'alert_sources': [{'alert_source_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}]}], 'auto_decline_enabled': False, 'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'defer_time_seconds': 1,
            'enabled': False, 'escalation_bindings': [{'binding': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'expressions': [{'else_branch': {'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'grouping_keys': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0'}],
            'grouping_window_seconds': 1, 'incident_condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'incident_enabled': False, 'name': 'Production
            incidents', 'template': {'custom_field_priorities': {'abc123': 'abc123'}, 'custom_fields':
            {'custom_field_10014': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'incident_mode': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'incident_type': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'name': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'priority_severity':
            'severity-first-wins', 'severity': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'summary': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'workspace':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertRoutesV2UpdateResponseBody
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertRoutesV2UpdateRequestBody,
) -> Response[AlertRoutesV2UpdateResponseBody]:
    """Update Alert Routes V2

     Updates an alert route.

    We recommend you create alert routes in the incident.io dashboard where we allow
    previewing filter and grouping rules.

    Args:
        id (str):
        body (AlertRoutesV2UpdateRequestBody):  Example: {'alert_sources': [{'alert_source_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}]}], 'auto_decline_enabled': False, 'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'defer_time_seconds': 1,
            'enabled': False, 'escalation_bindings': [{'binding': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'expressions': [{'else_branch': {'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'grouping_keys': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0'}],
            'grouping_window_seconds': 1, 'incident_condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'incident_enabled': False, 'name': 'Production
            incidents', 'template': {'custom_field_priorities': {'abc123': 'abc123'}, 'custom_fields':
            {'custom_field_10014': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'incident_mode': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'incident_type': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'name': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'priority_severity':
            'severity-first-wins', 'severity': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'summary': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'workspace':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertRoutesV2UpdateResponseBody]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertRoutesV2UpdateRequestBody,
) -> Optional[AlertRoutesV2UpdateResponseBody]:
    """Update Alert Routes V2

     Updates an alert route.

    We recommend you create alert routes in the incident.io dashboard where we allow
    previewing filter and grouping rules.

    Args:
        id (str):
        body (AlertRoutesV2UpdateRequestBody):  Example: {'alert_sources': [{'alert_source_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}]}], 'auto_decline_enabled': False, 'condition_groups':
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}], 'defer_time_seconds': 1,
            'enabled': False, 'escalation_bindings': [{'binding': {'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'expressions': [{'else_branch': {'result': {'array_value':
            [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}}, 'label': 'Team Slack channel', 'operations':
            [{'branches': {'branches': [{'condition_groups': [{'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'result': {'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}}], 'returns': {'array': True, 'type': 'IncidentStatus'}}, 'filter':
            {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}]}, 'navigate': {'reference':
            'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}, 'operation_type': 'navigate', 'parse':
            {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source':
            'metadata.annotations["github.com/repo"]'}}], 'reference': 'abc123', 'root_reference':
            'incident.status'}], 'grouping_keys': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0'}],
            'grouping_window_seconds': 1, 'incident_condition_groups': [{'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}]}], 'incident_enabled': False, 'name': 'Production
            incidents', 'template': {'custom_field_priorities': {'abc123': 'abc123'}, 'custom_fields':
            {'custom_field_10014': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}},
            'incident_mode': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'incident_type': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'name': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'priority_severity':
            'severity-first-wins', 'severity': {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}},
            'summary': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}],
            'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}, 'workspace':
            {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertRoutesV2UpdateResponseBody
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
