from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EscalationPathNodeEscalationPathV2")


@_attrs_define
class EscalationPathNodeEscalationPathV2:
    """
    Example:
        {'escalation_path_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        escalation_path_id (str): The ID of the escalation path to reassign to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    escalation_path_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        escalation_path_id = self.escalation_path_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "escalation_path_id": escalation_path_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        escalation_path_id = d.pop("escalation_path_id")

        escalation_path_node_escalation_path_v2 = cls(
            escalation_path_id=escalation_path_id,
        )

        escalation_path_node_escalation_path_v2.additional_properties = d
        return escalation_path_node_escalation_path_v2

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
