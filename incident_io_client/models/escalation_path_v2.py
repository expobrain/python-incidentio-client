from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_path_node_v2 import EscalationPathNodeV2
    from ..models.weekday_interval_config_v2 import WeekdayIntervalConfigV2


T = TypeVar("T", bound="EscalationPathV2")


@_attrs_define
class EscalationPathV2:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Urgent Support', 'path': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'if_else': {'conditions': [{'operation': {'label': 'Lawrence Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'},
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference': 'incident.severity'}}],
            'else_path': [{}], 'then_path': [{}]}, 'level': {'round_robin_config': {'enabled': False,
            'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type':
            'user', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}], 'working_hours': [{'id': 'abc123', 'name':
            'abc123', 'timezone': 'abc123', 'weekday_intervals': [{'end_time': '17:00', 'start_time': '09:00', 'weekday':
            'abc123'}]}]}

    Attributes:
        id (str): Unique identifier for this escalation path. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): The name of this escalation path, for the user's reference. Example: Urgent Support.
        path (List['EscalationPathNodeV2']): The nodes that form the levels and branches of this escalation path.
            Example: [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'if_else': {'conditions': [{'operation': {'label': 'Lawrence
            Jones', 'value': '01FCQSP07Z74QMMYPDDGQB9FTG'}, 'param_bindings': [{'array_value': [{'label': 'Lawrence Jones',
            'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal':
            'SEV123', 'reference': 'incident.severity'}}], 'subject': {'label': 'Incident Severity', 'reference':
            'incident.severity'}}], 'else_path': [{}], 'then_path': [{}]}, 'level': {'round_robin_config': {'enabled':
            False, 'rotate_after_seconds': 120}, 'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call',
            'type': 'user', 'urgency': 'high'}], 'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'notify_channel': {'targets': [{'id':
            'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'repeat': {'repeat_times': 3,
            'to_node': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'type': 'if_else'}].
        working_hours (Union[Unset, List['WeekdayIntervalConfigV2']]): The working hours for this escalation path.
            Example: [{'id': 'abc123', 'name': 'abc123', 'timezone': 'abc123', 'weekday_intervals': [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'abc123'}]}].
    """

    id: str
    name: str
    path: List["EscalationPathNodeV2"]
    working_hours: Union[Unset, List["WeekdayIntervalConfigV2"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        path = []
        for path_item_data in self.path:
            path_item = path_item_data.to_dict()
            path.append(path_item)

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
                "id": id,
                "name": name,
                "path": path,
            }
        )
        if working_hours is not UNSET:
            field_dict["working_hours"] = working_hours

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.escalation_path_node_v2 import EscalationPathNodeV2
        from ..models.weekday_interval_config_v2 import WeekdayIntervalConfigV2

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        path = []
        _path = d.pop("path")
        for path_item_data in _path:
            path_item = EscalationPathNodeV2.from_dict(path_item_data)

            path.append(path_item)

        working_hours = []
        _working_hours = d.pop("working_hours", UNSET)
        for working_hours_item_data in _working_hours or []:
            working_hours_item = WeekdayIntervalConfigV2.from_dict(working_hours_item_data)

            working_hours.append(working_hours_item)

        escalation_path_v2 = cls(
            id=id,
            name=name,
            path=path,
            working_hours=working_hours,
        )

        escalation_path_v2.additional_properties = d
        return escalation_path_v2

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
