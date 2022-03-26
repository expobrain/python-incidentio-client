from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_key_response_body import APIKeyResponseBody
from ..models.user_response_body import UserResponseBody
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActorResponseBody")


@attr.s(auto_attribs=True)
class ActorResponseBody:
    """
    Example:
        {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer'}}

    Attributes:
        api_key (Union[Unset, APIKeyResponseBody]):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API
            key'}.
        user (Union[Unset, UserResponseBody]):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'viewer'}.
    """

    api_key: Union[Unset, APIKeyResponseBody] = UNSET
    user: Union[Unset, UserResponseBody] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api_key, Unset):
            api_key = self.api_key.to_dict()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _api_key = d.pop("api_key", UNSET)
        api_key: Union[Unset, APIKeyResponseBody]
        if isinstance(_api_key, Unset):
            api_key = UNSET
        else:
            api_key = APIKeyResponseBody.from_dict(_api_key)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserResponseBody]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserResponseBody.from_dict(_user)

        actor_response_body = cls(
            api_key=api_key,
            user=user,
        )

        actor_response_body.additional_properties = d
        return actor_response_body

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
