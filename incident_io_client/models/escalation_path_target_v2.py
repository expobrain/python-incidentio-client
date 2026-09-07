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
        {'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'type': 'schedule', 'urgency': 'high'}

    Attributes:
        id (str): Uniquely identifies an entity of this type Example: lawrencejones.
        type (EscalationPathTargetV2Type): Controls what type of entity this target identifies, such as EscalationPolicy
            or User Example: schedule.
        urgency (EscalationPathTargetV2Urgency): The urgency of this escalation path target Example: high.
        schedule_mode (Union[Unset, EscalationPathTargetV2ScheduleMode]): Only set for schedule targets, this specifies
            which users to fetch from the schedule. Use currently_on_call to notify whoever is on call right now across the
            schedule, all_users to notify every user attached to the schedule, or all_users_for_rota /
            currently_on_call_for_rota / next_on_call_for_rota to scope to a specific rota (in which case selected_rota_id
            is required). next_on_call notifies whoever is next on call across the schedule. Example: currently_on_call.
        selected_rota_id (Union[Unset, str]): For schedule targets, identifies which rota on the schedule the
            schedule_mode applies to. Required when schedule_mode is all_users_for_rota, currently_on_call_for_rota, or
            next_on_call_for_rota; must be omitted for other schedule_mode values. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    id: str
    type: EscalationPathTargetV2Type
    urgency: EscalationPathTargetV2Urgency
    schedule_mode: Union[Unset, EscalationPathTargetV2ScheduleMode] = UNSET
    selected_rota_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        urgency = self.urgency.value

        schedule_mode: Union[Unset, str] = UNSET
        if not isinstance(self.schedule_mode, Unset):
            schedule_mode = self.schedule_mode.value

        selected_rota_id = self.selected_rota_id

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
        if selected_rota_id is not UNSET:
            field_dict["selected_rota_id"] = selected_rota_id

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

        selected_rota_id = d.pop("selected_rota_id", UNSET)

        escalation_path_target_v2 = cls(
            id=id,
            type=type,
            urgency=urgency,
            schedule_mode=schedule_mode,
            selected_rota_id=selected_rota_id,
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
