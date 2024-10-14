from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.escalations_v2_create_path_request_body import (
    EscalationsV2CreatePathRequestBody,
)
from ...models.escalations_v2_create_path_response_body import (
    EscalationsV2CreatePathResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: EscalationsV2CreatePathRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/escalation_paths",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[EscalationsV2CreatePathResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = EscalationsV2CreatePathResponseBody.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EscalationsV2CreatePathResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: EscalationsV2CreatePathRequestBody,
) -> Response[EscalationsV2CreatePathResponseBody]:
    """CreatePath Escalations V2

     Create an escalation path.

    An escalation path is a series of steps that describe how a page should be escalated,
    represented as graph, supporting conditional branches based on alert priority and working
    intervals.

    We recommend you create escalation paths in the incident.io dashboard where our path
    builder makes it easy to use conditions and visualise the path.

    Args:
        body (EscalationsV2CreatePathRequestBody):  Example: {'name': 'Urgent Support', 'path':
            [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}], 'else_path': [{}], 'then_path': [{}]}, 'level':
            {'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency':
            'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel':
            {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user',
            'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds':
            1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat':
            {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}],
            'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123',
            'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'abc123'}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EscalationsV2CreatePathResponseBody]
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
    body: EscalationsV2CreatePathRequestBody,
) -> Optional[EscalationsV2CreatePathResponseBody]:
    """CreatePath Escalations V2

     Create an escalation path.

    An escalation path is a series of steps that describe how a page should be escalated,
    represented as graph, supporting conditional branches based on alert priority and working
    intervals.

    We recommend you create escalation paths in the incident.io dashboard where our path
    builder makes it easy to use conditions and visualise the path.

    Args:
        body (EscalationsV2CreatePathRequestBody):  Example: {'name': 'Urgent Support', 'path':
            [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}], 'else_path': [{}], 'then_path': [{}]}, 'level':
            {'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency':
            'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel':
            {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user',
            'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds':
            1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat':
            {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}],
            'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123',
            'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'abc123'}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EscalationsV2CreatePathResponseBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: EscalationsV2CreatePathRequestBody,
) -> Response[EscalationsV2CreatePathResponseBody]:
    """CreatePath Escalations V2

     Create an escalation path.

    An escalation path is a series of steps that describe how a page should be escalated,
    represented as graph, supporting conditional branches based on alert priority and working
    intervals.

    We recommend you create escalation paths in the incident.io dashboard where our path
    builder makes it easy to use conditions and visualise the path.

    Args:
        body (EscalationsV2CreatePathRequestBody):  Example: {'name': 'Urgent Support', 'path':
            [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}], 'else_path': [{}], 'then_path': [{}]}, 'level':
            {'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency':
            'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel':
            {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user',
            'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds':
            1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat':
            {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}],
            'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123',
            'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'abc123'}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EscalationsV2CreatePathResponseBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: EscalationsV2CreatePathRequestBody,
) -> Optional[EscalationsV2CreatePathResponseBody]:
    """CreatePath Escalations V2

     Create an escalation path.

    An escalation path is a series of steps that describe how a page should be escalated,
    represented as graph, supporting conditional branches based on alert priority and working
    intervals.

    We recommend you create escalation paths in the incident.io dashboard where our path
    builder makes it easy to use conditions and visualise the path.

    Args:
        body (EscalationsV2CreatePathRequestBody):  Example: {'name': 'Urgent Support', 'path':
            [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}], 'else_path': [{}], 'then_path': [{}]}, 'level':
            {'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency':
            'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel':
            {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user',
            'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds':
            1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat':
            {'repeat_times': 3, 'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}],
            'working_hours': [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123',
            'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'abc123'}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EscalationsV2CreatePathResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
