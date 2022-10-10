from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.incidents_v2_list_response_body import IncidentsV2ListResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, Any] = UNSET,
    severity: Union[Unset, None, Any] = UNSET,
    incident_type: Union[Unset, None, Any] = UNSET,
    incident_role: Union[Unset, None, Any] = UNSET,
    custom_field: Union[Unset, None, Any] = UNSET,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/incidents"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page_size"] = page_size

    params["after"] = after

    params["status"] = status

    params["severity"] = severity

    params["incident_type"] = incident_type

    params["incident_role"] = incident_role

    params["custom_field"] = custom_field

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncidentsV2ListResponseBody]:
    if response.status_code == 200:
        response_200 = IncidentsV2ListResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentsV2ListResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, Any] = UNSET,
    severity: Union[Unset, None, Any] = UNSET,
    incident_type: Union[Unset, None, Any] = UNSET,
    incident_role: Union[Unset, None, Any] = UNSET,
    custom_field: Union[Unset, None, Any] = UNSET,
) -> Response[IncidentsV2ListResponseBody]:
    """List Incidents V2

     List all incidents for an organisation.

    This endpoint supports a number of filters, which can help find incidents matching certain
    criteria.

    Filters are provided as query parameters, but due to the dynamic nature of what you can
    query by (different accounts have different custom fields, statuses, etc) they are more
    complex than most.

    To help, here are some exemplar curl requests with a human description of what they search
    for.

    Note that:
    - Filters may be used together, and the result will be incidents that match all filters.
    - IDs are normally in UUID format, but have been replaced with shorter strings to improve
    readability.
    - All query parameters must be URI encoded.

    ### By status

    With status of id=ABC, find all incidents that are set to that status:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status[one_of]=ABC'

    Or all incidents that are not set to status with id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status[not_in]=ABC'

    ### By severity

    With severity of id=ABC, find all incidents that are set to that severity:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'severity[one_of]=ABC'

    Or all incidents where severity rank is greater-than-or-equal-to the rank of severity
    id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'severity[gte]=ABC'

    Or all incidents where severity rank is less-than-or-equal-to the rank of severity id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'severity[lte]=ABC'

    ### By incident type

    With incident type of id=ABC, find all incidents that are of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_type[one_of]=ABC'

    Or all incidents not of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_type[not_in]=ABC'

    ### By incident role

    Roles and custom fields have another nested layer in the query parameter, to account for
    operations against any of the roles or custom fields created in the account.

    With incident role id=ABC, find all incidents where that role is unset:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_role[ABC][is_blank]=true'

    Or where the role has been set:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_role[ABC][is_blank]=false'

    ### By option custom fields

    With an option custom field id=ABC, all incidents that have field ABC set to the custom
    field option of id=XYZ:

    		curl \
    			--get 'https://api.incident.io/v2/incidents' \
    			--data 'custom_field[ABC][one_of]=XYZ'

    Or all incidents that do not have custom field id=ABC set to option id=XYZ:

    		curl \
    			--get 'https://api.incident.io/v2/incidents' \
    			--data 'custom_field[ABC][not_in]=XYZ'

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        status (Union[Unset, None, Any]):
        severity (Union[Unset, None, Any]):
        incident_type (Union[Unset, None, Any]):
        incident_role (Union[Unset, None, Any]):
        custom_field (Union[Unset, None, Any]):

    Returns:
        Response[IncidentsV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        after=after,
        status=status,
        severity=severity,
        incident_type=incident_type,
        incident_role=incident_role,
        custom_field=custom_field,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, Any] = UNSET,
    severity: Union[Unset, None, Any] = UNSET,
    incident_type: Union[Unset, None, Any] = UNSET,
    incident_role: Union[Unset, None, Any] = UNSET,
    custom_field: Union[Unset, None, Any] = UNSET,
) -> Optional[IncidentsV2ListResponseBody]:
    """List Incidents V2

     List all incidents for an organisation.

    This endpoint supports a number of filters, which can help find incidents matching certain
    criteria.

    Filters are provided as query parameters, but due to the dynamic nature of what you can
    query by (different accounts have different custom fields, statuses, etc) they are more
    complex than most.

    To help, here are some exemplar curl requests with a human description of what they search
    for.

    Note that:
    - Filters may be used together, and the result will be incidents that match all filters.
    - IDs are normally in UUID format, but have been replaced with shorter strings to improve
    readability.
    - All query parameters must be URI encoded.

    ### By status

    With status of id=ABC, find all incidents that are set to that status:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status[one_of]=ABC'

    Or all incidents that are not set to status with id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status[not_in]=ABC'

    ### By severity

    With severity of id=ABC, find all incidents that are set to that severity:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'severity[one_of]=ABC'

    Or all incidents where severity rank is greater-than-or-equal-to the rank of severity
    id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'severity[gte]=ABC'

    Or all incidents where severity rank is less-than-or-equal-to the rank of severity id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'severity[lte]=ABC'

    ### By incident type

    With incident type of id=ABC, find all incidents that are of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_type[one_of]=ABC'

    Or all incidents not of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_type[not_in]=ABC'

    ### By incident role

    Roles and custom fields have another nested layer in the query parameter, to account for
    operations against any of the roles or custom fields created in the account.

    With incident role id=ABC, find all incidents where that role is unset:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_role[ABC][is_blank]=true'

    Or where the role has been set:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_role[ABC][is_blank]=false'

    ### By option custom fields

    With an option custom field id=ABC, all incidents that have field ABC set to the custom
    field option of id=XYZ:

    		curl \
    			--get 'https://api.incident.io/v2/incidents' \
    			--data 'custom_field[ABC][one_of]=XYZ'

    Or all incidents that do not have custom field id=ABC set to option id=XYZ:

    		curl \
    			--get 'https://api.incident.io/v2/incidents' \
    			--data 'custom_field[ABC][not_in]=XYZ'

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        status (Union[Unset, None, Any]):
        severity (Union[Unset, None, Any]):
        incident_type (Union[Unset, None, Any]):
        incident_role (Union[Unset, None, Any]):
        custom_field (Union[Unset, None, Any]):

    Returns:
        Response[IncidentsV2ListResponseBody]
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        status=status,
        severity=severity,
        incident_type=incident_type,
        incident_role=incident_role,
        custom_field=custom_field,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, Any] = UNSET,
    severity: Union[Unset, None, Any] = UNSET,
    incident_type: Union[Unset, None, Any] = UNSET,
    incident_role: Union[Unset, None, Any] = UNSET,
    custom_field: Union[Unset, None, Any] = UNSET,
) -> Response[IncidentsV2ListResponseBody]:
    """List Incidents V2

     List all incidents for an organisation.

    This endpoint supports a number of filters, which can help find incidents matching certain
    criteria.

    Filters are provided as query parameters, but due to the dynamic nature of what you can
    query by (different accounts have different custom fields, statuses, etc) they are more
    complex than most.

    To help, here are some exemplar curl requests with a human description of what they search
    for.

    Note that:
    - Filters may be used together, and the result will be incidents that match all filters.
    - IDs are normally in UUID format, but have been replaced with shorter strings to improve
    readability.
    - All query parameters must be URI encoded.

    ### By status

    With status of id=ABC, find all incidents that are set to that status:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status[one_of]=ABC'

    Or all incidents that are not set to status with id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status[not_in]=ABC'

    ### By severity

    With severity of id=ABC, find all incidents that are set to that severity:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'severity[one_of]=ABC'

    Or all incidents where severity rank is greater-than-or-equal-to the rank of severity
    id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'severity[gte]=ABC'

    Or all incidents where severity rank is less-than-or-equal-to the rank of severity id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'severity[lte]=ABC'

    ### By incident type

    With incident type of id=ABC, find all incidents that are of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_type[one_of]=ABC'

    Or all incidents not of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_type[not_in]=ABC'

    ### By incident role

    Roles and custom fields have another nested layer in the query parameter, to account for
    operations against any of the roles or custom fields created in the account.

    With incident role id=ABC, find all incidents where that role is unset:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_role[ABC][is_blank]=true'

    Or where the role has been set:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_role[ABC][is_blank]=false'

    ### By option custom fields

    With an option custom field id=ABC, all incidents that have field ABC set to the custom
    field option of id=XYZ:

    		curl \
    			--get 'https://api.incident.io/v2/incidents' \
    			--data 'custom_field[ABC][one_of]=XYZ'

    Or all incidents that do not have custom field id=ABC set to option id=XYZ:

    		curl \
    			--get 'https://api.incident.io/v2/incidents' \
    			--data 'custom_field[ABC][not_in]=XYZ'

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        status (Union[Unset, None, Any]):
        severity (Union[Unset, None, Any]):
        incident_type (Union[Unset, None, Any]):
        incident_role (Union[Unset, None, Any]):
        custom_field (Union[Unset, None, Any]):

    Returns:
        Response[IncidentsV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        after=after,
        status=status,
        severity=severity,
        incident_type=incident_type,
        incident_role=incident_role,
        custom_field=custom_field,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, Any] = UNSET,
    severity: Union[Unset, None, Any] = UNSET,
    incident_type: Union[Unset, None, Any] = UNSET,
    incident_role: Union[Unset, None, Any] = UNSET,
    custom_field: Union[Unset, None, Any] = UNSET,
) -> Optional[IncidentsV2ListResponseBody]:
    """List Incidents V2

     List all incidents for an organisation.

    This endpoint supports a number of filters, which can help find incidents matching certain
    criteria.

    Filters are provided as query parameters, but due to the dynamic nature of what you can
    query by (different accounts have different custom fields, statuses, etc) they are more
    complex than most.

    To help, here are some exemplar curl requests with a human description of what they search
    for.

    Note that:
    - Filters may be used together, and the result will be incidents that match all filters.
    - IDs are normally in UUID format, but have been replaced with shorter strings to improve
    readability.
    - All query parameters must be URI encoded.

    ### By status

    With status of id=ABC, find all incidents that are set to that status:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status[one_of]=ABC'

    Or all incidents that are not set to status with id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status[not_in]=ABC'

    ### By severity

    With severity of id=ABC, find all incidents that are set to that severity:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'severity[one_of]=ABC'

    Or all incidents where severity rank is greater-than-or-equal-to the rank of severity
    id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'severity[gte]=ABC'

    Or all incidents where severity rank is less-than-or-equal-to the rank of severity id=ABC:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'severity[lte]=ABC'

    ### By incident type

    With incident type of id=ABC, find all incidents that are of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_type[one_of]=ABC'

    Or all incidents not of that type:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_type[not_in]=ABC'

    ### By incident role

    Roles and custom fields have another nested layer in the query parameter, to account for
    operations against any of the roles or custom fields created in the account.

    With incident role id=ABC, find all incidents where that role is unset:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_role[ABC][is_blank]=true'

    Or where the role has been set:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'incident_role[ABC][is_blank]=false'

    ### By option custom fields

    With an option custom field id=ABC, all incidents that have field ABC set to the custom
    field option of id=XYZ:

    		curl \
    			--get 'https://api.incident.io/v2/incidents' \
    			--data 'custom_field[ABC][one_of]=XYZ'

    Or all incidents that do not have custom field id=ABC set to option id=XYZ:

    		curl \
    			--get 'https://api.incident.io/v2/incidents' \
    			--data 'custom_field[ABC][not_in]=XYZ'

    Args:
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):
        status (Union[Unset, None, Any]):
        severity (Union[Unset, None, Any]):
        incident_type (Union[Unset, None, Any]):
        incident_role (Union[Unset, None, Any]):
        custom_field (Union[Unset, None, Any]):

    Returns:
        Response[IncidentsV2ListResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            status=status,
            severity=severity,
            incident_type=incident_type,
            incident_role=incident_role,
            custom_field=custom_field,
        )
    ).parsed
