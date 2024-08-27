from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.condition_subject_color import ConditionSubjectColor
from ..models.condition_subject_icon import ConditionSubjectIcon
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConditionSubject")


@_attrs_define
class ConditionSubject:
    """
    Example:
        {'color': 'yellow', 'icon': 'action', 'label': 'Incident Severity', 'reference': 'incident.severity'}

    Attributes:
        icon (ConditionSubjectIcon): String telling the UI what icon to use for this field Example: action.
        label (str): Human readable identifier for the subject Example: Incident Severity.
        reference (str): Reference into the scope for the value of the subject Example: incident.severity.
        color (Union[Unset, ConditionSubjectColor]): String telling the UI what color to use for this field, if
            applicable Example: yellow.
    """

    icon: ConditionSubjectIcon
    label: str
    reference: str
    color: Union[Unset, ConditionSubjectColor] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        icon = self.icon.value

        label = self.label

        reference = self.reference

        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "icon": icon,
                "label": label,
                "reference": reference,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        icon = ConditionSubjectIcon(d.pop("icon"))

        label = d.pop("label")

        reference = d.pop("reference")

        _color = d.pop("color", UNSET)
        color: Union[Unset, ConditionSubjectColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = ConditionSubjectColor(_color)

        condition_subject = cls(
            icon=icon,
            label=label,
            reference=reference,
            color=color,
        )

        condition_subject.additional_properties = d
        return condition_subject

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
