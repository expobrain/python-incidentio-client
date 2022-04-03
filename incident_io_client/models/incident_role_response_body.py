from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="IncidentRoleResponseBody")


@attr.s(auto_attribs=True)
class IncidentRoleResponseBody:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'lead_role': True, 'name': 'Incident Lead', 'required': True, 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        description (str): Describes the purpose of the role Example: The person currently coordinating the incident.
        id (str): Unique identifier for the role Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        instructions (str): Provided to whoever is nominated for the role Example: Take point on the incident; Make sure
            people are clear on responsibilities.
        lead_role (bool): Whether this role is the special lead role Example: True.
        name (str): Human readable name of the incident role Example: Incident Lead.
        required (bool): Whether incident require this role to be set Example: True.
        shortform (str): Short human readable name for Slack Example: lead.
    """

    description: str
    id: str
    instructions: str
    lead_role: bool
    name: str
    required: bool
    shortform: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        id = self.id
        instructions = self.instructions
        lead_role = self.lead_role
        name = self.name
        required = self.required
        shortform = self.shortform

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "id": id,
                "instructions": instructions,
                "lead_role": lead_role,
                "name": name,
                "required": required,
                "shortform": shortform,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        id = d.pop("id")

        instructions = d.pop("instructions")

        lead_role = d.pop("lead_role")

        name = d.pop("name")

        required = d.pop("required")

        shortform = d.pop("shortform")

        incident_role_response_body = cls(
            description=description,
            id=id,
            instructions=instructions,
            lead_role=lead_role,
            name=name,
            required=required,
            shortform=shortform,
        )

        incident_role_response_body.additional_properties = d
        return incident_role_response_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
