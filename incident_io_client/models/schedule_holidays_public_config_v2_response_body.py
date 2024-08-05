from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScheduleHolidaysPublicConfigV2ResponseBody")


@_attrs_define
class ScheduleHolidaysPublicConfigV2ResponseBody:
    """
    Example:
        {'country_codes': ['GB', 'FR']}

    Attributes:
        country_codes (List[str]): ISO 3166-1 alpha-2 country codes for the countries that this schedule is configured
            to view holidays for Example: ['GB', 'FR'].
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

        schedule_holidays_public_config_v2_response_body = cls(
            country_codes=country_codes,
        )

        schedule_holidays_public_config_v2_response_body.additional_properties = d
        return schedule_holidays_public_config_v2_response_body

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
