from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginationMetaResultResponseBody")


@_attrs_define
class PaginationMetaResultResponseBody:
    """
    Example:
        {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}

    Attributes:
        page_size (int): What was the maximum number of results requested Default: 25. Example: 25.
        after (Union[Unset, str]): If provided, pass this as the 'after' param to load the next page Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
    """

    page_size: int = 25
    after: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_size = self.page_size
        after = self.after

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page_size": page_size,
            }
        )
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page_size = d.pop("page_size")

        after = d.pop("after", UNSET)

        pagination_meta_result_response_body = cls(
            page_size=page_size,
            after=after,
        )

        pagination_meta_result_response_body.additional_properties = d
        return pagination_meta_result_response_body

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
