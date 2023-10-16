from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_v2_response_body_role import UserV2ResponseBodyRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserV2ResponseBody")


@_attrs_define
class UserV2ResponseBody:
    """
    Example:
        {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
            'viewer', 'slack_user_id': 'U02AYNF2XJM'}

    Attributes:
        id (str): Unique identifier of the user Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Name of the user Example: Lisa Karlin Curtis.
        role (UserV2ResponseBodyRole): DEPRECATED: Role of the user as of March 9th 2023, this value is no longer
            updated. Example: viewer.
        email (Union[Unset, str]): Email address of the user. Example: lisa@incident.io.
        slack_user_id (Union[Unset, str]): Slack ID of the user Example: U02AYNF2XJM.
    """

    id: str
    name: str
    role: UserV2ResponseBodyRole
    email: Union[Unset, str] = UNSET
    slack_user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        role = self.role.value

        email = self.email
        slack_user_id = self.slack_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "role": role,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if slack_user_id is not UNSET:
            field_dict["slack_user_id"] = slack_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        role = UserV2ResponseBodyRole(d.pop("role"))

        email = d.pop("email", UNSET)

        slack_user_id = d.pop("slack_user_id", UNSET)

        user_v2_response_body = cls(
            id=id,
            name=name,
            role=role,
            email=email,
            slack_user_id=slack_user_id,
        )

        user_v2_response_body.additional_properties = d
        return user_v2_response_body

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
