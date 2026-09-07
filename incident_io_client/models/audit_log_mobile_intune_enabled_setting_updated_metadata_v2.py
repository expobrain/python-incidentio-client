from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogMobileIntuneEnabledSettingUpdatedMetadataV2")


@_attrs_define
class AuditLogMobileIntuneEnabledSettingUpdatedMetadataV2:
    """
    Example:
        {'enabled': 'true'}

    Attributes:
        enabled (Union[Unset, str]): Whether Intune is enabled after the update Example: true.
    """

    enabled: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        audit_log_mobile_intune_enabled_setting_updated_metadata_v2 = cls(
            enabled=enabled,
        )

        audit_log_mobile_intune_enabled_setting_updated_metadata_v2.additional_properties = d
        return audit_log_mobile_intune_enabled_setting_updated_metadata_v2

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
