from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PolicyFindingFollowUpV2")


@_attrs_define
class PolicyFindingFollowUpV2:
    """Set when policy_type is follow_up.

    Example:
        {'follow_up_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        follow_up_id (str): The follow-up that fell short of the policy Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        incident_id (str): The incident the follow-up belongs to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    follow_up_id: str
    incident_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        follow_up_id = self.follow_up_id

        incident_id = self.incident_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "follow_up_id": follow_up_id,
                "incident_id": incident_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        follow_up_id = d.pop("follow_up_id")

        incident_id = d.pop("incident_id")

        policy_finding_follow_up_v2 = cls(
            follow_up_id=follow_up_id,
            incident_id=incident_id,
        )

        policy_finding_follow_up_v2.additional_properties = d
        return policy_finding_follow_up_v2

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
