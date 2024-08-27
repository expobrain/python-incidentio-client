from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_resource_v2_category import CatalogResourceV2Category

T = TypeVar("T", bound="CatalogResourceV2")


@_attrs_define
class CatalogResourceV2:
    """
    Example:
        {'category': 'custom', 'description': 'Boolean true or false value', 'label': 'GitHub Repository', 'type':
            'CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"]', 'value_docstring': 'Either the GraphQL node ID of the repository
            or a string of <owner>/<repo>, e.g. incident-io/website'}

    Attributes:
        category (CatalogResourceV2Category): Which category of resource Example: custom.
        description (str): Human readable description for this resource Example: Boolean true or false value.
        label (str): Label for this catalog resource type Example: GitHub Repository.
        type (str): Catalog type name for this resource Example: CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"].
        value_docstring (str): Documentation for the literal string value of this resource Example: Either the GraphQL
            node ID of the repository or a string of <owner>/<repo>, e.g. incident-io/website.
    """

    category: CatalogResourceV2Category
    description: str
    label: str
    type: str
    value_docstring: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category.value

        description = self.description

        label = self.label

        type = self.type

        value_docstring = self.value_docstring

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "description": description,
                "label": label,
                "type": type,
                "value_docstring": value_docstring,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = CatalogResourceV2Category(d.pop("category"))

        description = d.pop("description")

        label = d.pop("label")

        type = d.pop("type")

        value_docstring = d.pop("value_docstring")

        catalog_resource_v2 = cls(
            category=category,
            description=description,
            label=label,
            type=type,
            value_docstring=value_docstring,
        )

        catalog_resource_v2.additional_properties = d
        return catalog_resource_v2

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
