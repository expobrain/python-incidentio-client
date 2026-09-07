from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_structure_component_v2 import (
        StatusPageStructureComponentV2,
    )
    from ..models.status_page_structure_group_v2 import StatusPageStructureGroupV2


T = TypeVar("T", bound="StatusPageStructureSubPageItemV2")


@_attrs_define
class StatusPageStructureSubPageItemV2:
    """
    Example:
        {'component': {'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}, 'group': {'components':
            [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU
            Data center'}}

    Attributes:
        component (Union[Unset, StatusPageStructureComponentV2]):  Example: {'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}.
        group (Union[Unset, StatusPageStructureGroupV2]):  Example: {'components': [{'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'App'}], 'id': '01FCNDV6P870EA6S7TK1DSYDG1', 'name': 'EU Data center'}.
    """

    component: Union[Unset, "StatusPageStructureComponentV2"] = UNSET
    group: Union[Unset, "StatusPageStructureGroupV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        component: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.component, Unset):
            component = self.component.to_dict()

        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component is not UNSET:
            field_dict["component"] = component
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.status_page_structure_component_v2 import (
            StatusPageStructureComponentV2,
        )
        from ..models.status_page_structure_group_v2 import StatusPageStructureGroupV2

        d = src_dict.copy()
        _component = d.pop("component", UNSET)
        component: Union[Unset, StatusPageStructureComponentV2]
        if isinstance(_component, Unset):
            component = UNSET
        else:
            component = StatusPageStructureComponentV2.from_dict(_component)

        _group = d.pop("group", UNSET)
        group: Union[Unset, StatusPageStructureGroupV2]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = StatusPageStructureGroupV2.from_dict(_group)

        status_page_structure_sub_page_item_v2 = cls(
            component=component,
            group=group,
        )

        status_page_structure_sub_page_item_v2.additional_properties = d
        return status_page_structure_sub_page_item_v2

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
