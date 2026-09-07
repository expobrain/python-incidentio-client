from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_update_type_payload_v3_categories_item import (
    CatalogUpdateTypePayloadV3CategoriesItem,
)
from ..models.catalog_update_type_payload_v3_color import (
    CatalogUpdateTypePayloadV3Color,
)
from ..models.catalog_update_type_payload_v3_icon import CatalogUpdateTypePayloadV3Icon
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_update_type_payload_v3_annotations import (
        CatalogUpdateTypePayloadV3Annotations,
    )


T = TypeVar("T", bound="CatalogUpdateTypePayloadV3")


@_attrs_define
class CatalogUpdateTypePayloadV3:
    """
    Example:
        {'annotations': {'incident.io/catalog-importer/id': 'id-of-config'}, 'categories': ['customer'], 'color':
            'yellow', 'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'icon': 'alert', 'name':
            'Kubernetes Cluster', 'owning_team_ids': ['01G0J1EXE7AXZ2C93K61WBPYEH'], 'ranked': True, 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog', 'use_name_as_identifier': True}

    Attributes:
        description (str): Human readble description of this type Example: Represents Kubernetes clusters that we run
            inside of GKE..
        name (str): Name is the human readable name of this type Example: Kubernetes Cluster.
        annotations (Union[Unset, CatalogUpdateTypePayloadV3Annotations]): Annotations that can track metadata about
            this type Example: {'incident.io/catalog-importer/id': 'id-of-config'}.
        categories (Union[Unset, List[CatalogUpdateTypePayloadV3CategoriesItem]]): What categories is this type
            considered part of Example: ['customer'].
        color (Union[Unset, CatalogUpdateTypePayloadV3Color]): Sets the display color of this type in the dashboard
            Example: yellow.
        icon (Union[Unset, CatalogUpdateTypePayloadV3Icon]): Sets the display icon of this type in the dashboard
            Example: alert.
        owning_team_ids (Union[Unset, List[str]]): IDs of the teams that own this catalog type Example:
            ['01G0J1EXE7AXZ2C93K61WBPYEH'].
        ranked (Union[Unset, bool]): If this type should be ranked Example: True.
        source_repo_url (Union[Unset, str]): The url of the external repository where this type is managed Example:
            https://github.com/my-company/incident-io-catalog.
        use_name_as_identifier (Union[Unset, bool]): If enabled, you can refer to entries of this type by their name, as
            well as their external ID and any aliases. Example: True.
    """

    description: str
    name: str
    annotations: Union[Unset, "CatalogUpdateTypePayloadV3Annotations"] = UNSET
    categories: Union[Unset, List[CatalogUpdateTypePayloadV3CategoriesItem]] = UNSET
    color: Union[Unset, CatalogUpdateTypePayloadV3Color] = UNSET
    icon: Union[Unset, CatalogUpdateTypePayloadV3Icon] = UNSET
    owning_team_ids: Union[Unset, List[str]] = UNSET
    ranked: Union[Unset, bool] = UNSET
    source_repo_url: Union[Unset, str] = UNSET
    use_name_as_identifier: Union[Unset, bool] = UNSET
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

        owning_team_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = self.owning_team_ids

        ranked = self.ranked

        source_repo_url = self.source_repo_url

        use_name_as_identifier = self.use_name_as_identifier

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
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids
        if ranked is not UNSET:
            field_dict["ranked"] = ranked
        if source_repo_url is not UNSET:
            field_dict["source_repo_url"] = source_repo_url
        if use_name_as_identifier is not UNSET:
            field_dict["use_name_as_identifier"] = use_name_as_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_update_type_payload_v3_annotations import (
            CatalogUpdateTypePayloadV3Annotations,
        )

        d = src_dict.copy()
        description = d.pop("description")

        name = d.pop("name")

        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, CatalogUpdateTypePayloadV3Annotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = CatalogUpdateTypePayloadV3Annotations.from_dict(_annotations)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = CatalogUpdateTypePayloadV3CategoriesItem(
                categories_item_data
            )

            categories.append(categories_item)

        _color = d.pop("color", UNSET)
        color: Union[Unset, CatalogUpdateTypePayloadV3Color]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CatalogUpdateTypePayloadV3Color(_color)

        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, CatalogUpdateTypePayloadV3Icon]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = CatalogUpdateTypePayloadV3Icon(_icon)

        owning_team_ids = cast(List[str], d.pop("owning_team_ids", UNSET))

        ranked = d.pop("ranked", UNSET)

        source_repo_url = d.pop("source_repo_url", UNSET)

        use_name_as_identifier = d.pop("use_name_as_identifier", UNSET)

        catalog_update_type_payload_v3 = cls(
            description=description,
            name=name,
            annotations=annotations,
            categories=categories,
            color=color,
            icon=icon,
            owning_team_ids=owning_team_ids,
            ranked=ranked,
            source_repo_url=source_repo_url,
            use_name_as_identifier=use_name_as_identifier,
        )

        catalog_update_type_payload_v3.additional_properties = d
        return catalog_update_type_payload_v3

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
