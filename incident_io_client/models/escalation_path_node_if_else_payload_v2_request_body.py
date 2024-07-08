from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_payload_v2_request_body import ConditionPayloadV2RequestBody
    from ..models.escalation_path_node_payload_v2_request_body import (
        EscalationPathNodePayloadV2RequestBody,
    )


T = TypeVar("T", bound="EscalationPathNodeIfElsePayloadV2RequestBody")


@_attrs_define
class EscalationPathNodeIfElsePayloadV2RequestBody:
    """
    Example:
        {'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}], 'else_path': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions':
            [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'round_robin_config': {'enabled': False,
            'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type':
            'user', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'then_path': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': 'one_of', 'param_bindings':
            [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123',
            'reference': 'incident.severity'}}], 'subject': 'incident.severity'}], 'else_path': [{}], 'then_path': [{}]},
            'level': {'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}]}

    Attributes:
        else_path (List['EscalationPathNodePayloadV2RequestBody']): The nodes that form the levels if our condition is
            not met Example: [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}], 'else_path': [{}],
            'then_path': [{}]}, 'level': {'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets':
            [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}].
        then_path (List['EscalationPathNodePayloadV2RequestBody']): The nodes that form the levels if our condition is
            met Example: [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': 'one_of',
            'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject': 'incident.severity'}], 'else_path': [{}],
            'then_path': [{}]}, 'level': {'round_robin_config': {'enabled': False, 'rotate_after_seconds': 120}, 'targets':
            [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}].
        conditions (Union[Unset, List['ConditionPayloadV2RequestBody']]): The condition that defines which branch to
            take Example: [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}].
    """

    else_path: List["EscalationPathNodePayloadV2RequestBody"]
    then_path: List["EscalationPathNodePayloadV2RequestBody"]
    conditions: Union[Unset, List["ConditionPayloadV2RequestBody"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        else_path = []
        for else_path_item_data in self.else_path:
            else_path_item = else_path_item_data.to_dict()
            else_path.append(else_path_item)

        then_path = []
        for then_path_item_data in self.then_path:
            then_path_item = then_path_item_data.to_dict()
            then_path.append(then_path_item)

        conditions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "else_path": else_path,
                "then_path": then_path,
            }
        )
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.condition_payload_v2_request_body import (
            ConditionPayloadV2RequestBody,
        )
        from ..models.escalation_path_node_payload_v2_request_body import (
            EscalationPathNodePayloadV2RequestBody,
        )

        d = src_dict.copy()
        else_path = []
        _else_path = d.pop("else_path")
        for else_path_item_data in _else_path:
            else_path_item = EscalationPathNodePayloadV2RequestBody.from_dict(else_path_item_data)

            else_path.append(else_path_item)

        then_path = []
        _then_path = d.pop("then_path")
        for then_path_item_data in _then_path:
            then_path_item = EscalationPathNodePayloadV2RequestBody.from_dict(then_path_item_data)

            then_path.append(then_path_item)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = ConditionPayloadV2RequestBody.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        escalation_path_node_if_else_payload_v2_request_body = cls(
            else_path=else_path,
            then_path=then_path,
            conditions=conditions,
        )

        escalation_path_node_if_else_payload_v2_request_body.additional_properties = d
        return escalation_path_node_if_else_payload_v2_request_body

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
