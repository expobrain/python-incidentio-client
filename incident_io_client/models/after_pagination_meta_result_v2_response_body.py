from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AfterPaginationMetaResultV2ResponseBody")


@_attrs_define
class AfterPaginationMetaResultV2ResponseBody:
    """
    Example:
        {'after': 'abc123', 'after_url': 'abc123'}

    Attributes:
        after (str): The time, if it exists, of the last entry's end time Example: abc123.
        after_url (str): The URL to fetch the next page of entries Example: abc123.
    """

    after: str
    after_url: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        after = self.after

        after_url = self.after_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "after": after,
                "after_url": after_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        after = d.pop("after")

        after_url = d.pop("after_url")

        after_pagination_meta_result_v2_response_body = cls(
            after=after,
            after_url=after_url,
        )

        after_pagination_meta_result_v2_response_body.additional_properties = d
        return after_pagination_meta_result_v2_response_body

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
