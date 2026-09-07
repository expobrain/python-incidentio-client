from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_slack_user_group_payload_v2 import NewSlackUserGroupPayloadV2
    from ..models.schedule_sync_target_create_payload_v2_annotations import (
        ScheduleSyncTargetCreatePayloadV2Annotations,
    )


T = TypeVar("T", bound="ScheduleSyncTargetCreatePayloadV2")


@_attrs_define
class ScheduleSyncTargetCreatePayloadV2:
    """
    Example:
        {'add_bot_to_group': True, 'annotations': {'incident.io/terraform/version': '3.0.0'}, 'new_slack_user_group':
            {'description': 'The team responsible for Project A', 'handle': 'project-team-a', 'name': 'Project Team A',
            'slack_team_id': 'T01234567'}, 'slack_user_group_id': 'S06MNNU5BMK'}

    Attributes:
        add_bot_to_group (bool): Whether the incident.io bot should be added to the group Example: True.
        annotations (Union[Unset, ScheduleSyncTargetCreatePayloadV2Annotations]): Annotations that track metadata about
            this resource Example: {'incident.io/terraform/version': '3.0.0'}.
        new_slack_user_group (Union[Unset, NewSlackUserGroupPayloadV2]):  Example: {'description': 'The team responsible
            for Project A', 'handle': 'project-team-a', 'name': 'Project Team A', 'slack_team_id': 'T01234567'}.
        slack_user_group_id (Union[Unset, str]): Slack ID of an existing user group to sync to. Mutually exclusive with
            new_slack_user_group; exactly one must be set. Example: S06MNNU5BMK.
    """

    add_bot_to_group: bool
    annotations: Union[Unset, "ScheduleSyncTargetCreatePayloadV2Annotations"] = UNSET
    new_slack_user_group: Union[Unset, "NewSlackUserGroupPayloadV2"] = UNSET
    slack_user_group_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        add_bot_to_group = self.add_bot_to_group

        annotations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        new_slack_user_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_slack_user_group, Unset):
            new_slack_user_group = self.new_slack_user_group.to_dict()

        slack_user_group_id = self.slack_user_group_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "add_bot_to_group": add_bot_to_group,
            }
        )
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if new_slack_user_group is not UNSET:
            field_dict["new_slack_user_group"] = new_slack_user_group
        if slack_user_group_id is not UNSET:
            field_dict["slack_user_group_id"] = slack_user_group_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.new_slack_user_group_payload_v2 import NewSlackUserGroupPayloadV2
        from ..models.schedule_sync_target_create_payload_v2_annotations import (
            ScheduleSyncTargetCreatePayloadV2Annotations,
        )

        d = src_dict.copy()
        add_bot_to_group = d.pop("add_bot_to_group")

        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, ScheduleSyncTargetCreatePayloadV2Annotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = ScheduleSyncTargetCreatePayloadV2Annotations.from_dict(
                _annotations
            )

        _new_slack_user_group = d.pop("new_slack_user_group", UNSET)
        new_slack_user_group: Union[Unset, NewSlackUserGroupPayloadV2]
        if isinstance(_new_slack_user_group, Unset):
            new_slack_user_group = UNSET
        else:
            new_slack_user_group = NewSlackUserGroupPayloadV2.from_dict(
                _new_slack_user_group
            )

        slack_user_group_id = d.pop("slack_user_group_id", UNSET)

        schedule_sync_target_create_payload_v2 = cls(
            add_bot_to_group=add_bot_to_group,
            annotations=annotations,
            new_slack_user_group=new_slack_user_group,
            slack_user_group_id=slack_user_group_id,
        )

        schedule_sync_target_create_payload_v2.additional_properties = d
        return schedule_sync_target_create_payload_v2

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
