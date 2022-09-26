from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_v1_response_body_role import UserV1ResponseBodyRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserV1ResponseBody")


@attr.s(auto_attribs=True)
class UserV1ResponseBody:
    """
    Example:
        {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'viewer', 'slack_user_id': 'U02AYNF2XJM'}

    Attributes:
        id (str): Unique identifier of the user Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Name of the user Example: Lisa Karlin Curtis.
        role (UserV1ResponseBodyRole): Role of the user Example: viewer.
        slack_user_id (str): Slack ID of the user Example: U02AYNF2XJM.
        email (Union[Unset, str]): Email address of the user. Example: lisa@incident.io.
    """

    id: str
    name: str
    role: UserV1ResponseBodyRole
    slack_user_id: str
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        role = self.role.value

        slack_user_id = self.slack_user_id
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "role": role,
                "slack_user_id": slack_user_id,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        role = UserV1ResponseBodyRole(d.pop("role"))

        slack_user_id = d.pop("slack_user_id")

        email = d.pop("email", UNSET)

        user_v1_response_body = cls(
            id=id,
            name=name,
            role=role,
            slack_user_id=slack_user_id,
            email=email,
        )

        user_v1_response_body.additional_properties = d
        return user_v1_response_body

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
