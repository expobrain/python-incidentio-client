from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleLayerUpdatePayloadV2RequestBody")


@_attrs_define
class ScheduleLayerUpdatePayloadV2RequestBody:
    """
    Example:
        {'id': '01G0J1EXE7AXZ2C93K61WBPYEH', 'name': 'Layer 1'}

    Attributes:
        id (Union[Unset, str]): Unique identifier of the layer Example: 01G0J1EXE7AXZ2C93K61WBPYEH.
        name (Union[Unset, str]): Name of the layer Example: Layer 1.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        schedule_layer_update_payload_v2_request_body = cls(
            id=id,
            name=name,
        )

        schedule_layer_update_payload_v2_request_body.additional_properties = d
        return schedule_layer_update_payload_v2_request_body

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
