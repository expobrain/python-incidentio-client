from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_path_target_v2_request_body_type import (
    EscalationPathTargetV2RequestBodyType,
)
from ..models.escalation_path_target_v2_request_body_urgency import (
    EscalationPathTargetV2RequestBodyUrgency,
)

T = TypeVar("T", bound="EscalationPathTargetV2RequestBody")


@_attrs_define
class EscalationPathTargetV2RequestBody:
    """
    Example:
        {'id': 'lawrencejones', 'type': 'user', 'urgency': 'high'}

    Attributes:
        id (str): Uniquely identifies an entity of this type Example: lawrencejones.
        type (EscalationPathTargetV2RequestBodyType): Controls what type of entity this target identifies, such as
            EscalationPolicy or User Example: user.
        urgency (EscalationPathTargetV2RequestBodyUrgency): The urgency of this escalation path target Example: high.
    """

    id: str
    type: EscalationPathTargetV2RequestBodyType
    urgency: EscalationPathTargetV2RequestBodyUrgency
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        urgency = self.urgency.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "urgency": urgency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = EscalationPathTargetV2RequestBodyType(d.pop("type"))

        urgency = EscalationPathTargetV2RequestBodyUrgency(d.pop("urgency"))

        escalation_path_target_v2_request_body = cls(
            id=id,
            type=type,
            urgency=urgency,
        )

        escalation_path_target_v2_request_body.additional_properties = d
        return escalation_path_target_v2_request_body

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
