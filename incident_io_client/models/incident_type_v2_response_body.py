import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="IncidentTypeV2ResponseBody")


@attr.s(auto_attribs=True)
class IncidentTypeV2ResponseBody:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Customer facing production outages', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_default': True, 'name': 'Production Outage', 'private_incidents_only': False,
            'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When this resource was created Example: 2021-08-17T13:28:57.801578Z.
        description (str): What is this incident type for? Example: Customer facing production outages.
        id (str): Unique identifier for this Incident Type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        is_default (bool): The default Incident Type is used when no other type is explicitly specified Example: True.
        name (str): The name of this Incident Type Example: Production Outage.
        private_incidents_only (bool): Should all incidents created with this Incident Type be private?
        updated_at (datetime.datetime): When this resource was last updated Example: 2021-08-17T13:28:57.801578Z.
    """

    created_at: datetime.datetime
    description: str
    id: str
    is_default: bool
    name: str
    private_incidents_only: bool
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description
        id = self.id
        is_default = self.is_default
        name = self.name
        private_incidents_only = self.private_incidents_only
        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "id": id,
                "is_default": is_default,
                "name": name,
                "private_incidents_only": private_incidents_only,
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

        is_default = d.pop("is_default")

        name = d.pop("name")

        private_incidents_only = d.pop("private_incidents_only")

        updated_at = isoparse(d.pop("updated_at"))

        incident_type_v2_response_body = cls(
            created_at=created_at,
            description=description,
            id=id,
            is_default=is_default,
            name=name,
            private_incidents_only=private_incidents_only,
            updated_at=updated_at,
        )

        incident_type_v2_response_body.additional_properties = d
        return incident_type_v2_response_body

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
