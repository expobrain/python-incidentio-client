from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_follow_up_updated_v2_new_status import (
    ActivityFollowUpUpdatedV2NewStatus,
)
from ..models.activity_follow_up_updated_v2_previous_status import (
    ActivityFollowUpUpdatedV2PreviousStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ActivityFollowUpUpdatedV2")


@_attrs_define
class ActivityFollowUpUpdatedV2:
    """
    Example:
        {'follow_up_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'new_assignee': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'},
            'new_status': 'completed', 'new_title': 'Add a payments-api rollback runbook', 'previous_assignee': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'previous_status': 'outstanding', 'previous_title': 'Add a runbook', 'updater':
            {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
            'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}}}

    Attributes:
        follow_up_id (str): The follow-up that changed. Fetch it from GET /v2/follow_ups/{id}. Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        new_assignee (Union[Unset, UserV2]):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
        new_status (Union[Unset, ActivityFollowUpUpdatedV2NewStatus]): Status after, when the status changed Example:
            completed.
        new_title (Union[Unset, str]): Title after, when the title changed Example: Add a payments-api rollback runbook.
        previous_assignee (Union[Unset, UserV2]):  Example: {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
        previous_status (Union[Unset, ActivityFollowUpUpdatedV2PreviousStatus]): Status before, when the status changed
            Example: outstanding.
        previous_title (Union[Unset, str]): Title before, when the title changed Example: Add a runbook.
        updater (Union[Unset, ActorV2]):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}.
    """

    follow_up_id: str
    new_assignee: Union[Unset, "UserV2"] = UNSET
    new_status: Union[Unset, ActivityFollowUpUpdatedV2NewStatus] = UNSET
    new_title: Union[Unset, str] = UNSET
    previous_assignee: Union[Unset, "UserV2"] = UNSET
    previous_status: Union[Unset, ActivityFollowUpUpdatedV2PreviousStatus] = UNSET
    previous_title: Union[Unset, str] = UNSET
    updater: Union[Unset, "ActorV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        follow_up_id = self.follow_up_id

        new_assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_assignee, Unset):
            new_assignee = self.new_assignee.to_dict()

        new_status: Union[Unset, str] = UNSET
        if not isinstance(self.new_status, Unset):
            new_status = self.new_status.value

        new_title = self.new_title

        previous_assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.previous_assignee, Unset):
            previous_assignee = self.previous_assignee.to_dict()

        previous_status: Union[Unset, str] = UNSET
        if not isinstance(self.previous_status, Unset):
            previous_status = self.previous_status.value

        previous_title = self.previous_title

        updater: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updater, Unset):
            updater = self.updater.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "follow_up_id": follow_up_id,
            }
        )
        if new_assignee is not UNSET:
            field_dict["new_assignee"] = new_assignee
        if new_status is not UNSET:
            field_dict["new_status"] = new_status
        if new_title is not UNSET:
            field_dict["new_title"] = new_title
        if previous_assignee is not UNSET:
            field_dict["previous_assignee"] = previous_assignee
        if previous_status is not UNSET:
            field_dict["previous_status"] = previous_status
        if previous_title is not UNSET:
            field_dict["previous_title"] = previous_title
        if updater is not UNSET:
            field_dict["updater"] = updater

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.actor_v2 import ActorV2
        from ..models.user_v2 import UserV2

        d = src_dict.copy()
        follow_up_id = d.pop("follow_up_id")

        _new_assignee = d.pop("new_assignee", UNSET)
        new_assignee: Union[Unset, UserV2]
        if isinstance(_new_assignee, Unset):
            new_assignee = UNSET
        else:
            new_assignee = UserV2.from_dict(_new_assignee)

        _new_status = d.pop("new_status", UNSET)
        new_status: Union[Unset, ActivityFollowUpUpdatedV2NewStatus]
        if isinstance(_new_status, Unset):
            new_status = UNSET
        else:
            new_status = ActivityFollowUpUpdatedV2NewStatus(_new_status)

        new_title = d.pop("new_title", UNSET)

        _previous_assignee = d.pop("previous_assignee", UNSET)
        previous_assignee: Union[Unset, UserV2]
        if isinstance(_previous_assignee, Unset):
            previous_assignee = UNSET
        else:
            previous_assignee = UserV2.from_dict(_previous_assignee)

        _previous_status = d.pop("previous_status", UNSET)
        previous_status: Union[Unset, ActivityFollowUpUpdatedV2PreviousStatus]
        if isinstance(_previous_status, Unset):
            previous_status = UNSET
        else:
            previous_status = ActivityFollowUpUpdatedV2PreviousStatus(_previous_status)

        previous_title = d.pop("previous_title", UNSET)

        _updater = d.pop("updater", UNSET)
        updater: Union[Unset, ActorV2]
        if isinstance(_updater, Unset):
            updater = UNSET
        else:
            updater = ActorV2.from_dict(_updater)

        activity_follow_up_updated_v2 = cls(
            follow_up_id=follow_up_id,
            new_assignee=new_assignee,
            new_status=new_status,
            new_title=new_title,
            previous_assignee=previous_assignee,
            previous_status=previous_status,
            previous_title=previous_title,
            updater=updater,
        )

        activity_follow_up_updated_v2.additional_properties = d
        return activity_follow_up_updated_v2

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
