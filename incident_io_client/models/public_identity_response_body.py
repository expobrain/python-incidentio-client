from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="PublicIdentityResponseBody")


@attr.s(auto_attribs=True)
class PublicIdentityResponseBody:
    """
    Example:
        {'name': 'Consequuntur nesciunt dolorum ut.', 'roles': ['Quia aut enim quisquam.', 'Ratione assumenda.',
            'Officia accusamus magni sit eligendi aperiam.']}

    Attributes:
        name (str): The name assigned to the current API Key Example: Quos quod..
        roles (List[str]): Which roles have been enabled for this key. Available roles are viewer, incident_creator,
            global_access, manage_settings. Example: ['Aspernatur quia eveniet voluptatem exercitationem dicta.', 'Enim hic
            est.', 'Fugiat magni et tenetur.', 'Aspernatur sunt.'].
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
