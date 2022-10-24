from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.identity_v1_response_body import IdentityV1ResponseBody

T = TypeVar("T", bound="UtilitiesV1IdentityResponseBody")


@attr.s(auto_attribs=True)
class UtilitiesV1IdentityResponseBody:
    """
    Example:
        {'identity': {'name': 'Alertmanager token', 'roles': ['viewer', 'incident_creator', 'manage_settings',
            'manage_settings']}}

    Attributes:
        identity (IdentityV1ResponseBody):  Example: {'name': 'Alertmanager token', 'roles': ['manage_settings',
            'viewer']}.
    """

    identity: IdentityV1ResponseBody
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identity = self.identity.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identity": identity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identity = IdentityV1ResponseBody.from_dict(d.pop("identity"))

        utilities_v1_identity_response_body = cls(
            identity=identity,
        )

        utilities_v1_identity_response_body.additional_properties = d
        return utilities_v1_identity_response_body

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
