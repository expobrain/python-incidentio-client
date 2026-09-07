from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_update_type_payload_v2_categories_item import (
    CatalogUpdateTypePayloadV2CategoriesItem,
)
from ..models.catalog_update_type_payload_v2_color import (
    CatalogUpdateTypePayloadV2Color,
)
from ..models.catalog_update_type_payload_v2_icon import CatalogUpdateTypePayloadV2Icon
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_update_type_payload_v2_annotations import (
        CatalogUpdateTypePayloadV2Annotations,
    )


T = TypeVar("T", bound="CatalogUpdateTypePayloadV2")


@_attrs_define
class CatalogUpdateTypePayloadV2:
    """
    Example:
        {'annotations': {'incident.io/catalog-importer/id': 'id-of-config'}, 'categories': ['customer'], 'color':
            'yellow', 'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'alert', 'name':
            'Kubernetes Cluster', 'ranked': True, 'source_repo_url': 'https://github.com/my-company/incident-io-catalog'}

    Attributes:
        description (str): Human readble description of this type Example: Represents Kubernetes clusters that we run
            inside of GKE..
        name (str): Name is the human readable name of this type Example: Kubernetes Cluster.
        annotations (Union[Unset, CatalogUpdateTypePayloadV2Annotations]): Annotations that can track metadata about
            this type Example: {'incident.io/catalog-importer/id': 'id-of-config'}.
        categories (Union[Unset, List[CatalogUpdateTypePayloadV2CategoriesItem]]): What categories is this type
            considered part of Example: ['customer'].
        color (Union[Unset, CatalogUpdateTypePayloadV2Color]): Sets the display color of this type in the dashboard
            Example: yellow.
        icon (Union[Unset, CatalogUpdateTypePayloadV2Icon]): Sets the display icon of this type in the dashboard
            Example: alert.
        ranked (Union[Unset, bool]): If this type should be ranked Example: True.
        source_repo_url (Union[Unset, str]): The url of the external repository where this type is managed Example:
            https://github.com/my-company/incident-io-catalog.
    """

    description: str
    name: str
    annotations: Union[Unset, "CatalogUpdateTypePayloadV2Annotations"] = UNSET
    categories: Union[Unset, List[CatalogUpdateTypePayloadV2CategoriesItem]] = UNSET
    color: Union[Unset, CatalogUpdateTypePayloadV2Color] = UNSET
    icon: Union[Unset, CatalogUpdateTypePayloadV2Icon] = UNSET
    ranked: Union[Unset, bool] = UNSET
    source_repo_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        name = self.name

        annotations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        categories: Union[Unset, List[str]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.value
                categories.append(categories_item)

        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        icon: Union[Unset, str] = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.value

        ranked = self.ranked

        source_repo_url = self.source_repo_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
            }
        )
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if categories is not UNSET:
            field_dict["categories"] = categories
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if ranked is not UNSET:
            field_dict["ranked"] = ranked
        if source_repo_url is not UNSET:
            field_dict["source_repo_url"] = source_repo_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_update_type_payload_v2_annotations import (
            CatalogUpdateTypePayloadV2Annotations,
        )

        d = src_dict.copy()
        description = d.pop("description")

        name = d.pop("name")

        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, CatalogUpdateTypePayloadV2Annotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = CatalogUpdateTypePayloadV2Annotations.from_dict(_annotations)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = CatalogUpdateTypePayloadV2CategoriesItem(
                categories_item_data
            )

            categories.append(categories_item)

        _color = d.pop("color", UNSET)
        color: Union[Unset, CatalogUpdateTypePayloadV2Color]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CatalogUpdateTypePayloadV2Color(_color)

        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, CatalogUpdateTypePayloadV2Icon]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = CatalogUpdateTypePayloadV2Icon(_icon)

        ranked = d.pop("ranked", UNSET)

        source_repo_url = d.pop("source_repo_url", UNSET)

        catalog_update_type_payload_v2 = cls(
            description=description,
            name=name,
            annotations=annotations,
            categories=categories,
            color=color,
            icon=icon,
            ranked=ranked,
            source_repo_url=source_repo_url,
        )

        catalog_update_type_payload_v2.additional_properties = d
        return catalog_update_type_payload_v2

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
