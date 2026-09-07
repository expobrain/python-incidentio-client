from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_actor_v2 import AlertActorV2
    from ..models.user_v2 import UserV2
    from ..models.workflow_actor_v2 import WorkflowActorV2


T = TypeVar("T", bound="EscalationCreatorV2")


@_attrs_define
class EscalationCreatorV2:
    """The creator of this escalation. Can be a user, a workflow, or an alert. If the escalation came from a call route,
    this will be empty.

        Example:
            {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
                'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role':
                'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
                workflow'}}

        Attributes:
            alert (Union[Unset, AlertActorV2]):  Example: {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
                '*errors.withMessage: PG::Error failed to connect'}.
            user (Union[Unset, UserV2]):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
                'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
            workflow (Union[Unset, WorkflowActorV2]):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
                workflow'}.
    """

    alert: Union[Unset, "AlertActorV2"] = UNSET
    user: Union[Unset, "UserV2"] = UNSET
    workflow: Union[Unset, "WorkflowActorV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        workflow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert is not UNSET:
            field_dict["alert"] = alert
        if user is not UNSET:
            field_dict["user"] = user
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_actor_v2 import AlertActorV2
        from ..models.user_v2 import UserV2
        from ..models.workflow_actor_v2 import WorkflowActorV2

        d = src_dict.copy()
        _alert = d.pop("alert", UNSET)
        alert: Union[Unset, AlertActorV2]
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = AlertActorV2.from_dict(_alert)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserV2]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserV2.from_dict(_user)

        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, WorkflowActorV2]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = WorkflowActorV2.from_dict(_workflow)

        escalation_creator_v2 = cls(
            alert=alert,
            user=user,
            workflow=workflow,
        )

        escalation_creator_v2.additional_properties = d
        return escalation_creator_v2

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
