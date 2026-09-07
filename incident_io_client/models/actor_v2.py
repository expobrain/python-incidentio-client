from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_actor_v2 import AlertActorV2
    from ..models.api_key_actor_v2 import APIKeyActorV2
    from ..models.user_v2 import UserV2
    from ..models.workflow_actor_v2 import WorkflowActorV2


T = TypeVar("T", bound="ActorV2")


@_attrs_define
class ActorV2:
    """
    Example:
        {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title': '*errors.withMessage: PG::Error failed to connect'},
            'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'owner',
            'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}

    Attributes:
        alert (Union[Unset, AlertActorV2]):  Example: {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}.
        api_key (Union[Unset, APIKeyActorV2]):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API
            key'}.
        user (Union[Unset, UserV2]):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
        workflow (Union[Unset, WorkflowActorV2]):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little
            workflow'}.
    """

    alert: Union[Unset, "AlertActorV2"] = UNSET
    api_key: Union[Unset, "APIKeyActorV2"] = UNSET
    user: Union[Unset, "UserV2"] = UNSET
    workflow: Union[Unset, "WorkflowActorV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        api_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api_key, Unset):
            api_key = self.api_key.to_dict()

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
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if user is not UNSET:
            field_dict["user"] = user
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_actor_v2 import AlertActorV2
        from ..models.api_key_actor_v2 import APIKeyActorV2
        from ..models.user_v2 import UserV2
        from ..models.workflow_actor_v2 import WorkflowActorV2

        d = src_dict.copy()
        _alert = d.pop("alert", UNSET)
        alert: Union[Unset, AlertActorV2]
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = AlertActorV2.from_dict(_alert)

        _api_key = d.pop("api_key", UNSET)
        api_key: Union[Unset, APIKeyActorV2]
        if isinstance(_api_key, Unset):
            api_key = UNSET
        else:
            api_key = APIKeyActorV2.from_dict(_api_key)

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

        actor_v2 = cls(
            alert=alert,
            api_key=api_key,
            user=user,
            workflow=workflow,
        )

        actor_v2.additional_properties = d
        return actor_v2

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
