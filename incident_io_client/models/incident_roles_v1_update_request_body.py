from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentRolesV1UpdateRequestBody")


@_attrs_define
class IncidentRolesV1UpdateRequestBody:
    """
    Example:
        {'description': 'The person currently coordinating the incident', 'instructions': 'Take point on the incident;
            Make sure people are clear on responsibilities', 'name': 'Incident Lead', 'required': False, 'shortform':
            'lead'}

    Attributes:
        description (str): Describes the purpose of the role Example: The person currently coordinating the incident.
        instructions (str): Provided to whoever is nominated for the role. Note that this will be empty for the
            'reporter' role. Example: Take point on the incident; Make sure people are clear on responsibilities.
        name (str): Human readable name of the incident role Example: Incident Lead.
        shortform (str): Short human readable name for Slack. Note that this will be empty for the 'reporter' role.
            Example: lead.
        required (Union[Unset, bool]): DEPRECATED: this will always be false.
    """

    description: str
    instructions: str
    name: str
    shortform: str
    required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        instructions = self.instructions

        name = self.name

        shortform = self.shortform

        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "instructions": instructions,
                "name": name,
                "shortform": shortform,
            }
        )
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        instructions = d.pop("instructions")

        name = d.pop("name")

        shortform = d.pop("shortform")

        required = d.pop("required", UNSET)

        incident_roles_v1_update_request_body = cls(
            description=description,
            instructions=instructions,
            name=name,
            shortform=shortform,
            required=required,
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
