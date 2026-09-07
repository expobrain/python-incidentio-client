from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_sync_rule_create_payload_v2_sync_type import (
    ScheduleSyncRuleCreatePayloadV2SyncType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_sync_rule_create_payload_v2_annotations import (
        ScheduleSyncRuleCreatePayloadV2Annotations,
    )


T = TypeVar("T", bound="ScheduleSyncRuleCreatePayloadV2")


@_attrs_define
class ScheduleSyncRuleCreatePayloadV2:
    """
    Example:
        {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'permanent_member_user_ids':
            ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'rotation_id': '01JXYZ000000000000000000RT', 'schedule_sync_target_id':
            '01JXYZ000000000000000000AB', 'sync_type': 'on_call'}

    Attributes:
        schedule_sync_target_id (str): The sync target to link to Example: 01JXYZ000000000000000000AB.
        sync_type (ScheduleSyncRuleCreatePayloadV2SyncType): Which schedule members sync to the user group Example:
            on_call.
        annotations (Union[Unset, ScheduleSyncRuleCreatePayloadV2Annotations]): Annotations that track metadata about
            this resource Example: {'incident.io/terraform/version': '3.0.0'}.
        permanent_member_user_ids (Union[Unset, List[str]]): IDs of users to always keep in the Slack user group,
            regardless of who is on call. Each must be an active user in your organisation. Defaults to none. Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
        rotation_id (Union[Unset, str]): If set, scopes the rule to a single rotation on the schedule. When unset, all
            rotations are synced. Example: 01JXYZ000000000000000000RT.
    """

    schedule_sync_target_id: str
    sync_type: ScheduleSyncRuleCreatePayloadV2SyncType
    annotations: Union[Unset, "ScheduleSyncRuleCreatePayloadV2Annotations"] = UNSET
    permanent_member_user_ids: Union[Unset, List[str]] = UNSET
    rotation_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schedule_sync_target_id = self.schedule_sync_target_id

        sync_type = self.sync_type.value

        annotations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        permanent_member_user_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permanent_member_user_ids, Unset):
            permanent_member_user_ids = self.permanent_member_user_ids

        rotation_id = self.rotation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_sync_target_id": schedule_sync_target_id,
                "sync_type": sync_type,
            }
        )
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if permanent_member_user_ids is not UNSET:
            field_dict["permanent_member_user_ids"] = permanent_member_user_ids
        if rotation_id is not UNSET:
            field_dict["rotation_id"] = rotation_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schedule_sync_rule_create_payload_v2_annotations import (
            ScheduleSyncRuleCreatePayloadV2Annotations,
        )

        d = src_dict.copy()
        schedule_sync_target_id = d.pop("schedule_sync_target_id")

        sync_type = ScheduleSyncRuleCreatePayloadV2SyncType(d.pop("sync_type"))

        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, ScheduleSyncRuleCreatePayloadV2Annotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = ScheduleSyncRuleCreatePayloadV2Annotations.from_dict(
                _annotations
            )

        permanent_member_user_ids = cast(
            List[str], d.pop("permanent_member_user_ids", UNSET)
        )

        rotation_id = d.pop("rotation_id", UNSET)

        schedule_sync_rule_create_payload_v2 = cls(
            schedule_sync_target_id=schedule_sync_target_id,
            sync_type=sync_type,
            annotations=annotations,
            permanent_member_user_ids=permanent_member_user_ids,
            rotation_id=rotation_id,
        )

        schedule_sync_rule_create_payload_v2.additional_properties = d
        return schedule_sync_rule_create_payload_v2

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
