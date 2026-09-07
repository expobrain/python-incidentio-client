from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_template_attribute_binding_v2 import (
        AlertTemplateAttributeBindingV2,
    )


T = TypeVar("T", bound="AlertTemplateAttributeV2")


@_attrs_define
class AlertTemplateAttributeV2:
    """
    Example:
        {'alert_attribute_id': 'abc123', 'binding': {'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}], 'merge_strategy': 'first_wins', 'value': {'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}}}

    Attributes:
        alert_attribute_id (str): ID of the alert attribute to set with this binding Example: abc123.
        binding (AlertTemplateAttributeBindingV2):  Example: {'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'merge_strategy': 'first_wins', 'value': {'label': 'Lawrence
            Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}.
    """

    alert_attribute_id: str
    binding: "AlertTemplateAttributeBindingV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_attribute_id = self.alert_attribute_id

        binding = self.binding.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_attribute_id": alert_attribute_id,
                "binding": binding,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_template_attribute_binding_v2 import (
            AlertTemplateAttributeBindingV2,
        )

        d = src_dict.copy()
        alert_attribute_id = d.pop("alert_attribute_id")

        binding = AlertTemplateAttributeBindingV2.from_dict(d.pop("binding"))

        alert_template_attribute_v2 = cls(
            alert_attribute_id=alert_attribute_id,
            binding=binding,
        )

        alert_template_attribute_v2.additional_properties = d
        return alert_template_attribute_v2

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
