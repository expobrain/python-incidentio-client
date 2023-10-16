from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_statuses_v1_create_request_body import (
    IncidentStatusesV1CreateRequestBody,
)
from ...models.incident_statuses_v1_create_response_body import (
    IncidentStatusesV1CreateResponseBody,
)
from ...types import Response


def _get_kwargs(
    *,
    json_body: IncidentStatusesV1CreateRequestBody,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v1/incident_statuses",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentStatusesV1CreateResponseBody]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = IncidentStatusesV1CreateResponseBody.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentStatusesV1CreateResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentStatusesV1CreateRequestBody,
) -> Response[IncidentStatusesV1CreateResponseBody]:
    """Create Incident Statuses V1

     Create a new incident status

    Args:
        json_body (IncidentStatusesV1CreateRequestBody):  Example: {'category': 'live',
            'description': "Impact has been **fully mitigated**, and we're ready to learn from this
            incident.", 'name': 'Closed'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentStatusesV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentStatusesV1CreateRequestBody,
) -> Optional[IncidentStatusesV1CreateResponseBody]:
    """Create Incident Statuses V1

     Create a new incident status

    Args:
        json_body (IncidentStatusesV1CreateRequestBody):  Example: {'category': 'live',
            'description': "Impact has been **fully mitigated**, and we're ready to learn from this
            incident.", 'name': 'Closed'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentStatusesV1CreateResponseBody
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentStatusesV1CreateRequestBody,
) -> Response[IncidentStatusesV1CreateResponseBody]:
    """Create Incident Statuses V1

     Create a new incident status

    Args:
        json_body (IncidentStatusesV1CreateRequestBody):  Example: {'category': 'live',
            'description': "Impact has been **fully mitigated**, and we're ready to learn from this
            incident.", 'name': 'Closed'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentStatusesV1CreateResponseBody]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: IncidentStatusesV1CreateRequestBody,
) -> Optional[IncidentStatusesV1CreateResponseBody]:
    """Create Incident Statuses V1

     Create a new incident status

    Args:
        json_body (IncidentStatusesV1CreateRequestBody):  Example: {'category': 'live',
            'description': "Impact has been **fully mitigated**, and we're ready to learn from this
            incident.", 'name': 'Closed'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentStatusesV1CreateResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
