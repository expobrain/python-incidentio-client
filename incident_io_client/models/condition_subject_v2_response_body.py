from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConditionSubjectV2ResponseBody")


@_attrs_define
class ConditionSubjectV2ResponseBody:
    """
    Example:
        {'label': 'Incident Severity', 'reference': 'incident.severity'}

    Attributes:
        label (str): Human readable identifier for the subject Example: Incident Severity.
        reference (str): Reference into the scope for the value of the subject Example: incident.severity.
    """

    label: str
    reference: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        reference = self.reference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "reference": reference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        reference = d.pop("reference")

        condition_subject_v2_response_body = cls(
            label=label,
            reference=reference,
        )

        condition_subject_v2_response_body.additional_properties = d
        return condition_subject_v2_response_body

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
