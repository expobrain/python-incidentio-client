from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_path_target_v2_schedule_mode import (
    EscalationPathTargetV2ScheduleMode,
)
from ..models.escalation_path_target_v2_type import EscalationPathTargetV2Type
from ..models.escalation_path_target_v2_urgency import EscalationPathTargetV2Urgency
from ..types import UNSET, Unset

T = TypeVar("T", bound="EscalationPathTargetV2")


@_attrs_define
class EscalationPathTargetV2:
    """
    Example:
        {'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency': 'high'}

    Attributes:
        id (str): Uniquely identifies an entity of this type Example: lawrencejones.
        type (EscalationPathTargetV2Type): Controls what type of entity this target identifies, such as EscalationPolicy
            or User Example: user.
        urgency (EscalationPathTargetV2Urgency): The urgency of this escalation path target Example: high.
        schedule_mode (Union[Unset, EscalationPathTargetV2ScheduleMode]): Only set for schedule targets, and either
            currently_on_call, all_users or all_users_for_rota and specifies which users to fetch from the schedule Example:
            currently_on_call.
    """

    id: str
    type: EscalationPathTargetV2Type
    urgency: EscalationPathTargetV2Urgency
    schedule_mode: Union[Unset, EscalationPathTargetV2ScheduleMode] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        urgency = self.urgency.value

        schedule_mode: Union[Unset, str] = UNSET
        if not isinstance(self.schedule_mode, Unset):
            schedule_mode = self.schedule_mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "urgency": urgency,
            }
        )
        if schedule_mode is not UNSET:
            field_dict["schedule_mode"] = schedule_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = EscalationPathTargetV2Type(d.pop("type"))

        urgency = EscalationPathTargetV2Urgency(d.pop("urgency"))

        _schedule_mode = d.pop("schedule_mode", UNSET)
        schedule_mode: Union[Unset, EscalationPathTargetV2ScheduleMode]
        if isinstance(_schedule_mode, Unset):
            schedule_mode = UNSET
        else:
            schedule_mode = EscalationPathTargetV2ScheduleMode(_schedule_mode)

        escalation_path_target_v2 = cls(
            id=id,
            type=type,
            urgency=urgency,
            schedule_mode=schedule_mode,
        )

        escalation_path_target_v2.additional_properties = d
        return escalation_path_target_v2

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
