from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="APIKeyV1ResponseBody")


@attr.s(auto_attribs=True)
class APIKeyV1ResponseBody:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}

    Attributes:
        id (str): Unique identifier for this API key Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): The name of the API key, for the user's reference Example: My test API key.
    """

    id: str
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        api_key_v1_response_body = cls(
            id=id,
            name=name,
        )

        api_key_v1_response_body.additional_properties = d
        return api_key_v1_response_body

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
