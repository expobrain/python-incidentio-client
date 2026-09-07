from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.grouping_settings_v3 import GroupingSettingsV3


T = TypeVar("T", bound="AlertGroupingConfigV3")


@_attrs_define
class AlertGroupingConfigV3:
    """
    Example:
        {'default': {'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}], 'window_seconds': 1800,
            'window_type': 'rolling'}}

    Attributes:
        default (GroupingSettingsV3):  Example: {'enabled': True, 'grouping_keys': [{'reference': 'alert.title'}],
            'window_seconds': 1800, 'window_type': 'rolling'}.
    """

    default: "GroupingSettingsV3"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default = self.default.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default": default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.grouping_settings_v3 import GroupingSettingsV3

        d = src_dict.copy()
        default = GroupingSettingsV3.from_dict(d.pop("default"))

        alert_grouping_config_v3 = cls(
            default=default,
        )

        alert_grouping_config_v3.additional_properties = d
        return alert_grouping_config_v3

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
