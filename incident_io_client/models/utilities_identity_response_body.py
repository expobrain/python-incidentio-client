from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.public_identity_response_body import PublicIdentityResponseBody

T = TypeVar("T", bound="UtilitiesIdentityResponseBody")


@attr.s(auto_attribs=True)
class UtilitiesIdentityResponseBody:
    """
    Example:
        {'identity': {'name': 'Et ut voluptates.', 'roles': ['Molestias ut voluptas excepturi eius tempora.', 'Id
            impedit aut quis repellat a delectus.']}}

    Attributes:
        identity (PublicIdentityResponseBody):  Example: {'name': 'Consequuntur nesciunt dolorum ut.', 'roles': ['Quia
            aut enim quisquam.', 'Ratione assumenda.', 'Officia accusamus magni sit eligendi aperiam.']}.
    """

    identity: PublicIdentityResponseBody
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
        identity = PublicIdentityResponseBody.from_dict(d.pop("identity"))

        utilities_identity_response_body = cls(
            identity=identity,
        )

        utilities_identity_response_body.additional_properties = d
        return utilities_identity_response_body

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
