from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_path_node_v2_type import EscalationPathNodeV2Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_path_node_if_else_v2 import EscalationPathNodeIfElseV2
    from ..models.escalation_path_node_level_v2 import EscalationPathNodeLevelV2
    from ..models.escalation_path_node_notify_channel_v2 import (
        EscalationPathNodeNotifyChannelV2,
    )
    from ..models.escalation_path_node_repeat_v2 import EscalationPathNodeRepeatV2


T = TypeVar("T", bound="EscalationPathNodeV2")


@_attrs_define
class EscalationPathNodeV2:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': {'label': 'Lawrence Jones',
            'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'round_robin_config': {'enabled':
            False, 'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'type': 'user', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}

    Attributes:
        id (str): An ID for this node, unique within the escalation path.

            This allows you to reference the node in other nodes, such as when configuring a 'repeat' node. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        type (EscalationPathNodeV2Type): The type of this node. Available types are:
            * level: A set of targets (users or schedules) that should be paged, either all at once, or with a round-robin
            configuration.
            * notify_channel: Send the escalation to a Slack channel, where it can be acked by anyone in the channel.
            * if_else: Branch the escalation based on a set of conditions.
            * repeat: Go back to a previous node and repeat the logic from there. Example: if_else.
        if_else (Union[Unset, EscalationPathNodeIfElseV2]):  Example: {'conditions': [{'operation': {'label': 'Lawrence
            Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}], 'else_path': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions':
            [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings':
            [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label':
            'Incident Severity', 'reference': 'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level':
            {'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones',
            'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency': 'high'}], 'time_to_ack_interval_condition':
            'active', 'time_to_ack_seconds': 1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'notify_channel': {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user',
            'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'then_path': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'round_robin_config': {'enabled':
            False, 'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'type': 'user', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}]}.
        level (Union[Unset, EscalationPathNodeLevelV2]):  Example: {'round_robin_config': {'enabled': False,
            'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type':
            'user', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
        notify_channel (Union[Unset, EscalationPathNodeNotifyChannelV2]):  Example: {'targets': [{'id': 'lawrencejones',
            'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency': 'high'}], 'time_to_ack_interval_condition':
            'active', 'time_to_ack_seconds': 1800, 'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
        repeat (Union[Unset, EscalationPathNodeRepeatV2]):  Example: {'repeat_times': 3, 'to_node':
            '01FCNDV6P870EA6S7TK1DSYDG0'}.
    """

    id: str
    type: EscalationPathNodeV2Type
    if_else: Union[Unset, "EscalationPathNodeIfElseV2"] = UNSET
    level: Union[Unset, "EscalationPathNodeLevelV2"] = UNSET
    notify_channel: Union[Unset, "EscalationPathNodeNotifyChannelV2"] = UNSET
    repeat: Union[Unset, "EscalationPathNodeRepeatV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        if_else: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.if_else, Unset):
            if_else = self.if_else.to_dict()

        level: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.to_dict()

        notify_channel: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notify_channel, Unset):
            notify_channel = self.notify_channel.to_dict()

        repeat: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repeat, Unset):
            repeat = self.repeat.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if if_else is not UNSET:
            field_dict["if_else"] = if_else
        if level is not UNSET:
            field_dict["level"] = level
        if notify_channel is not UNSET:
            field_dict["notify_channel"] = notify_channel
        if repeat is not UNSET:
            field_dict["repeat"] = repeat

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.escalation_path_node_if_else_v2 import EscalationPathNodeIfElseV2
        from ..models.escalation_path_node_level_v2 import EscalationPathNodeLevelV2
        from ..models.escalation_path_node_notify_channel_v2 import (
            EscalationPathNodeNotifyChannelV2,
        )
        from ..models.escalation_path_node_repeat_v2 import EscalationPathNodeRepeatV2

        d = src_dict.copy()
        id = d.pop("id")

        type = EscalationPathNodeV2Type(d.pop("type"))

        _if_else = d.pop("if_else", UNSET)
        if_else: Union[Unset, EscalationPathNodeIfElseV2]
        if isinstance(_if_else, Unset):
            if_else = UNSET
        else:
            if_else = EscalationPathNodeIfElseV2.from_dict(_if_else)

        _level = d.pop("level", UNSET)
        level: Union[Unset, EscalationPathNodeLevelV2]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = EscalationPathNodeLevelV2.from_dict(_level)

        _notify_channel = d.pop("notify_channel", UNSET)
        notify_channel: Union[Unset, EscalationPathNodeNotifyChannelV2]
        if isinstance(_notify_channel, Unset):
            notify_channel = UNSET
        else:
            notify_channel = EscalationPathNodeNotifyChannelV2.from_dict(
                _notify_channel
            )

        _repeat = d.pop("repeat", UNSET)
        repeat: Union[Unset, EscalationPathNodeRepeatV2]
        if isinstance(_repeat, Unset):
            repeat = UNSET
        else:
            repeat = EscalationPathNodeRepeatV2.from_dict(_repeat)

        escalation_path_node_v2 = cls(
            id=id,
            type=type,
            if_else=if_else,
            level=level,
            notify_channel=notify_channel,
            repeat=repeat,
        )

        escalation_path_node_v2.additional_properties = d
        return escalation_path_node_v2

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
