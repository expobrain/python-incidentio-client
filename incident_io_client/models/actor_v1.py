from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key_v1 import APIKeyV1
    from ..models.user_v1 import UserV1


T = TypeVar("T", bound="ActorV1")


@_attrs_define
class ActorV1:
    """
    Example:
        {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}}

    Attributes:
        api_key (Union[Unset, APIKeyV1]):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}.
        user (Union[Unset, UserV1]):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}.
    """

    api_key: Union[Unset, "APIKeyV1"] = UNSET
    user: Union[Unset, "UserV1"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        from ..models.api_key_v1 import APIKeyV1
        from ..models.user_v1 import UserV1

        d = src_dict.copy()
        _api_key = d.pop("api_key", UNSET)
        api_key: Union[Unset, APIKeyV1]
        if isinstance(_api_key, Unset):
            api_key = UNSET
        else:
            api_key = APIKeyV1.from_dict(_api_key)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserV1]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserV1.from_dict(_user)

        actor_v1 = cls(
            api_key=api_key,
            user=user,
        )

        actor_v1.additional_properties = d
        return actor_v1

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
