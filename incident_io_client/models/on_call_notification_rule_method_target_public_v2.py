from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.on_call_notification_rule_method_target_public_v2_type import (
    OnCallNotificationRuleMethodTargetPublicV2Type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.on_call_notification_rule_method_target_all_public_v2 import (
        OnCallNotificationRuleMethodTargetAllPublicV2,
    )
    from ..models.on_call_notification_rule_method_target_specific_public_v2 import (
        OnCallNotificationRuleMethodTargetSpecificPublicV2,
    )


T = TypeVar("T", bound="OnCallNotificationRuleMethodTargetPublicV2")


@_attrs_define
class OnCallNotificationRuleMethodTargetPublicV2:
    """
    Example:
        {'all': {}, 'specific': {'id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'specific'}

    Attributes:
        type (OnCallNotificationRuleMethodTargetPublicV2Type): Whether this targets a specific method or all methods of
            a given type. Example: specific.
        all_ (Union[Unset, OnCallNotificationRuleMethodTargetAllPublicV2]):
        specific (Union[Unset, OnCallNotificationRuleMethodTargetSpecificPublicV2]):  Example: {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}.
    """

    type: OnCallNotificationRuleMethodTargetPublicV2Type
    all_: Union[Unset, "OnCallNotificationRuleMethodTargetAllPublicV2"] = UNSET
    specific: Union[Unset, "OnCallNotificationRuleMethodTargetSpecificPublicV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        all_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.all_, Unset):
            all_ = self.all_.to_dict()

        specific: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.specific, Unset):
            specific = self.specific.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if all_ is not UNSET:
            field_dict["all"] = all_
        if specific is not UNSET:
            field_dict["specific"] = specific

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.on_call_notification_rule_method_target_all_public_v2 import (
            OnCallNotificationRuleMethodTargetAllPublicV2,
        )
        from ..models.on_call_notification_rule_method_target_specific_public_v2 import (
            OnCallNotificationRuleMethodTargetSpecificPublicV2,
        )

        d = src_dict.copy()
        type = OnCallNotificationRuleMethodTargetPublicV2Type(d.pop("type"))

        _all_ = d.pop("all", UNSET)
        all_: Union[Unset, OnCallNotificationRuleMethodTargetAllPublicV2]
        if isinstance(_all_, Unset):
            all_ = UNSET
        else:
            all_ = OnCallNotificationRuleMethodTargetAllPublicV2.from_dict(_all_)

        _specific = d.pop("specific", UNSET)
        specific: Union[Unset, OnCallNotificationRuleMethodTargetSpecificPublicV2]
        if isinstance(_specific, Unset):
            specific = UNSET
        else:
            specific = OnCallNotificationRuleMethodTargetSpecificPublicV2.from_dict(
                _specific
            )

        on_call_notification_rule_method_target_public_v2 = cls(
            type=type,
            all_=all_,
            specific=specific,
        )

        on_call_notification_rule_method_target_public_v2.additional_properties = d
        return on_call_notification_rule_method_target_public_v2

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
