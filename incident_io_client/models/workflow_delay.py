from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowDelay")


@_attrs_define
class WorkflowDelay:
    """
    Example:
        {'conditions_apply_over_delay': False, 'for_seconds': 60}

    Attributes:
        conditions_apply_over_delay (bool): If this workflow is delayed, whether the conditions should be rechecked
            between trigger firing and execution
        for_seconds (int): Delay in seconds between trigger firing and running the workflow Example: 60.
    """

    conditions_apply_over_delay: bool
    for_seconds: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conditions_apply_over_delay = self.conditions_apply_over_delay

        for_seconds = self.for_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditions_apply_over_delay": conditions_apply_over_delay,
                "for_seconds": for_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        conditions_apply_over_delay = d.pop("conditions_apply_over_delay")

        for_seconds = d.pop("for_seconds")

        workflow_delay = cls(
            conditions_apply_over_delay=conditions_apply_over_delay,
            for_seconds=for_seconds,
        )

        workflow_delay.additional_properties = d
        return workflow_delay

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
