from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_attribute_v2 import AlertAttributeV2
    from ..models.alert_attribute_value_v2 import AlertAttributeValueV2


T = TypeVar("T", bound="AlertAttributeEntryV2")


@_attrs_define
class AlertAttributeEntryV2:
    """
    Example:
        {'array_value': [{'catalog_entry': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'label': 'Payments Team', 'literal': 'SEV123'}],
            'attribute': {'array': False, 'emoji': 'fire', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'service',
            'required': False, 'type': 'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}, 'value': {'catalog_entry':
            {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-
            call'}, 'label': 'Payments Team', 'literal': 'SEV123'}}

    Attributes:
        attribute (AlertAttributeV2):  Example: {'array': False, 'emoji': 'fire', 'id': '01GW2G3V0S59R238FAHPDS1R66',
            'name': 'service', 'required': False, 'type': 'CatalogEntry["01GW2G3V0S59R238FAHPDS1R67"]'}.
        array_value (Union[Unset, List['AlertAttributeValueV2']]): The value of the attribute if it is an array Example:
            [{'catalog_entry': {'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Primary On-call'}, 'label': 'Payments Team', 'literal': 'SEV123'}].
        value (Union[Unset, AlertAttributeValueV2]):  Example: {'catalog_entry': {'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}, 'label': 'Payments
            Team', 'literal': 'SEV123'}.
    """

    attribute: "AlertAttributeV2"
    array_value: Union[Unset, List["AlertAttributeValueV2"]] = UNSET
    value: Union[Unset, "AlertAttributeValueV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute = self.attribute.to_dict()

        array_value: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.array_value, Unset):
            array_value = []
            for array_value_item_data in self.array_value:
                array_value_item = array_value_item_data.to_dict()
                array_value.append(array_value_item)

        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute": attribute,
            }
        )
        if array_value is not UNSET:
            field_dict["array_value"] = array_value
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_attribute_v2 import AlertAttributeV2
        from ..models.alert_attribute_value_v2 import AlertAttributeValueV2

        d = src_dict.copy()
        attribute = AlertAttributeV2.from_dict(d.pop("attribute"))

        array_value = []
        _array_value = d.pop("array_value", UNSET)
        for array_value_item_data in _array_value or []:
            array_value_item = AlertAttributeValueV2.from_dict(array_value_item_data)

            array_value.append(array_value_item)

        _value = d.pop("value", UNSET)
        value: Union[Unset, AlertAttributeValueV2]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = AlertAttributeValueV2.from_dict(_value)

        alert_attribute_entry_v2 = cls(
            attribute=attribute,
            array_value=array_value,
            value=value,
        )

        alert_attribute_entry_v2.additional_properties = d
        return alert_attribute_entry_v2

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
