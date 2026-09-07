from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogOnCallNotificationMethodMetadataV2")


@_attrs_define
class AuditLogOnCallNotificationMethodMetadataV2:
    """
    Example:
        {'target_user': '01JV9EMFCFRGCFVNDWTBKT2EBR'}

    Attributes:
        target_user (Union[Unset, str]): The user whose notification method was created or destroyed Example:
            01JV9EMFCFRGCFVNDWTBKT2EBR.
    """

    target_user: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target_user = self.target_user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_user is not UNSET:
            field_dict["target_user"] = target_user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        target_user = d.pop("target_user", UNSET)

        audit_log_on_call_notification_method_metadata_v2 = cls(
            target_user=target_user,
        )

        audit_log_on_call_notification_method_metadata_v2.additional_properties = d
        return audit_log_on_call_notification_method_metadata_v2

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
