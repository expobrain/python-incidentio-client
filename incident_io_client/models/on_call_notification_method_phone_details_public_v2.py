from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OnCallNotificationMethodPhoneDetailsPublicV2")


@_attrs_define
class OnCallNotificationMethodPhoneDetailsPublicV2:
    """
    Example:
        {'supports_sms': True, 'supports_voice': True}

    Attributes:
        supports_sms (bool): Whether this phone number can receive SMS notifications. Example: True.
        supports_voice (bool): Whether this phone number can receive voice call notifications. Example: True.
    """

    supports_sms: bool
    supports_voice: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supports_sms = self.supports_sms

        supports_voice = self.supports_voice

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "supports_sms": supports_sms,
                "supports_voice": supports_voice,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supports_sms = d.pop("supports_sms")

        supports_voice = d.pop("supports_voice")

        on_call_notification_method_phone_details_public_v2 = cls(
            supports_sms=supports_sms,
            supports_voice=supports_voice,
        )

        on_call_notification_method_phone_details_public_v2.additional_properties = d
        return on_call_notification_method_phone_details_public_v2

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
