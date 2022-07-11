from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="PublicIdentityResponseBody")


@attr.s(auto_attribs=True)
class PublicIdentityResponseBody:
    """
    Example:
        {'name': 'Et officia accusamus magni.', 'roles': ['Aperiam veniam ratione a non qui.', 'Nulla ipsum atque animi
            ea qui et.', 'Voluptas nemo laudantium qui.', 'Nihil et consectetur et est.']}

    Attributes:
        name (str): The name assigned to the current API Key Example: Exercitationem dicta soluta enim..
        roles (List[str]): Which roles have been enabled for this key. Available roles are viewer, incident_creator,
            global_access, manage_settings. Example: ['Est consequuntur nesciunt.', 'Ut architecto labore.', 'Aut enim
            quisquam accusamus ratione.'].
    """

    name: str
    roles: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        roles = self.roles

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

        roles = cast(List[str], d.pop("roles"))

        public_identity_response_body = cls(
            name=name,
            roles=roles,
        )

        public_identity_response_body.additional_properties = d
        return public_identity_response_body

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
