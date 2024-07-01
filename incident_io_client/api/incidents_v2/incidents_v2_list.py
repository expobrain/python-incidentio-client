from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incidents_v2_list_response_body import IncidentsV2ListResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    status: Union[Unset, Any] = UNSET,
    status_category: Union[Unset, Any] = UNSET,
    created_at: Union[Unset, Any] = UNSET,
    updated_at: Union[Unset, Any] = UNSET,
    severity: Union[Unset, Any] = UNSET,
    incident_type: Union[Unset, Any] = UNSET,
    incident_role: Union[Unset, Any] = UNSET,
    custom_field: Union[Unset, Any] = UNSET,
    mode: Union[Unset, Any] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page_size"] = page_size

    params["after"] = after

    params["status"] = status

    params["status_category"] = status_category

    params["created_at"] = created_at

    params["updated_at"] = updated_at

    params["severity"] = severity

    params["incident_type"] = incident_type

    params["incident_role"] = incident_role

    params["custom_field"] = custom_field

    params["mode"] = mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/incidents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentsV2ListResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentsV2ListResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentsV2ListResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    status: Union[Unset, Any] = UNSET,
    status_category: Union[Unset, Any] = UNSET,
    created_at: Union[Unset, Any] = UNSET,
    updated_at: Union[Unset, Any] = UNSET,
    severity: Union[Unset, Any] = UNSET,
    incident_type: Union[Unset, Any] = UNSET,
    incident_role: Union[Unset, Any] = UNSET,
    custom_field: Union[Unset, Any] = UNSET,
    mode: Union[Unset, Any] = UNSET,
) -> Response[IncidentsV2ListResponseBody]:
    r""" List Incidents V2

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

    ### By created_at or updated_at

    Find all incidents that follow specified date parameters for created_at and updated_at fields.
    Possible values are \"gte\" (greater than or equal to) and \"lte\" (less than or equal to). The
    following example finds all incidents created before or on 2021-01-02T00:00:00Z:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'created_at[lte]=2021-01-02'

    ### By status category

    Find all incidents that are in a status category. Possible values are \"triage\",
    \"declined\", \"merged\", \"canceled\", \"live\", \"learning\" and \"closed\":

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status_category[one_of]=live'

    Or all incidents that are not in a status category:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status_category[not_in]=live'


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

    ### By incident mode

    By default, we return standard and retrospective incidents. This means that test and
    tutorial incidents are filtered out. To override this behaviour, you can use the
    mode filter to specify which modes you want to get.

    To find incidents of all modes:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'mode[one_of]=standard&mode[one_of]=retrospective&mode[one_of]=test&mode[one_of]=tutorial'

    To find just test incidents:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'mode[one_of]=test'


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
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):
        status (Union[Unset, Any]):
        status_category (Union[Unset, Any]):
        created_at (Union[Unset, Any]):
        updated_at (Union[Unset, Any]):
        severity (Union[Unset, Any]):
        incident_type (Union[Unset, Any]):
        incident_role (Union[Unset, Any]):
        custom_field (Union[Unset, Any]):
        mode (Union[Unset, Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentsV2ListResponseBody]
     """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        status=status,
        status_category=status_category,
        created_at=created_at,
        updated_at=updated_at,
        severity=severity,
        incident_type=incident_type,
        incident_role=incident_role,
        custom_field=custom_field,
        mode=mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    status: Union[Unset, Any] = UNSET,
    status_category: Union[Unset, Any] = UNSET,
    created_at: Union[Unset, Any] = UNSET,
    updated_at: Union[Unset, Any] = UNSET,
    severity: Union[Unset, Any] = UNSET,
    incident_type: Union[Unset, Any] = UNSET,
    incident_role: Union[Unset, Any] = UNSET,
    custom_field: Union[Unset, Any] = UNSET,
    mode: Union[Unset, Any] = UNSET,
) -> Optional[IncidentsV2ListResponseBody]:
    r""" List Incidents V2

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

    ### By created_at or updated_at

    Find all incidents that follow specified date parameters for created_at and updated_at fields.
    Possible values are \"gte\" (greater than or equal to) and \"lte\" (less than or equal to). The
    following example finds all incidents created before or on 2021-01-02T00:00:00Z:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'created_at[lte]=2021-01-02'

    ### By status category

    Find all incidents that are in a status category. Possible values are \"triage\",
    \"declined\", \"merged\", \"canceled\", \"live\", \"learning\" and \"closed\":

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status_category[one_of]=live'

    Or all incidents that are not in a status category:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status_category[not_in]=live'


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

    ### By incident mode

    By default, we return standard and retrospective incidents. This means that test and
    tutorial incidents are filtered out. To override this behaviour, you can use the
    mode filter to specify which modes you want to get.

    To find incidents of all modes:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'mode[one_of]=standard&mode[one_of]=retrospective&mode[one_of]=test&mode[one_of]=tutorial'

    To find just test incidents:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'mode[one_of]=test'


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
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):
        status (Union[Unset, Any]):
        status_category (Union[Unset, Any]):
        created_at (Union[Unset, Any]):
        updated_at (Union[Unset, Any]):
        severity (Union[Unset, Any]):
        incident_type (Union[Unset, Any]):
        incident_role (Union[Unset, Any]):
        custom_field (Union[Unset, Any]):
        mode (Union[Unset, Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentsV2ListResponseBody
     """

    return sync_detailed(
        client=client,
        page_size=page_size,
        after=after,
        status=status,
        status_category=status_category,
        created_at=created_at,
        updated_at=updated_at,
        severity=severity,
        incident_type=incident_type,
        incident_role=incident_role,
        custom_field=custom_field,
        mode=mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    status: Union[Unset, Any] = UNSET,
    status_category: Union[Unset, Any] = UNSET,
    created_at: Union[Unset, Any] = UNSET,
    updated_at: Union[Unset, Any] = UNSET,
    severity: Union[Unset, Any] = UNSET,
    incident_type: Union[Unset, Any] = UNSET,
    incident_role: Union[Unset, Any] = UNSET,
    custom_field: Union[Unset, Any] = UNSET,
    mode: Union[Unset, Any] = UNSET,
) -> Response[IncidentsV2ListResponseBody]:
    r""" List Incidents V2

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

    ### By created_at or updated_at

    Find all incidents that follow specified date parameters for created_at and updated_at fields.
    Possible values are \"gte\" (greater than or equal to) and \"lte\" (less than or equal to). The
    following example finds all incidents created before or on 2021-01-02T00:00:00Z:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'created_at[lte]=2021-01-02'

    ### By status category

    Find all incidents that are in a status category. Possible values are \"triage\",
    \"declined\", \"merged\", \"canceled\", \"live\", \"learning\" and \"closed\":

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status_category[one_of]=live'

    Or all incidents that are not in a status category:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status_category[not_in]=live'


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

    ### By incident mode

    By default, we return standard and retrospective incidents. This means that test and
    tutorial incidents are filtered out. To override this behaviour, you can use the
    mode filter to specify which modes you want to get.

    To find incidents of all modes:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'mode[one_of]=standard&mode[one_of]=retrospective&mode[one_of]=test&mode[one_of]=tutorial'

    To find just test incidents:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'mode[one_of]=test'


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
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):
        status (Union[Unset, Any]):
        status_category (Union[Unset, Any]):
        created_at (Union[Unset, Any]):
        updated_at (Union[Unset, Any]):
        severity (Union[Unset, Any]):
        incident_type (Union[Unset, Any]):
        incident_role (Union[Unset, Any]):
        custom_field (Union[Unset, Any]):
        mode (Union[Unset, Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentsV2ListResponseBody]
     """

    kwargs = _get_kwargs(
        page_size=page_size,
        after=after,
        status=status,
        status_category=status_category,
        created_at=created_at,
        updated_at=updated_at,
        severity=severity,
        incident_type=incident_type,
        incident_role=incident_role,
        custom_field=custom_field,
        mode=mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 25,
    after: Union[Unset, str] = UNSET,
    status: Union[Unset, Any] = UNSET,
    status_category: Union[Unset, Any] = UNSET,
    created_at: Union[Unset, Any] = UNSET,
    updated_at: Union[Unset, Any] = UNSET,
    severity: Union[Unset, Any] = UNSET,
    incident_type: Union[Unset, Any] = UNSET,
    incident_role: Union[Unset, Any] = UNSET,
    custom_field: Union[Unset, Any] = UNSET,
    mode: Union[Unset, Any] = UNSET,
) -> Optional[IncidentsV2ListResponseBody]:
    r""" List Incidents V2

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

    ### By created_at or updated_at

    Find all incidents that follow specified date parameters for created_at and updated_at fields.
    Possible values are \"gte\" (greater than or equal to) and \"lte\" (less than or equal to). The
    following example finds all incidents created before or on 2021-01-02T00:00:00Z:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'created_at[lte]=2021-01-02'

    ### By status category

    Find all incidents that are in a status category. Possible values are \"triage\",
    \"declined\", \"merged\", \"canceled\", \"live\", \"learning\" and \"closed\":

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status_category[one_of]=live'

    Or all incidents that are not in a status category:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'status_category[not_in]=live'


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

    ### By incident mode

    By default, we return standard and retrospective incidents. This means that test and
    tutorial incidents are filtered out. To override this behaviour, you can use the
    mode filter to specify which modes you want to get.

    To find incidents of all modes:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'mode[one_of]=standard&mode[one_of]=retrospective&mode[one_of]=test&mode[one_of]=tutorial'

    To find just test incidents:

    		curl --get 'https://api.incident.io/v2/incidents' \
    			--data 'mode[one_of]=test'


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
        page_size (Union[Unset, int]):  Default: 25.
        after (Union[Unset, str]):
        status (Union[Unset, Any]):
        status_category (Union[Unset, Any]):
        created_at (Union[Unset, Any]):
        updated_at (Union[Unset, Any]):
        severity (Union[Unset, Any]):
        incident_type (Union[Unset, Any]):
        incident_role (Union[Unset, Any]):
        custom_field (Union[Unset, Any]):
        mode (Union[Unset, Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentsV2ListResponseBody
     """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            after=after,
            status=status,
            status_category=status_category,
            created_at=created_at,
            updated_at=updated_at,
            severity=severity,
            incident_type=incident_type,
            incident_role=incident_role,
            custom_field=custom_field,
            mode=mode,
        )
    ).parsed
