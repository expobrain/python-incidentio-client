from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_with_roles_v2 import UserWithRolesV2


T = TypeVar("T", bound="UsersV2ShowResponseBody")


@_attrs_define
class UsersV2ShowResponseBody:
    """
    Example:
        {'user': {'base_role': {'description': 'Elevated permissions for the customer success team.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug': 'customer-success'}, 'custom_roles':
            [{'description': 'Elevated permissions for the customer success team.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Customer Success', 'slug': 'customer-success'}], 'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}}

    Attributes:
        user (UserWithRolesV2):  Example: {'base_role': {'description': 'Elevated permissions for the customer success
            team.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug': 'customer-success'},
            'custom_roles': [{'description': 'Elevated permissions for the customer success team.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug': 'customer-success'}], 'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}.
    """

    user: "UserWithRolesV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_with_roles_v2 import UserWithRolesV2

        d = src_dict.copy()
        user = UserWithRolesV2.from_dict(d.pop("user"))

        users_v2_show_response_body = cls(
            user=user,
        )

        users_v2_show_response_body.additional_properties = d
        return users_v2_show_response_body

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
