from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.condition_payload_v2_request_body import ConditionPayloadV2RequestBody


T = TypeVar("T", bound="ConditionGroupPayloadV2RequestBody")


@_attrs_define
class ConditionGroupPayloadV2RequestBody:
    """
    Example:
        {'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}

    Attributes:
        conditions (List['ConditionPayloadV2RequestBody']): All conditions in this list must be satisfied for the group
            to be satisfied Example: [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123',
            'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}],
            'subject': 'incident.severity'}].
    """

    conditions: List["ConditionPayloadV2RequestBody"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item = conditions_item_data.to_dict()
            conditions.append(conditions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditions": conditions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.condition_payload_v2_request_body import (
            ConditionPayloadV2RequestBody,
        )

        d = src_dict.copy()
        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in _conditions:
            conditions_item = ConditionPayloadV2RequestBody.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        condition_group_payload_v2_request_body = cls(
            conditions=conditions,
        )

        condition_group_payload_v2_request_body.additional_properties = d
        return condition_group_payload_v2_request_body

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
