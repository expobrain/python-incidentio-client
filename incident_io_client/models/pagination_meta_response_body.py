from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginationMetaResponseBody")


@attr.s(auto_attribs=True)
class PaginationMetaResponseBody:
    """
    Example:
        {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25, 'total_record_count': 238}

    Attributes:
        page_size (int): What was the maximum number of results requested Example: 25.
        total_record_count (int): How many matching records were there in total Example: 238.
        after (Union[Unset, str]): If provided, were records after a particular ID Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    page_size: int
    total_record_count: int
    after: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_size = self.page_size
        total_record_count = self.total_record_count
        after = self.after

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page_size": page_size,
                "total_record_count": total_record_count,
            }
        )
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page_size = d.pop("page_size")

        total_record_count = d.pop("total_record_count")

        after = d.pop("after", UNSET)

        pagination_meta_response_body = cls(
            page_size=page_size,
            total_record_count=total_record_count,
            after=after,
        )

        pagination_meta_response_body.additional_properties = d
        return pagination_meta_response_body

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
