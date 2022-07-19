from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.incidents_create_request_body import IncidentsCreateRequestBody
from ...models.incidents_create_response_body import IncidentsCreateResponseBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: IncidentsCreateRequestBody,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v1/incidents"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncidentsCreateResponseBody]:
    if response.status_code == 200:
        response_200 = IncidentsCreateResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentsCreateResponseBody]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: IncidentsCreateRequestBody,
) -> Response[IncidentsCreateResponseBody]:
    """Create Incidents

     Create a new incident.

    Args:
        json_body (IncidentsCreateRequestBody):  Example: {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like
            it'}]}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like
            it'}]}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like
            it'}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments': [{'assignee':
            {'email': 'Dolore autem ea et voluptatem minus aut.', 'id': 'Ut doloribus porro et sit
            nihil.', 'slack_user_id': 'Alias aut rerum fugiat exercitationem maiores.'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee': {'email': 'Dolore autem ea
            et voluptatem minus aut.', 'id': 'Ut doloribus porro et sit nihil.', 'slack_user_id':
            'Alias aut rerum fugiat exercitationem maiores.'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee': {'email': 'Dolore autem ea et voluptatem minus
            aut.', 'id': 'Ut doloribus porro et sit nihil.', 'slack_user_id': 'Alias aut rerum fugiat
            exercitationem maiores.'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee':
            {'email': 'Dolore autem ea et voluptatem minus aut.', 'id': 'Ut doloribus porro et sit
            nihil.', 'slack_user_id': 'Alias aut rerum fugiat exercitationem maiores.'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_type_id': 'Aut repellendus
            voluptatem.', 'mode': 'real', 'name': 'Our database is sad', 'severity_id': 'Placeat quod
            aspernatur quia eveniet.', 'source_message_channel_id': 'C02AW36C1M5',
            'source_message_timestamp': '1653650280.526509', 'status': 'triage', 'summary': "Our
            database is really really sad, and we don't know why yet.", 'visibility': 'public'}.

    Returns:
        Response[IncidentsCreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: IncidentsCreateRequestBody,
) -> Optional[IncidentsCreateResponseBody]:
    """Create Incidents

     Create a new incident.

    Args:
        json_body (IncidentsCreateRequestBody):  Example: {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like
            it'}]}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like
            it'}]}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like
            it'}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments': [{'assignee':
            {'email': 'Dolore autem ea et voluptatem minus aut.', 'id': 'Ut doloribus porro et sit
            nihil.', 'slack_user_id': 'Alias aut rerum fugiat exercitationem maiores.'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee': {'email': 'Dolore autem ea
            et voluptatem minus aut.', 'id': 'Ut doloribus porro et sit nihil.', 'slack_user_id':
            'Alias aut rerum fugiat exercitationem maiores.'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee': {'email': 'Dolore autem ea et voluptatem minus
            aut.', 'id': 'Ut doloribus porro et sit nihil.', 'slack_user_id': 'Alias aut rerum fugiat
            exercitationem maiores.'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee':
            {'email': 'Dolore autem ea et voluptatem minus aut.', 'id': 'Ut doloribus porro et sit
            nihil.', 'slack_user_id': 'Alias aut rerum fugiat exercitationem maiores.'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_type_id': 'Aut repellendus
            voluptatem.', 'mode': 'real', 'name': 'Our database is sad', 'severity_id': 'Placeat quod
            aspernatur quia eveniet.', 'source_message_channel_id': 'C02AW36C1M5',
            'source_message_timestamp': '1653650280.526509', 'status': 'triage', 'summary': "Our
            database is really really sad, and we don't know why yet.", 'visibility': 'public'}.

    Returns:
        Response[IncidentsCreateResponseBody]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: IncidentsCreateRequestBody,
) -> Response[IncidentsCreateResponseBody]:
    """Create Incidents

     Create a new incident.

    Args:
        json_body (IncidentsCreateRequestBody):  Example: {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like
            it'}]}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like
            it'}]}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like
            it'}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments': [{'assignee':
            {'email': 'Dolore autem ea et voluptatem minus aut.', 'id': 'Ut doloribus porro et sit
            nihil.', 'slack_user_id': 'Alias aut rerum fugiat exercitationem maiores.'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee': {'email': 'Dolore autem ea
            et voluptatem minus aut.', 'id': 'Ut doloribus porro et sit nihil.', 'slack_user_id':
            'Alias aut rerum fugiat exercitationem maiores.'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee': {'email': 'Dolore autem ea et voluptatem minus
            aut.', 'id': 'Ut doloribus porro et sit nihil.', 'slack_user_id': 'Alias aut rerum fugiat
            exercitationem maiores.'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee':
            {'email': 'Dolore autem ea et voluptatem minus aut.', 'id': 'Ut doloribus porro et sit
            nihil.', 'slack_user_id': 'Alias aut rerum fugiat exercitationem maiores.'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_type_id': 'Aut repellendus
            voluptatem.', 'mode': 'real', 'name': 'Our database is sad', 'severity_id': 'Placeat quod
            aspernatur quia eveniet.', 'source_message_channel_id': 'C02AW36C1M5',
            'source_message_timestamp': '1653650280.526509', 'status': 'triage', 'summary': "Our
            database is really really sad, and we don't know why yet.", 'visibility': 'public'}.

    Returns:
        Response[IncidentsCreateResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: IncidentsCreateRequestBody,
) -> Optional[IncidentsCreateResponseBody]:
    """Create Incidents

     Create a new incident.

    Args:
        json_body (IncidentsCreateRequestBody):  Example: {'custom_field_entries':
            [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like
            it'}]}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like
            it'}]}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric':
            '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text
            field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like
            it'}]}], 'idempotency_key': 'alert-uuid', 'incident_role_assignments': [{'assignee':
            {'email': 'Dolore autem ea et voluptatem minus aut.', 'id': 'Ut doloribus porro et sit
            nihil.', 'slack_user_id': 'Alias aut rerum fugiat exercitationem maiores.'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee': {'email': 'Dolore autem ea
            et voluptatem minus aut.', 'id': 'Ut doloribus porro et sit nihil.', 'slack_user_id':
            'Alias aut rerum fugiat exercitationem maiores.'}, 'incident_role_id':
            '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee': {'email': 'Dolore autem ea et voluptatem minus
            aut.', 'id': 'Ut doloribus porro et sit nihil.', 'slack_user_id': 'Alias aut rerum fugiat
            exercitationem maiores.'}, 'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}, {'assignee':
            {'email': 'Dolore autem ea et voluptatem minus aut.', 'id': 'Ut doloribus porro et sit
            nihil.', 'slack_user_id': 'Alias aut rerum fugiat exercitationem maiores.'},
            'incident_role_id': '01FH5TZRWMNAFB0DZ23FD1TV96'}], 'incident_type_id': 'Aut repellendus
            voluptatem.', 'mode': 'real', 'name': 'Our database is sad', 'severity_id': 'Placeat quod
            aspernatur quia eveniet.', 'source_message_channel_id': 'C02AW36C1M5',
            'source_message_timestamp': '1653650280.526509', 'status': 'triage', 'summary': "Our
            database is really really sad, and we don't know why yet.", 'visibility': 'public'}.

    Returns:
        Response[IncidentsCreateResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
