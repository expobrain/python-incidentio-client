from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionsCreatePayloadV2")


@_attrs_define
class ActionsCreatePayloadV2:
    """
    Example:
        {'assignee_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'description': 'Call the fire brigade', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYD5H'}

    Attributes:
        description (str): Description of the action. Supports Markdown. Example: Call the fire brigade.
        incident_id (str): Unique identifier of the incident the action belongs to Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        assignee_id (Union[Unset, str]): ID of the user this action is assigned to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    description: str
    incident_id: str
    assignee_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        incident_id = self.incident_id

        assignee_id = self.assignee_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "incident_id": incident_id,
            }
        )
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        incident_id = d.pop("incident_id")

        assignee_id = d.pop("assignee_id", UNSET)

        actions_create_payload_v2 = cls(
            description=description,
            incident_id=incident_id,
            assignee_id=assignee_id,
        )

        actions_create_payload_v2.additional_properties = d
        return actions_create_payload_v2

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
