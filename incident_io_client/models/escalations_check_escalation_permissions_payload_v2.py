from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EscalationsCheckEscalationPermissionsPayloadV2")


@_attrs_define
class EscalationsCheckEscalationPermissionsPayloadV2:
    """
    Example:
        {'user_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH']}

    Attributes:
        user_ids (List[str]): The IDs of the users to check response options for Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
    """

    user_ids: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_ids = self.user_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_ids": user_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_ids = cast(List[str], d.pop("user_ids"))

        escalations_check_escalation_permissions_payload_v2 = cls(
            user_ids=user_ids,
        )

        escalations_check_escalation_permissions_payload_v2.additional_properties = d
        return escalations_check_escalation_permissions_payload_v2

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
