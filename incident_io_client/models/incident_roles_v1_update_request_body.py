from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="IncidentRolesV1UpdateRequestBody")


@attr.s(auto_attribs=True)
class IncidentRolesV1UpdateRequestBody:
    """
    Example:
        {'description': 'The person currently coordinating the incident', 'instructions': 'Take point on the incident;
            Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': True, 'shortform': 'lead'}

    Attributes:
        description (str): Describes the purpose of the role Example: The person currently coordinating the incident.
        instructions (str): Provided to whoever is nominated for the role Example: Take point on the incident; Make sure
            people are clear on responsibilities.
        name (str): Human readable name of the incident role Example: Incident Lead.
        required (bool): Whether incident require this role to be set Example: True.
        shortform (str): Short human readable name for Slack Example: lead.
    """

    description: str
    instructions: str
    name: str
    required: bool
    shortform: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        instructions = self.instructions
        name = self.name
        required = self.required
        shortform = self.shortform

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "instructions": instructions,
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

        instructions = d.pop("instructions")

        name = d.pop("name")

        required = d.pop("required")

        shortform = d.pop("shortform")

        incident_roles_v1_update_request_body = cls(
            description=description,
            instructions=instructions,
            name=name,
            required=required,
            shortform=shortform,
        )

        incident_roles_v1_update_request_body.additional_properties = d
        return incident_roles_v1_update_request_body

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
