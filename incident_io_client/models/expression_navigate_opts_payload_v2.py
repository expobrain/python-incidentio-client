from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExpressionNavigateOptsPayloadV2")


@_attrs_define
class ExpressionNavigateOptsPayloadV2:
    """
    Example:
        {'reference': 'catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"]'}

    Attributes:
        reference (str): The reference that you want to navigate to Example:
            catalog_attribute["01FCNDV6P870EA6S7TK1DSYD5H"].
    """

    reference: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference = self.reference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reference": reference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reference = d.pop("reference")

        expression_navigate_opts_payload_v2 = cls(
            reference=reference,
        )

        expression_navigate_opts_payload_v2.additional_properties = d
        return expression_navigate_opts_payload_v2

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
