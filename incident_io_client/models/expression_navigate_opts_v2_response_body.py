from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExpressionNavigateOptsV2ResponseBody")


@_attrs_define
class ExpressionNavigateOptsV2ResponseBody:
    """
    Example:
        {'reference': '1235', 'reference_label': 'Teams'}

    Attributes:
        reference (str): The reference within the scope to navigate to Example: 1235.
        reference_label (str): The name of the reference to navigate to Example: Teams.
    """

    reference: str
    reference_label: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference = self.reference

        reference_label = self.reference_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reference": reference,
                "reference_label": reference_label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reference = d.pop("reference")

        reference_label = d.pop("reference_label")

        expression_navigate_opts_v2_response_body = cls(
            reference=reference,
            reference_label=reference_label,
        )

        expression_navigate_opts_v2_response_body.additional_properties = d
        return expression_navigate_opts_v2_response_body

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
