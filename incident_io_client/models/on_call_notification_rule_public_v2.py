from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.on_call_notification_rule_public_v2_method_type import (
    OnCallNotificationRulePublicV2MethodType,
)
from ..models.on_call_notification_rule_public_v2_rule_type import (
    OnCallNotificationRulePublicV2RuleType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.on_call_notification_rule_app_details_public_v2 import (
        OnCallNotificationRuleAppDetailsPublicV2,
    )
    from ..models.on_call_notification_rule_method_target_public_v2 import (
        OnCallNotificationRuleMethodTargetPublicV2,
    )
    from ..models.on_call_notification_rule_phone_details_public_v2 import (
        OnCallNotificationRulePhoneDetailsPublicV2,
    )


T = TypeVar("T", bound="OnCallNotificationRulePublicV2")


@_attrs_define
class OnCallNotificationRulePublicV2:
    """
    Example:
        {'app': {'push_notification_criticality': 'critical'}, 'delay_seconds': 0, 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'method_target': {'all': {}, 'specific': {'id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'specific'},
            'method_type': 'app', 'phone': {'channel': 'voice'}, 'rule_type': 'low_urgency'}

    Attributes:
        id (str): Unique identifier for this notification rule Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        method_target (OnCallNotificationRuleMethodTargetPublicV2):  Example: {'all': {}, 'specific': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'specific'}.
        method_type (OnCallNotificationRulePublicV2MethodType): The high-level type of notification method. Phone rules
            include phone details that distinguish SMS from voice calls. Example: app.
        rule_type (OnCallNotificationRulePublicV2RuleType): The urgency level this rule applies to Example: low_urgency.
        app (Union[Unset, OnCallNotificationRuleAppDetailsPublicV2]):  Example: {'push_notification_criticality':
            'critical'}.
        delay_seconds (Union[Unset, int]): Delay in seconds before this rule activates. 0 means immediate.
        phone (Union[Unset, OnCallNotificationRulePhoneDetailsPublicV2]):  Example: {'channel': 'voice'}.
    """

    id: str
    method_target: "OnCallNotificationRuleMethodTargetPublicV2"
    method_type: OnCallNotificationRulePublicV2MethodType
    rule_type: OnCallNotificationRulePublicV2RuleType
    app: Union[Unset, "OnCallNotificationRuleAppDetailsPublicV2"] = UNSET
    delay_seconds: Union[Unset, int] = UNSET
    phone: Union[Unset, "OnCallNotificationRulePhoneDetailsPublicV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        method_target = self.method_target.to_dict()

        method_type = self.method_type.value

        rule_type = self.rule_type.value

        app: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.app, Unset):
            app = self.app.to_dict()

        delay_seconds = self.delay_seconds

        phone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.phone, Unset):
            phone = self.phone.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "method_target": method_target,
                "method_type": method_type,
                "rule_type": rule_type,
            }
        )
        if app is not UNSET:
            field_dict["app"] = app
        if delay_seconds is not UNSET:
            field_dict["delay_seconds"] = delay_seconds
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.on_call_notification_rule_app_details_public_v2 import (
            OnCallNotificationRuleAppDetailsPublicV2,
        )
        from ..models.on_call_notification_rule_method_target_public_v2 import (
            OnCallNotificationRuleMethodTargetPublicV2,
        )
        from ..models.on_call_notification_rule_phone_details_public_v2 import (
            OnCallNotificationRulePhoneDetailsPublicV2,
        )

        d = src_dict.copy()
        id = d.pop("id")

        method_target = OnCallNotificationRuleMethodTargetPublicV2.from_dict(
            d.pop("method_target")
        )

        method_type = OnCallNotificationRulePublicV2MethodType(d.pop("method_type"))

        rule_type = OnCallNotificationRulePublicV2RuleType(d.pop("rule_type"))

        _app = d.pop("app", UNSET)
        app: Union[Unset, OnCallNotificationRuleAppDetailsPublicV2]
        if isinstance(_app, Unset):
            app = UNSET
        else:
            app = OnCallNotificationRuleAppDetailsPublicV2.from_dict(_app)

        delay_seconds = d.pop("delay_seconds", UNSET)

        _phone = d.pop("phone", UNSET)
        phone: Union[Unset, OnCallNotificationRulePhoneDetailsPublicV2]
        if isinstance(_phone, Unset):
            phone = UNSET
        else:
            phone = OnCallNotificationRulePhoneDetailsPublicV2.from_dict(_phone)

        on_call_notification_rule_public_v2 = cls(
            id=id,
            method_target=method_target,
            method_type=method_type,
            rule_type=rule_type,
            app=app,
            delay_seconds=delay_seconds,
            phone=phone,
        )

        on_call_notification_rule_public_v2.additional_properties = d
        return on_call_notification_rule_public_v2

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
