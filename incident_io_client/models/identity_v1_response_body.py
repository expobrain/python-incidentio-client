from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identity_v1_response_body_roles_item import (
    IdentityV1ResponseBodyRolesItem,
)

T = TypeVar("T", bound="IdentityV1ResponseBody")


@_attrs_define
class IdentityV1ResponseBody:
    """
    Example:
        {'name': 'Alertmanager token', 'roles': ['incident_creator']}

    Attributes:
        name (str): The name assigned to the current API Key Example: Alertmanager token.
        roles (List[IdentityV1ResponseBodyRolesItem]): Which roles have been enabled for this key Example:
            ['incident_creator'].
    """

    name: str
    roles: List[IdentityV1ResponseBodyRolesItem]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.value

            roles.append(roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "roles": roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = IdentityV1ResponseBodyRolesItem(roles_item_data)

            roles.append(roles_item)

        identity_v1_response_body = cls(
            name=name,
            roles=roles,
        )

        identity_v1_response_body.additional_properties = d
        return identity_v1_response_body

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
