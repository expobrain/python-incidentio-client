from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="IdentityV1ResponseBody")


@attr.s(auto_attribs=True)
class IdentityV1ResponseBody:
    """
    Example:
        {'name': 'Aut enim quisquam accusamus ratione.', 'roles': ['Officia accusamus magni sit eligendi aperiam.',
            'Ratione a non.']}

    Attributes:
        name (str): The name assigned to the current API Key Example: Voluptatem exercitationem dicta..
        roles (List[str]): Which roles have been enabled for this key. Available roles are viewer, incident_creator,
            global_access, manage_settings. Example: ['Magni et tenetur quo aspernatur.', 'Est consequuntur nesciunt.', 'Ut
            architecto labore.'].
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
