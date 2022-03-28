import asyncio
import os

from dotenv import load_dotenv

from incident_io_client import AuthenticatedClient
from incident_io_client.api.actions import actions_list, actions_show
from incident_io_client.api.custom_fields import custom_fields_list, custom_fields_show
from incident_io_client.api.incident_roles import (
    incident_roles_list,
    incident_roles_show,
)
from incident_io_client.api.incidents import incidents_list, incidents_show
from incident_io_client.api.severities import severities_list, severities_show

load_dotenv()

token = os.environ["INCIDENT_IO_TOKEN"]
url = "https://api.incident.io"


async def main() -> None:
    # Create client
    client = AuthenticatedClient(base_url=url, token=token)

    # ----------------------------------------------------------------
    # Actions
    # ----------------------------------------------------------------

    # List all actions
    actions_response = await actions_list.asyncio(client=client)
    assert actions_response

    print(actions_response.actions)

    # Show single action
    action_id = actions_response.actions[0].id

    action_response = await actions_show.asyncio(action_id, client=client)
    assert action_response

    print(action_response.action)

    # ----------------------------------------------------------------
    # Custom fields
    # ----------------------------------------------------------------

    # List all custom fields
    custom_fields_response = await custom_fields_list.asyncio(client=client)
    assert custom_fields_response

    print(custom_fields_response.custom_fields)

    # Show single custom field
    custom_field_id = custom_fields_response.custom_fields[0].id

    custom_field_response = await custom_fields_show.asyncio(custom_field_id, client=client)
    assert custom_field_response

    print(custom_field_response.custom_field)

    # ----------------------------------------------------------------
    # Incident roles
    # ----------------------------------------------------------------

    # List all incident roles
    incident_roles_response = await incident_roles_list.asyncio(client=client)
    assert incident_roles_response

    print(incident_roles_response.incident_roles)

    # Show single incident role
    incident_role_id = incident_roles_response.incident_roles[0].id

    incident_role_response = await incident_roles_show.asyncio(incident_role_id, client=client)
    assert incident_role_response

    print(incident_role_response.incident_role)

    # ----------------------------------------------------------------
    # Severities
    # ----------------------------------------------------------------

    # List all severities
    severities_response = await severities_list.asyncio(client=client)
    assert severities_response

    print(severities_response.severities)

    # Show single severity
    severityid = severities_response.severities[0].id

    severityresponse = await severities_show.asyncio(severityid, client=client)
    assert severityresponse

    print(severityresponse.severity)

    # ----------------------------------------------------------------
    # Incidents
    # ----------------------------------------------------------------

    # List all incidents
    incidents_response = await incidents_list.asyncio(client=client)
    assert incidents_response

    print(incidents_response.incidents)

    # Show single incident
    incident_id = incidents_response.incidents[0].id

    incident_response = await incidents_show.asyncio(incident_id, client=client)
    assert incident_response

    print(incident_response.incident)


if __name__ == "__main__":
    asyncio.run(main())
