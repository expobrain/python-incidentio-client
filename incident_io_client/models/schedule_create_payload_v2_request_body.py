from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_config_create_payload_v2_request_body import (
        ScheduleConfigCreatePayloadV2RequestBody,
    )
    from ..models.schedule_create_payload_v2_request_body_annotations import (
        ScheduleCreatePayloadV2RequestBodyAnnotations,
    )


T = TypeVar("T", bound="ScheduleCreatePayloadV2RequestBody")


@_attrs_define
class ScheduleCreatePayloadV2RequestBody:
    """
    Example:
        {'annotations': {'incident.io/terraform/version': 'version-of-terraform'}, 'config': {'rotations':
            [{'effective_from': '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z',
            'handovers': [{'interval': 1, 'interval_type': 'daily'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}], 'name': 'My Rotation', 'users': [{'email': 'bob@example.com',
            'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}], 'working_interval': [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'tuesday'}]}]}, 'name': 'My Schedule', 'timezone': 'America/Los_Angeles'}

    Attributes:
        annotations (Union[Unset, ScheduleCreatePayloadV2RequestBodyAnnotations]): Annotations that can track metadata
            about the schedule Example: {'incident.io/terraform/version': 'version-of-terraform'}.
        config (Union[Unset, ScheduleConfigCreatePayloadV2RequestBody]):  Example: {'rotations': [{'effective_from':
            '2021-08-17T13:28:57.801578Z', 'handover_start_at': '2021-08-17T13:28:57.801578Z', 'handovers': [{'interval': 1,
            'interval_type': 'daily'}], 'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'layers': [{'id': '01G0J1EXE7AXZ2C93K61WBPYEH',
            'name': 'Layer 1'}], 'name': 'My Rotation', 'users': [{'email': 'bob@example.com', 'id':
            '01G0J1EXE7AXZ2C93K61WBPYEH', 'slack_user_id': 'USER123'}], 'working_interval': [{'end_time': '17:00',
            'start_time': '09:00', 'weekday': 'tuesday'}]}]}.
        name (Union[Unset, str]): Name of the schedule Example: My Schedule.
        timezone (Union[Unset, str]): Timezone of the schedule Example: America/Los_Angeles.
    """

    annotations: Union[Unset, "ScheduleCreatePayloadV2RequestBodyAnnotations"] = UNSET
    config: Union[Unset, "ScheduleConfigCreatePayloadV2RequestBody"] = UNSET
    name: Union[Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        annotations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        name = self.name

        timezone = self.timezone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if config is not UNSET:
            field_dict["config"] = config
        if name is not UNSET:
            field_dict["name"] = name
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schedule_config_create_payload_v2_request_body import (
            ScheduleConfigCreatePayloadV2RequestBody,
        )
        from ..models.schedule_create_payload_v2_request_body_annotations import (
            ScheduleCreatePayloadV2RequestBodyAnnotations,
        )

        d = src_dict.copy()
        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, ScheduleCreatePayloadV2RequestBodyAnnotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = ScheduleCreatePayloadV2RequestBodyAnnotations.from_dict(_annotations)

        _config = d.pop("config", UNSET)
        config: Union[Unset, ScheduleConfigCreatePayloadV2RequestBody]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ScheduleConfigCreatePayloadV2RequestBody.from_dict(_config)

        name = d.pop("name", UNSET)

        timezone = d.pop("timezone", UNSET)

        schedule_create_payload_v2_request_body = cls(
            annotations=annotations,
            config=config,
            name=name,
            timezone=timezone,
        )

        schedule_create_payload_v2_request_body.additional_properties = d
        return schedule_create_payload_v2_request_body

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
