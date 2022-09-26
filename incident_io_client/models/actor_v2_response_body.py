from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_key_v2_response_body import APIKeyV2ResponseBody
from ..models.user_v2_response_body import UserV2ResponseBody
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActorV2ResponseBody")


@attr.s(auto_attribs=True)
class ActorV2ResponseBody:
    """
    Example:
        {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}}

    Attributes:
        api_key (Union[Unset, APIKeyV2ResponseBody]):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test
            API key'}.
        user (Union[Unset, UserV2ResponseBody]):  Example: {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}.
    """

    api_key: Union[Unset, APIKeyV2ResponseBody] = UNSET
    user: Union[Unset, UserV2ResponseBody] = UNSET
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
        api_key: Union[Unset, APIKeyV2ResponseBody]
        if isinstance(_api_key, Unset):
            api_key = UNSET
        else:
            api_key = APIKeyV2ResponseBody.from_dict(_api_key)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserV2ResponseBody]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserV2ResponseBody.from_dict(_user)

        actor_v2_response_body = cls(
            api_key=api_key,
            user=user,
        )

        actor_v2_response_body.additional_properties = d
        return actor_v2_response_body

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
