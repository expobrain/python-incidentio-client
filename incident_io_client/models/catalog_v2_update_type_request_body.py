from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_v2_update_type_request_body_categories_item import (
    CatalogV2UpdateTypeRequestBodyCategoriesItem,
)
from ..models.catalog_v2_update_type_request_body_color import (
    CatalogV2UpdateTypeRequestBodyColor,
)
from ..models.catalog_v2_update_type_request_body_icon import (
    CatalogV2UpdateTypeRequestBodyIcon,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_v2_update_type_request_body_annotations import (
        CatalogV2UpdateTypeRequestBodyAnnotations,
    )


T = TypeVar("T", bound="CatalogV2UpdateTypeRequestBody")


@_attrs_define
class CatalogV2UpdateTypeRequestBody:
    """
    Example:
        {'annotations': {'incident.io/catalog-importer/id': 'id-of-config'}, 'categories': ['issue-tracker'], 'color':
            'yellow', 'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'alert', 'name':
            'Kubernetes Cluster', 'ranked': True, 'source_repo_url': 'https://github.com/my-company/incident-io-catalog'}

    Attributes:
        description (str): Human readble description of this type Example: Represents Kubernetes clusters that we run
            inside of GKE..
        name (str): Name is the human readable name of this type Example: Kubernetes Cluster.
        annotations (Union[Unset, CatalogV2UpdateTypeRequestBodyAnnotations]): Annotations that can track metadata about
            this type Example: {'incident.io/catalog-importer/id': 'id-of-config'}.
        categories (Union[Unset, List[CatalogV2UpdateTypeRequestBodyCategoriesItem]]): What categories is this type
            considered part of Example: ['issue-tracker'].
        color (Union[Unset, CatalogV2UpdateTypeRequestBodyColor]): Sets the display color of this type in the dashboard
            Example: yellow.
        icon (Union[Unset, CatalogV2UpdateTypeRequestBodyIcon]): Sets the display icon of this type in the dashboard
            Example: alert.
        ranked (Union[Unset, bool]): If this type should be ranked Example: True.
        source_repo_url (Union[Unset, str]): The url of the external repository where this type is managed Example:
            https://github.com/my-company/incident-io-catalog.
    """

    description: str
    name: str
    annotations: Union[Unset, "CatalogV2UpdateTypeRequestBodyAnnotations"] = UNSET
    categories: Union[Unset, list[CatalogV2UpdateTypeRequestBodyCategoriesItem]] = UNSET
    color: Union[Unset, CatalogV2UpdateTypeRequestBodyColor] = UNSET
    icon: Union[Unset, CatalogV2UpdateTypeRequestBodyIcon] = UNSET
    ranked: Union[Unset, bool] = UNSET
    source_repo_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        annotations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        categories: Union[Unset, list[str]] = UNSET
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

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.catalog_v2_update_type_request_body_annotations import (
            CatalogV2UpdateTypeRequestBodyAnnotations,
        )

        d = src_dict.copy()
        description = d.pop("description")

        name = d.pop("name")

        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, CatalogV2UpdateTypeRequestBodyAnnotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = CatalogV2UpdateTypeRequestBodyAnnotations.from_dict(_annotations)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = CatalogV2UpdateTypeRequestBodyCategoriesItem(categories_item_data)

            categories.append(categories_item)

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

        source_repo_url = d.pop("source_repo_url", UNSET)

        catalog_v2_update_type_request_body = cls(
            description=description,
            name=name,
            annotations=annotations,
            categories=categories,
            color=color,
            icon=icon,
            ranked=ranked,
            source_repo_url=source_repo_url,
        )

        catalog_v2_update_type_request_body.additional_properties = d
        return catalog_v2_update_type_request_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
