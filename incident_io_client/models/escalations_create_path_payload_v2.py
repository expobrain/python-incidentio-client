from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_path_node_payload_v2 import EscalationPathNodePayloadV2
    from ..models.escalation_path_repeat_config_v2 import EscalationPathRepeatConfigV2
    from ..models.weekday_interval_config_v2 import WeekdayIntervalConfigV2


T = TypeVar("T", bound="EscalationsCreatePathPayloadV2")


@_attrs_define
class EscalationsCreatePathPayloadV2:
    """
    Example:
        {'name': 'Urgent Support', 'path': [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300,
            'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}], 'else_path': [{}],
            'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config': {'attempts': 3, 'interval_seconds': 300},
            'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones',
            'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule',
            'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type':
            'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'repeat_config': {'delay_repeat_on_activity':
            False, 'repeat_after_seconds': 1800}, 'team_ids': ['01JPQA75EPNEES4479P16P4XAB'], 'working_hours': [{'id':
            'abc123', 'name': 'abc123', 'timezone': 'abc123', 'weekday_intervals': [{'end_time': '17:00', 'start_time':
            '09:00', 'weekday': 'monday'}]}]}

    Attributes:
        name (str): The name of this escalation path, for the user's reference. Example: Urgent Support.
        path (List['EscalationPathNodePayloadV2']): The nodes that form the levels and branches of this escalation path.
            Example: [{'delay': {'delay_interval_condition': 'active', 'delay_seconds': 300,
            'delay_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'escalation_path': {'escalation_path_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation':
            'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}], 'else_path': [{}],
            'then_path': [{}]}, 'level': {'ack_mode': 'all', 'retry_config': {'attempts': 3, 'interval_seconds': 300},
            'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones',
            'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type': 'schedule',
            'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'selected_rota_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'type':
            'schedule', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}].
        repeat_config (Union[Unset, EscalationPathRepeatConfigV2]):  Example: {'delay_repeat_on_activity': False,
            'repeat_after_seconds': 1800}.
        team_ids (Union[Unset, List[str]]): IDs of the teams that own this escalation path. This will automatically sync
            escalation paths with the right teams in Catalog. If you have an escalation paths attribute on your Teams, this
            attribute is required. Example: ['01JPQA75EPNEES4479P16P4XAB'].
        working_hours (Union[Unset, List['WeekdayIntervalConfigV2']]): The working hours for this escalation path.
            Example: [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123', 'weekday_intervals': [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'monday'}]}].
    """

    name: str
    path: List["EscalationPathNodePayloadV2"]
    repeat_config: Union[Unset, "EscalationPathRepeatConfigV2"] = UNSET
    team_ids: Union[Unset, List[str]] = UNSET
    working_hours: Union[Unset, List["WeekdayIntervalConfigV2"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        path = []
        for path_item_data in self.path:
            path_item = path_item_data.to_dict()
            path.append(path_item)

        repeat_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repeat_config, Unset):
            repeat_config = self.repeat_config.to_dict()

        team_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.team_ids, Unset):
            team_ids = self.team_ids

        working_hours: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.working_hours, Unset):
            working_hours = []
            for working_hours_item_data in self.working_hours:
                working_hours_item = working_hours_item_data.to_dict()
                working_hours.append(working_hours_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "path": path,
            }
        )
        if repeat_config is not UNSET:
            field_dict["repeat_config"] = repeat_config
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids
        if working_hours is not UNSET:
            field_dict["working_hours"] = working_hours

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.escalation_path_node_payload_v2 import EscalationPathNodePayloadV2
        from ..models.escalation_path_repeat_config_v2 import (
            EscalationPathRepeatConfigV2,
        )
        from ..models.weekday_interval_config_v2 import WeekdayIntervalConfigV2

        d = src_dict.copy()
        name = d.pop("name")

        path = []
        _path = d.pop("path")
        for path_item_data in _path:
            path_item = EscalationPathNodePayloadV2.from_dict(path_item_data)

            path.append(path_item)

        _repeat_config = d.pop("repeat_config", UNSET)
        repeat_config: Union[Unset, EscalationPathRepeatConfigV2]
        if isinstance(_repeat_config, Unset):
            repeat_config = UNSET
        else:
            repeat_config = EscalationPathRepeatConfigV2.from_dict(_repeat_config)

        team_ids = cast(List[str], d.pop("team_ids", UNSET))

        working_hours = []
        _working_hours = d.pop("working_hours", UNSET)
        for working_hours_item_data in _working_hours or []:
            working_hours_item = WeekdayIntervalConfigV2.from_dict(
                working_hours_item_data
            )

            working_hours.append(working_hours_item)

        escalations_create_path_payload_v2 = cls(
            name=name,
            path=path,
            repeat_config=repeat_config,
            team_ids=team_ids,
            working_hours=working_hours,
        )

        escalations_create_path_payload_v2.additional_properties = d
        return escalations_create_path_payload_v2

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
