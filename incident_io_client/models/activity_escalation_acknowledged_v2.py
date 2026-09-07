from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_v2 import UserV2


T = TypeVar("T", bound="ActivityEscalationAcknowledgedV2")


@_attrs_define
class ActivityEscalationAcknowledgedV2:
    """
    Example:
        {'acknowledger': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'escalation_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        escalation_id (str): The escalation that was acknowledged Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        acknowledger (Union[Unset, UserV2]):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}.
    """

    escalation_id: str
    acknowledger: Union[Unset, "UserV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        escalation_id = self.escalation_id

        acknowledger: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.acknowledger, Unset):
            acknowledger = self.acknowledger.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "escalation_id": escalation_id,
            }
        )
        if acknowledger is not UNSET:
            field_dict["acknowledger"] = acknowledger

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_v2 import UserV2

        d = src_dict.copy()
        escalation_id = d.pop("escalation_id")

        _acknowledger = d.pop("acknowledger", UNSET)
        acknowledger: Union[Unset, UserV2]
        if isinstance(_acknowledger, Unset):
            acknowledger = UNSET
        else:
            acknowledger = UserV2.from_dict(_acknowledger)

        activity_escalation_acknowledged_v2 = cls(
            escalation_id=escalation_id,
            acknowledger=acknowledger,
        )

        activity_escalation_acknowledged_v2.additional_properties = d
        return activity_escalation_acknowledged_v2

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
