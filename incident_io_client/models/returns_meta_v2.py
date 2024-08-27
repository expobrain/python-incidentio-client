from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReturnsMetaV2")


@_attrs_define
class ReturnsMetaV2:
    """
    Example:
        {'array': True, 'type': 'IncidentStatus'}

    Attributes:
        array (bool): Whether the return value should be single or multi-value Example: True.
        type (str): Expected return type of this expression (what to try casting the result to) Example: IncidentStatus.
    """

    array: bool
    type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        array = self.array

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        array = d.pop("array")

        type = d.pop("type")

        returns_meta_v2 = cls(
            array=array,
            type=type,
        )

        returns_meta_v2.additional_properties = d
        return returns_meta_v2

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
