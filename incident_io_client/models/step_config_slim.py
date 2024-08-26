from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StepConfigSlim")


@_attrs_define
class StepConfigSlim:
    """
    Example:
        {'label': 'PagerDuty Escalate', 'name': 'pagerduty.escalate'}

    Attributes:
        label (str): Human readable identifier for this step Example: PagerDuty Escalate.
        name (str): Unique name of the step in the engine Example: pagerduty.escalate.
    """

    label: str
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        name = d.pop("name")

        step_config_slim = cls(
            label=label,
            name=name,
        )

        step_config_slim.additional_properties = d
        return step_config_slim

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
