from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_path_node_v2_response_body_type import (
    EscalationPathNodeV2ResponseBodyType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_path_node_if_else_v2_response_body import (
        EscalationPathNodeIfElseV2ResponseBody,
    )
    from ..models.escalation_path_node_level_v2_response_body import (
        EscalationPathNodeLevelV2ResponseBody,
    )
    from ..models.escalation_path_node_repeat_v2_response_body import (
        EscalationPathNodeRepeatV2ResponseBody,
    )


T = TypeVar("T", bound="EscalationPathNodeV2ResponseBody")


@_attrs_define
class EscalationPathNodeV2ResponseBody:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': {'label': 'Lawrence Jones',
            'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'round_robin_config': {'enabled':
            False, 'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'type': 'user', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}

    Attributes:
        id (str): Unique internal ID of the escalation path node Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        type (EscalationPathNodeV2ResponseBodyType): The type of this node: level or branch Example: if_else.
        if_else (Union[Unset, EscalationPathNodeIfElseV2ResponseBody]):  Example: {'conditions': [{'operation':
            {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value':
            [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident
            Severity', 'reference': 'incident.severity'}}], 'else_path': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else':
            {'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}],
            'else_path': [{}], 'then_path': [{}]}, 'level': {'round_robin_config': {'enabled': False,
            'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type':
            'user', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'then_path': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': {'label': 'Lawrence Jones', 'value':
            '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'round_robin_config': {'enabled':
            False, 'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'type': 'user', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}]}.
        level (Union[Unset, EscalationPathNodeLevelV2ResponseBody]):  Example: {'round_robin_config': {'enabled': False,
            'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type':
            'user', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
        repeat (Union[Unset, EscalationPathNodeRepeatV2ResponseBody]):  Example: {'repeat_times': 3, 'to_node':
            '01FCNDV6P870EA6S7TK1DSYDG0'}.
    """

    id: str
    type: EscalationPathNodeV2ResponseBodyType
    if_else: Union[Unset, "EscalationPathNodeIfElseV2ResponseBody"] = UNSET
    level: Union[Unset, "EscalationPathNodeLevelV2ResponseBody"] = UNSET
    repeat: Union[Unset, "EscalationPathNodeRepeatV2ResponseBody"] = UNSET
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
        if repeat is not UNSET:
            field_dict["repeat"] = repeat

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.escalation_path_node_if_else_v2_response_body import (
            EscalationPathNodeIfElseV2ResponseBody,
        )
        from ..models.escalation_path_node_level_v2_response_body import (
            EscalationPathNodeLevelV2ResponseBody,
        )
        from ..models.escalation_path_node_repeat_v2_response_body import (
            EscalationPathNodeRepeatV2ResponseBody,
        )

        d = src_dict.copy()
        id = d.pop("id")

        type = EscalationPathNodeV2ResponseBodyType(d.pop("type"))

        _if_else = d.pop("if_else", UNSET)
        if_else: Union[Unset, EscalationPathNodeIfElseV2ResponseBody]
        if isinstance(_if_else, Unset):
            if_else = UNSET
        else:
            if_else = EscalationPathNodeIfElseV2ResponseBody.from_dict(_if_else)

        _level = d.pop("level", UNSET)
        level: Union[Unset, EscalationPathNodeLevelV2ResponseBody]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = EscalationPathNodeLevelV2ResponseBody.from_dict(_level)

        _repeat = d.pop("repeat", UNSET)
        repeat: Union[Unset, EscalationPathNodeRepeatV2ResponseBody]
        if isinstance(_repeat, Unset):
            repeat = UNSET
        else:
            repeat = EscalationPathNodeRepeatV2ResponseBody.from_dict(_repeat)

        escalation_path_node_v2_response_body = cls(
            id=id,
            type=type,
            if_else=if_else,
            level=level,
            repeat=repeat,
        )

        escalation_path_node_v2_response_body.additional_properties = d
        return escalation_path_node_v2_response_body

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
