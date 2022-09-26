from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeveritiesV1UpdateRequestBody")


@attr.s(auto_attribs=True)
class SeveritiesV1UpdateRequestBody:
    """
    Example:
        {'description': "It's not really that bad, everyone chill", 'name': 'Minor', 'rank': 1}

    Attributes:
        description (str): Description of the severity Example: It's not really that bad, everyone chill.
        name (str): Human readable name of the severity Example: Minor.
        rank (Union[Unset, int]): Rank to help sort severities (lower numbers are less severe) Example: 1.
    """

    description: str
    name: str
    rank: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name
        rank = self.rank

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
            }
        )
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        name = d.pop("name")

        rank = d.pop("rank", UNSET)

        severities_v1_update_request_body = cls(
            description=description,
            name=name,
            rank=rank,
        )

        severities_v1_update_request_body.additional_properties = d
        return severities_v1_update_request_body

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
