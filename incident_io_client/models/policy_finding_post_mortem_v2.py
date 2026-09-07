from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PolicyFindingPostMortemV2")


@_attrs_define
class PolicyFindingPostMortemV2:
    """Set when policy_type is post_mortem.

    Example:
        {'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        incident_id (str): The incident whose post-mortem fell short of the policy Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    incident_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_id = self.incident_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_id": incident_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        incident_id = d.pop("incident_id")

        policy_finding_post_mortem_v2 = cls(
            incident_id=incident_id,
        )

        policy_finding_post_mortem_v2.additional_properties = d
        return policy_finding_post_mortem_v2

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
