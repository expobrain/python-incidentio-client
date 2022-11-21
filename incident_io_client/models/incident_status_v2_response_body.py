import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.incident_status_v2_response_body_category import (
    IncidentStatusV2ResponseBodyCategory,
)

T = TypeVar("T", bound="IncidentStatusV2ResponseBody")


@attr.s(auto_attribs=True)
class IncidentStatusV2ResponseBody:
    """
    Example:
        {'category': 'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully
            mitigated**, and we're ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name':
            'Closed', 'rank': 4, 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        category (IncidentStatusV2ResponseBodyCategory): Whether this status is a live or closed status. If you have
            enabled auto-create, there will also be 'triage' and 'declined' statuses, which cannot be modified. Example:
            triage.
        created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        description (str): Rich text description of the incident status Example: Impact has been **fully mitigated**,
            and we're ready to learn from this incident..
        id (str): Unique ID of this incident status Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        name (str): Unique name of this status Example: Closed.
        rank (int): Order of this incident status Example: 4.
        updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
    """

    category: IncidentStatusV2ResponseBodyCategory
    created_at: datetime.datetime
    description: str
    id: str
    name: str
    rank: int
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category.value

        created_at = self.created_at.isoformat()

        description = self.description
        id = self.id
        name = self.name
        rank = self.rank
        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "created_at": created_at,
                "description": description,
                "id": id,
                "name": name,
                "rank": rank,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = IncidentStatusV2ResponseBodyCategory(d.pop("category"))

        created_at = isoparse(d.pop("created_at"))

        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        rank = d.pop("rank")

        updated_at = isoparse(d.pop("updated_at"))

        incident_status_v2_response_body = cls(
            category=category,
            created_at=created_at,
            description=description,
            id=id,
            name=name,
            rank=rank,
            updated_at=updated_at,
        )

        incident_status_v2_response_body.additional_properties = d
        return incident_status_v2_response_body

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
