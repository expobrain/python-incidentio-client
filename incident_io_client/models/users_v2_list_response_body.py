from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination_meta_result import PaginationMetaResult
    from ..models.user_with_roles_v2 import UserWithRolesV2


T = TypeVar("T", bound="UsersV2ListResponseBody")


@_attrs_define
class UsersV2ListResponseBody:
    """
    Example:
        {'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}, 'users': [{'base_role':
            {'description': 'Elevated permissions for the customer success team.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Customer Success', 'slug': 'customer-success'}, 'custom_roles': [{'description': 'Elevated permissions
            for the customer success team.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug':
            'customer-success'}], 'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}]}

    Attributes:
        pagination_meta (PaginationMetaResult):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}.
        users (List['UserWithRolesV2']):  Example: [{'base_role': {'description': 'Elevated permissions for the customer
            success team.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug': 'customer-success'},
            'custom_roles': [{'description': 'Elevated permissions for the customer success team.', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Customer Success', 'slug': 'customer-success'}], 'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}].
    """

    pagination_meta: "PaginationMetaResult"
    users: List["UserWithRolesV2"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination_meta = self.pagination_meta.to_dict()

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination_meta": pagination_meta,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pagination_meta_result import PaginationMetaResult
        from ..models.user_with_roles_v2 import UserWithRolesV2

        d = src_dict.copy()
        pagination_meta = PaginationMetaResult.from_dict(d.pop("pagination_meta"))

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = UserWithRolesV2.from_dict(users_item_data)

            users.append(users_item)

        users_v2_list_response_body = cls(
            pagination_meta=pagination_meta,
            users=users,
        )

        users_v2_list_response_body.additional_properties = d
        return users_v2_list_response_body

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
