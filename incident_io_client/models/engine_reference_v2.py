from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EngineReferenceV2")


@_attrs_define
class EngineReferenceV2:
    """
    Example:
        {'array': False, 'key': 'incident.custom_field["01FCNDV6P870EA6S7TK1DSYDG0"]', 'label': 'Incident -> Affected
            Team', 'type': 'IncidentSeverity'}

    Attributes:
        array (bool): If true, the reference can refer to 0 to many items
        key (str): The key of the field this is a reference to Example:
            incident.custom_field["01FCNDV6P870EA6S7TK1DSYDG0"].
        label (str): Human readable label for the field (with context) Example: Incident -> Affected Team.
        type (str): The type of this resource in the engine Example: IncidentSeverity.
    """

    array: bool
    key: str
    label: str
    type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        array = self.array

        key = self.key

        label = self.label

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "key": key,
                "label": label,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        array = d.pop("array")

        key = d.pop("key")

        label = d.pop("label")

        type = d.pop("type")

        engine_reference_v2 = cls(
            array=array,
            key=key,
            label=label,
            type=type,
        )

        engine_reference_v2.additional_properties = d
        return engine_reference_v2

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
