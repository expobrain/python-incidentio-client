from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.escalation_user_response_options_v2 import (
        EscalationUserResponseOptionsV2,
    )


T = TypeVar("T", bound="EscalationsCheckEscalationPermissionsResultV2")


@_attrs_define
class EscalationsCheckEscalationPermissionsResultV2:
    """
    Example:
        {'response_options': [{'available_actions': ['ack', 'nack', 'snooze'], 'user_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH'}]}

    Attributes:
        response_options (List['EscalationUserResponseOptionsV2']): The response options available to each requested
            user, in the same order as the request. Example: [{'available_actions': ['ack', 'nack', 'snooze'], 'user_id':
            '01G0J1EXE7AXZ2C93K61WBPYEH'}].
    """

    response_options: List["EscalationUserResponseOptionsV2"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        response_options = []
        for response_options_item_data in self.response_options:
            response_options_item = response_options_item_data.to_dict()
            response_options.append(response_options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response_options": response_options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.escalation_user_response_options_v2 import (
            EscalationUserResponseOptionsV2,
        )

        d = src_dict.copy()
        response_options = []
        _response_options = d.pop("response_options")
        for response_options_item_data in _response_options:
            response_options_item = EscalationUserResponseOptionsV2.from_dict(
                response_options_item_data
            )

            response_options.append(response_options_item)

        escalations_check_escalation_permissions_result_v2 = cls(
            response_options=response_options,
        )

        escalations_check_escalation_permissions_result_v2.additional_properties = d
        return escalations_check_escalation_permissions_result_v2

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
