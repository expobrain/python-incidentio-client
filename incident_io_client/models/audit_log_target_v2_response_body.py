from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_log_target_v2_response_body_type import (
    AuditLogTargetV2ResponseBodyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogTargetV2ResponseBody")


@_attrs_define
class AuditLogTargetV2ResponseBody:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'John Doe', 'type': 'user'}

    Attributes:
        id (str): The ID of the target Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        type (AuditLogTargetV2ResponseBodyType): The type of target Example: user.
        name (Union[Unset, str]): The name of the target Example: John Doe.
    """

    id: str
    type: AuditLogTargetV2ResponseBodyType
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type.value

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = AuditLogTargetV2ResponseBodyType(d.pop("type"))

        name = d.pop("name", UNSET)

        audit_log_target_v2_response_body = cls(
            id=id,
            type=type,
            name=name,
        )

        audit_log_target_v2_response_body.additional_properties = d
        return audit_log_target_v2_response_body

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
