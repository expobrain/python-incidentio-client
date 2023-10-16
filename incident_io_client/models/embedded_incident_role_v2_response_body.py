import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.embedded_incident_role_v2_response_body_role_type import (
    EmbeddedIncidentRoleV2ResponseBodyRoleType,
)

T = TypeVar("T", bound="EmbeddedIncidentRoleV2ResponseBody")


@_attrs_define
class EmbeddedIncidentRoleV2ResponseBody:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'The person currently coordinating the incident',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'instructions': 'Take point on the incident; Make sure people are clear on
            responsibilities', 'name': 'Incident Lead', 'required': True, 'role_type': 'lead', 'shortform': 'lead',
            'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When the action was created Example: 2021-08-17T13:28:57.801578Z.
        description (str): Describes the purpose of the role Example: The person currently coordinating the incident.
        id (str): Unique identifier for the role Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        instructions (str): Provided to whoever is nominated for the role Example: Take point on the incident; Make sure
            people are clear on responsibilities.
        name (str): Human readable name of the incident role Example: Incident Lead.
        required (bool): This field is deprecated. Example: True.
        role_type (EmbeddedIncidentRoleV2ResponseBodyRoleType): Type of incident role Example: lead.
        shortform (str): Short human readable name for Slack Example: lead.
        updated_at (datetime.datetime): When the action was last updated Example: 2021-08-17T13:28:57.801578Z.
    """

    created_at: datetime.datetime
    description: str
    id: str
    instructions: str
    name: str
    required: bool
    role_type: EmbeddedIncidentRoleV2ResponseBodyRoleType
    shortform: str
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description
        id = self.id
        instructions = self.instructions
        name = self.name
        required = self.required
        role_type = self.role_type.value

        shortform = self.shortform
        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "id": id,
                "instructions": instructions,
                "name": name,
                "required": required,
                "role_type": role_type,
                "shortform": shortform,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        description = d.pop("description")

        id = d.pop("id")

        instructions = d.pop("instructions")

        name = d.pop("name")

        required = d.pop("required")

        role_type = EmbeddedIncidentRoleV2ResponseBodyRoleType(d.pop("role_type"))

        shortform = d.pop("shortform")

        updated_at = isoparse(d.pop("updated_at"))

        embedded_incident_role_v2_response_body = cls(
            created_at=created_at,
            description=description,
            id=id,
            instructions=instructions,
            name=name,
            required=required,
            role_type=role_type,
            shortform=shortform,
            updated_at=updated_at,
        )

        embedded_incident_role_v2_response_body.additional_properties = d
        return embedded_incident_role_v2_response_body

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
