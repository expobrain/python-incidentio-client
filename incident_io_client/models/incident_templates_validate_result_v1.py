from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_template_validate_warning_v1 import (
        IncidentTemplateValidateWarningV1,
    )


T = TypeVar("T", bound="IncidentTemplatesValidateResultV1")


@_attrs_define
class IncidentTemplatesValidateResultV1:
    """
    Example:
        {'warnings': [{'detail': 'Creating a new template with this name will fail. Updating the template that already
            has it keeps working.', 'summary': 'An incident template with this name already exists'}]}

    Attributes:
        warnings (List['IncidentTemplateValidateWarningV1']): Anything suspect about this config that isn't severe
            enough to reject it. Empty when there's nothing to say. Example: [{'detail': 'Creating a new template with this
            name will fail. Updating the template that already has it keeps working.', 'summary': 'An incident template with
            this name already exists'}].
    """

    warnings: List["IncidentTemplateValidateWarningV1"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        warnings = []
        for warnings_item_data in self.warnings:
            warnings_item = warnings_item_data.to_dict()
            warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warnings": warnings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.incident_template_validate_warning_v1 import (
            IncidentTemplateValidateWarningV1,
        )

        d = src_dict.copy()
        warnings = []
        _warnings = d.pop("warnings")
        for warnings_item_data in _warnings:
            warnings_item = IncidentTemplateValidateWarningV1.from_dict(
                warnings_item_data
            )

            warnings.append(warnings_item)

        incident_templates_validate_result_v1 = cls(
            warnings=warnings,
        )

        incident_templates_validate_result_v1.additional_properties = d
        return incident_templates_validate_result_v1

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
