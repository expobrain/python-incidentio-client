from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_statuses_v1_update_request_body import (
    IncidentStatusesV1UpdateRequestBody,
)
from ...models.incident_statuses_v1_update_response_body import (
    IncidentStatusesV1UpdateResponseBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: IncidentStatusesV1UpdateRequestBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/v1/incident_statuses/{id}".format(
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
) -> Optional[IncidentStatusesV1UpdateResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentStatusesV1UpdateResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentStatusesV1UpdateResponseBody]:
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
    body: IncidentStatusesV1UpdateRequestBody,
) -> Response[IncidentStatusesV1UpdateResponseBody]:
    """Update Incident Statuses V1

     Update an existing incident status

    Args:
        id (str):
        body (IncidentStatusesV1UpdateRequestBody):  Example: {'description': "Impact has been
            **fully mitigated**, and we're ready to learn from this incident.", 'name': 'Closed'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentStatusesV1UpdateResponseBody]
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
    body: IncidentStatusesV1UpdateRequestBody,
) -> Optional[IncidentStatusesV1UpdateResponseBody]:
    """Update Incident Statuses V1

     Update an existing incident status

    Args:
        id (str):
        body (IncidentStatusesV1UpdateRequestBody):  Example: {'description': "Impact has been
            **fully mitigated**, and we're ready to learn from this incident.", 'name': 'Closed'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentStatusesV1UpdateResponseBody
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
    body: IncidentStatusesV1UpdateRequestBody,
) -> Response[IncidentStatusesV1UpdateResponseBody]:
    """Update Incident Statuses V1

     Update an existing incident status

    Args:
        id (str):
        body (IncidentStatusesV1UpdateRequestBody):  Example: {'description': "Impact has been
            **fully mitigated**, and we're ready to learn from this incident.", 'name': 'Closed'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentStatusesV1UpdateResponseBody]
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
    body: IncidentStatusesV1UpdateRequestBody,
) -> Optional[IncidentStatusesV1UpdateResponseBody]:
    """Update Incident Statuses V1

     Update an existing incident status

    Args:
        id (str):
        body (IncidentStatusesV1UpdateRequestBody):  Example: {'description': "Impact has been
            **fully mitigated**, and we're ready to learn from this incident.", 'name': 'Closed'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentStatusesV1UpdateResponseBody
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
