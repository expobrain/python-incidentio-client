from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.user_response_body_role import UserResponseBodyRole

T = TypeVar("T", bound="UserResponseBody")


@attr.s(auto_attribs=True)
class UserResponseBody:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer'}

    Attributes:
        id (str): Unique identifier of the user Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Name of the user Example: Lisa Karlin Curtis.
        role (UserResponseBodyRole): Role of the user Example: viewer.
    """

    id: str
    name: str
    role: UserResponseBodyRole
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        role = UserResponseBodyRole(d.pop("role"))

        user_response_body = cls(
            id=id,
            name=name,
            role=role,
        )

        user_response_body.additional_properties = d
        return user_response_body

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
