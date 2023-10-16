import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="SeverityV1ResponseBody")


@_attrs_define
class SeverityV1ResponseBody:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When the action was created Example: 2021-08-17T13:28:57.801578Z.
        description (str): Description of the severity Example: Issues with **low impact**..
        id (str): Unique identifier of the severity Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Human readable name of the severity Example: Minor.
        rank (int): Rank to help sort severities (lower numbers are less severe) Example: 1.
        updated_at (datetime.datetime): When the action was last updated Example: 2021-08-17T13:28:57.801578Z.
    """

    created_at: datetime.datetime
    description: str
    id: str
    name: str
    rank: int
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        created_at = isoparse(d.pop("created_at"))

        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        rank = d.pop("rank")

        updated_at = isoparse(d.pop("updated_at"))

        severity_v1_response_body = cls(
            created_at=created_at,
            description=description,
            id=id,
            name=name,
            rank=rank,
            updated_at=updated_at,
        )

        severity_v1_response_body.additional_properties = d
        return severity_v1_response_body

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
