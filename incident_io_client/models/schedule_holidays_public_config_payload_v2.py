from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScheduleHolidaysPublicConfigPayloadV2")


@_attrs_define
class ScheduleHolidaysPublicConfigPayloadV2:
    """
    Example:
        {'country_codes': ['abc123']}

    Attributes:
        country_codes (List[str]): ISO 3166-1 alpha-2 country codes for the countries that this schedule is configured
            to view holidays for Example: ['abc123'].
    """

    country_codes: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        country_codes = self.country_codes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country_codes": country_codes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        country_codes = cast(List[str], d.pop("country_codes"))

        schedule_holidays_public_config_payload_v2 = cls(
            country_codes=country_codes,
        )

        schedule_holidays_public_config_payload_v2.additional_properties = d
        return schedule_holidays_public_config_payload_v2

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
