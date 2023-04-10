from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.catalog_v2_update_type_request_body_color import (
    CatalogV2UpdateTypeRequestBodyColor,
)
from ..models.catalog_v2_update_type_request_body_icon import (
    CatalogV2UpdateTypeRequestBodyIcon,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogV2UpdateTypeRequestBody")


@attr.s(auto_attribs=True)
class CatalogV2UpdateTypeRequestBody:
    """
    Example:
        {'color': 'slate', 'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'box',
            'name': 'Kubernetes Cluster', 'ranked': True, 'semantic_type': 'custom'}

    Attributes:
        description (str): Human readble description of this type Example: Represents Kubernetes clusters that we run
            inside of GKE..
        name (str): Name is the human readable name of this type Example: Kubernetes Cluster.
        color (Union[Unset, CatalogV2UpdateTypeRequestBodyColor]): Sets the display color of this type in the dashboard
            Example: slate.
        icon (Union[Unset, CatalogV2UpdateTypeRequestBodyIcon]): Sets the display icon of this type in the dashboard
            Example: box.
        ranked (Union[Unset, bool]): If this type should be ranked Example: True.
        semantic_type (Union[Unset, str]): Semantic type of this resource Example: custom.
    """

    description: str
    name: str
    color: Union[Unset, CatalogV2UpdateTypeRequestBodyColor] = UNSET
    icon: Union[Unset, CatalogV2UpdateTypeRequestBodyIcon] = UNSET
    ranked: Union[Unset, bool] = UNSET
    semantic_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name
        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        icon: Union[Unset, str] = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.value

        ranked = self.ranked
        semantic_type = self.semantic_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if ranked is not UNSET:
            field_dict["ranked"] = ranked
        if semantic_type is not UNSET:
            field_dict["semantic_type"] = semantic_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        name = d.pop("name")

        _color = d.pop("color", UNSET)
        color: Union[Unset, CatalogV2UpdateTypeRequestBodyColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CatalogV2UpdateTypeRequestBodyColor(_color)

        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, CatalogV2UpdateTypeRequestBodyIcon]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = CatalogV2UpdateTypeRequestBodyIcon(_icon)

        ranked = d.pop("ranked", UNSET)

        semantic_type = d.pop("semantic_type", UNSET)

        catalog_v2_update_type_request_body = cls(
            description=description,
            name=name,
            color=color,
            icon=icon,
            ranked=ranked,
            semantic_type=semantic_type,
        )

        catalog_v2_update_type_request_body.additional_properties = d
        return catalog_v2_update_type_request_body

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
