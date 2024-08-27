from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_resource_v2 import CatalogResourceV2


T = TypeVar("T", bound="CatalogV2ListResourcesResponseBody")


@_attrs_define
class CatalogV2ListResourcesResponseBody:
    """
    Example:
        {'resources': [{'category': 'custom', 'description': 'Boolean true or false value', 'label': 'GitHub
            Repository', 'type': 'CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"]', 'value_docstring': 'Either the GraphQL node
            ID of the repository or a string of <owner>/<repo>, e.g. incident-io/website'}]}

    Attributes:
        resources (List['CatalogResourceV2']):  Example: [{'category': 'custom', 'description': 'Boolean true or false
            value', 'label': 'GitHub Repository', 'type': 'CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"]', 'value_docstring':
            'Either the GraphQL node ID of the repository or a string of <owner>/<repo>, e.g. incident-io/website'}].
    """

    resources: List["CatalogResourceV2"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resources": resources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_resource_v2 import CatalogResourceV2

        d = src_dict.copy()
        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = CatalogResourceV2.from_dict(resources_item_data)

            resources.append(resources_item)

        catalog_v2_list_resources_response_body = cls(
            resources=resources,
        )

        catalog_v2_list_resources_response_body.additional_properties = d
        return catalog_v2_list_resources_response_body

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
